import json
import sys
import re
import os
from jsonpath_ng import jsonpath, parse

in_path, in_filename = os.path.split(sys.argv[1])
out_dir = os.path.split(sys.argv[2])
_, date, title, id, _  = re.search('(.+) - (.+) - (.+).(.+)', in_filename)

print(date, title, id)

with open(os.path.join(in_path, in_filename)) as fin:
    sub = json.load(fin)

out_filename = os.path.join(out_dir, in_filename.replace('.json3', '.md'))
print(out_filename)

with open(out_filename, 'w') as fout:
    fout.write(f'# {title}\n\n')
    fout.write(f'<iframe src="http://www.youtube.com/embed/{id}"></iframe>\n\n')
    for match in parse('$.events[*].segs').find(sub):
        fout.write(''.join([seg['utf8'] for seg in match.value])) 
