"""Update automation/Status.md entries and the matching blueprint Lean metadata.

usage: python3 meta/setstatus.py LABEL STATUS "Auto.name1, Auto.name2"
   or: python3 meta/setstatus.py --batch FILE   (lines: LABEL|STATUS|names)
STATUS is one of: Todo, Completed, Statement completed, Proof completed.
Metadata rules (automation UpdateLeanMetadata): status Todo -> no \\lean / \\leanok;
otherwise exactly one \\lean{names} right after the label line; \\leanok iff Proof completed.
"""
import re, sys, subprocess
ts = subprocess.check_output(['date', '+%Y-%m-%dT%H:%M:%S%z']).decode().strip()
ts = ts[:-2] + ':' + ts[-2:]
if sys.argv[1] == '--batch':
    jobs = [l.rstrip('\n').split('|') for l in open(sys.argv[2]) if l.strip()]
else:
    jobs = [sys.argv[1:4]]
st = open('automation/Status.md').read().split('\n')
tex = open('blueprint/triangles_in_the_plane_blueprint.tex').read().split('\n')
for label, status, names in jobs:
    assert status in ('Todo', 'Completed', 'Statement completed', 'Proof completed'), status
    names = [n.strip() for n in names.split(',') if n.strip()]
    for k, l in enumerate(st):
        if l.startswith('\\label{%s}:' % label):
            st[k] = f'\\label{{{label}}}: [{status}] (Lean: {", ".join(names)}) ({ts})'
            break
    else:
        sys.exit('label not found in Status: ' + label)
    for k, l in enumerate(tex):
        if '\\label{%s}' % label in l and (l.lstrip().startswith('\\begin') or tex[k-1].lstrip().startswith('\\begin')):
            j = k + 1
            while j < len(tex) and (tex[j].startswith('\\lean{') or tex[j].strip() == '\\leanok'):
                del tex[j]
            ins = []
            if status != 'Todo':
                ins.append('\\lean{%s}' % ','.join(names))
                if status == 'Proof completed':
                    ins.append('\\leanok')
            tex[k+1:k+1] = ins
            break
    else:
        sys.exit('label not found in tex: ' + label)
open('automation/Status.md', 'w').write('\n'.join(st))
open('blueprint/triangles_in_the_plane_blueprint.tex', 'w').write('\n'.join(tex))
print(f'updated {len(jobs)} entries')
