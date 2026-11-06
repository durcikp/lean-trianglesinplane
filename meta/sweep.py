"""Find labels in automation/Status.md that are now fully proved but still marked
"Statement completed", and emit a batch file for meta/setstatus.py.

Robustness: a single `import Auto` sweep dies whenever ANY module is mid-rebuild by a
concurrent agent, and the failure is indistinguishable from "nothing new" unless you check
the error count. So this groups the Lean names by the module that defines them and checks
each module separately, skipping (and reporting) only the modules that fail to load.

usage: python3 meta/sweep.py [out_batch_file]
Then:  python3 meta/setstatus.py --batch <out_batch_file>
"""
import re, subprocess, sys, os, collections

OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-502/sweep_out.txt'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# label -> [lean names], for entries not yet marked Proof completed
labels = {}
for line in open('automation/Status.md'):
    m = re.match(r'\\label\{([^}]*)\}: \[Statement completed\] \(Lean: ([^)]*)\)', line)
    if m:
        ns = [n.strip() for n in m.group(2).split(',') if n.strip()]
        if ns:
            labels[m.group(1)] = ns

# map each Lean name to the module that declares it
want = {n for ns in labels.values() for n in ns}
name2mod = {}
for dirpath, _dirs, files in os.walk('Auto'):
    if 'Scratch' in dirpath:
        continue
    for fn in files:
        if not fn.endswith('.lean'):
            continue
        path = os.path.join(dirpath, fn)
        mod = path[:-5].replace(os.sep, '.')
        text = open(path, encoding='utf-8').read()
        for n in want:
            short = n.split('.')[-1]
            if re.search(r'(?m)^(noncomputable )?(theorem|lemma|def|abbrev|structure|instance) '
                         + re.escape(short) + r'\b', text):
                name2mod[n] = mod

bymod = collections.defaultdict(list)
missing = []
for n in want:
    if n in name2mod:
        bymod[name2mod[n]].append(n)
    else:
        missing.append(n)

clean, failed = set(), []
os.makedirs('Auto/Scratch', exist_ok=True)
for mod, names in sorted(bymod.items()):
    f = 'Auto/Scratch/_sweep_tmp.lean'
    with open(f, 'w') as fh:
        fh.write(f"import {mod}\nset_option maxHeartbeats 1000000\n"
                 + "\n".join(f"#print axioms {n}" for n in names) + "\n")
    r = subprocess.run(['lake', 'env', 'lean', f], capture_output=True, text=True)
    out = r.stdout + r.stderr
    if 'does not exist' in out or 'error:' in out and 'depends on axioms' not in out:
        failed.append(mod)
        continue
    for line in out.splitlines():
        m = re.match(r"'(\S+)' depends on axioms: \[(.*)\]", line.strip())
        if m and 'sorryAx' not in m.group(2):
            clean.add(m.group(1))
if os.path.exists('Auto/Scratch/_sweep_tmp.lean'):
    os.remove('Auto/Scratch/_sweep_tmp.lean')

done = [(lab, ns) for lab, ns in labels.items() if all(n in clean for n in ns)]
with open(OUT, 'w') as fh:
    for lab, ns in done:
        fh.write(f"{lab}|Proof completed|{', '.join(ns)}\n")

print(f"checked {len(bymod)} modules, {len(want)} names")
if failed:
    print(f"SKIPPED (module would not load, retry later): {failed}")
if missing:
    print(f"NAME NOT FOUND in any module: {missing}")
print(f"newly complete labels ({len(done)}): {[l for l, _ in done]}")
print(f"batch written to {OUT}")
