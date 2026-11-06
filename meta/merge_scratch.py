"""Merge proofs from a scratch file into a section file.
usage: merge_scratch.py SCRATCH MAIN
Scratch theorems named NAME_scratch replace the `sorry` proof of NAME in MAIN; all other
declarations (aux_ lemmas) are inserted before the first replaced theorem (with its docstring).
"""
import re, sys
scratch, main = sys.argv[1], sys.argv[2]
s = open(scratch).read()
m = open(main).read()
lines = s.split('\n')
# drop header and footer
body = []
started = False
for l in lines:
    if not started:
        if l.startswith('/--') or re.match(r'(theorem|lemma|def|noncomputable|instance|private|@\[|open scoped Classical in|set_option)', l):
            started = True
        else:
            continue
    body.append(l)
while body and (body[-1].strip() == '' or body[-1].startswith('end Auto')):
    body.pop()
text = '\n'.join(body)
# split into chunks at top-level starts
starts = [mt.start() for mt in re.finditer(r'(?m)^(/--|theorem |lemma |def |noncomputable def |abbrev |structure |instance |open scoped Classical in|@\[|set_option )', text)]
chunks = []
i = 0
while i < len(starts):
    a = starts[i]
    # glue docstring/attribute/open-in to next decl
    j = i
    while j + 1 < len(starts) and re.match(r'(/--|open scoped Classical in|@\[|set_option )', text[starts[j]:]) and not re.search(r'(?m)^(theorem|lemma|def|noncomputable def|abbrev|structure|instance) ', text[starts[j]:starts[j+1]]):
        j += 1
    b = starts[j + 1] if j + 1 < len(starts) else len(text)
    chunks.append(text[a:b].rstrip() + '\n')
    i = j + 1
aux_for = {}   # target name -> aux chunks appearing before it in the scratch file
pending, proofs, order = [], {}, []
for c in chunks:
    c2 = re.sub(r'\b(\w+)_scratch\b', r'\1', c)
    mt = re.search(r'(?m)^theorem (\S+)_scratch\b', c)
    if mt:
        name = mt.group(1)
        k1 = c2.find(':= by\n'); k2 = c2.find(':=\n')
        if k1 < 0 and k2 < 0:
            sys.exit('no := in ' + name)
        if k1 >= 0 and (k2 < 0 or k1 < k2):
            proofs[name] = ':= by\n' + c2[k1 + len(':= by\n'):]
        else:
            proofs[name] = ':=\n' + c2[k2 + len(':=\n'):]
        aux_for[name] = pending; pending = []; order.append(name)
    else:
        pending.append(c2)
if pending and order:
    aux_for[order[-1]] += pending
naux = 0
for name in order:
    proof = proofs[name]
    pat = re.compile(r'(?m)^theorem ' + re.escape(name) + r'\b')
    mt = pat.search(m)
    if not mt:
        sys.exit('theorem not found in main: ' + name)
    k = m.find(':= by\n  sorry\n', mt.start())
    nxt = re.compile(r'(?m)^(theorem|lemma|def|noncomputable def|/--) ').search(m, mt.end())
    if k < 0 or (nxt and k > nxt.start()):
        sys.exit('sorry proof not found for ' + name)
    m = m[:k] + proof.rstrip() + '\n' + m[k + len(':= by\n  sorry\n'):]
    if aux_for[name]:
        mt = pat.search(m)
        d = m.rfind('/--', 0, mt.start())
        pos = d if d >= 0 and m[m.find('-/', d)+2:mt.start()].strip() == '' else mt.start()
        pre = m.rfind('\n', 0, pos - 1)
        if m[pre+1:pos].strip() == 'open scoped Classical in':
            pos = pre + 1
        m = m[:pos] + '\n'.join(aux_for[name]) + '\n' + m[pos:]
        naux += len(aux_for[name])
print('merged', order, 'aux:', naux)
# carry over `open` namespaces used in the scratch header
import itertools
sopens = set(itertools.chain.from_iterable(l.split()[1:] for l in lines if l.startswith('open ') and not l.startswith('open scoped') and ' in' not in l))
mlines = m.split('\n')
for idx, l in enumerate(mlines):
    if l.startswith('open ') and not l.startswith('open scoped'):
        have = set(l.split()[1:])
        missing = [o for o in sorted(sopens) if o not in have]
        if missing:
            mlines[idx] = l + ' ' + ' '.join(missing)
            print('added opens', missing)
        break
sso = set(itertools.chain.from_iterable(l.split()[2:] for l in lines if l.startswith('open scoped') and ' in' not in l))
for idx, l in enumerate(mlines):
    if l.startswith('open scoped'):
        have = set(l.split()[2:])
        missing = [o for o in sorted(sso) if o not in have]
        if missing:
            mlines[idx] = l + ' ' + ' '.join(missing)
            print('added scoped opens', missing)
        break
m = '\n'.join(mlines)
open(main, 'w').write(m)
