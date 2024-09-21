import json
import sys
import re
from jsonpath_ng import jsonpath, parse

in_filename = sys.argv[1]
id = re.search(' - (.+)\.', in_filename)[1]
title = re.search(' - (.+) - ', in_filename)[1]

with open(in_filename) as fin:
    sub = json.load(fin)

out_filename = in_filename.replace('.json3', '.md')
print(out_filename)
with open(out_filename, 'w') as fout:
    fout.write(f'# {title}\n\n')
    fout.write(f'<iframe src="http://www.youtube.com/embed/{id}"></iframe>\n\n')
    for match in parse('$.events[*].segs').find(sub):
        fout.write(''.join([seg['utf8'] for seg in match.value])) 
