import json
import sys
import re
import os
from jsonpath_ng import jsonpath, parse

print(sys.argv)

input, output = sys.argv
in_path, in_filename = os.path.split(input)
_, date, title, id, _  = re.search('(.+) - (.+) - (.+).(.+)', in_filename)

print(date, title, id)

with open(input) as fin:
    sub = json.load(fin)

out_filename = os.path.join(output, in_filename.replace('.json3', '.md'))
print(out_filename)

with open(out_filename, 'w') as fout:
    fout.write(f'# {title}\n\n')
    fout.write(f'<iframe src="http://www.youtube.com/embed/{id}"></iframe>\n\n')
    for match in parse('$.events[*].segs').find(sub):
        fout.write(''.join([seg['utf8'] for seg in match.value])) 
