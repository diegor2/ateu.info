import json
import os
import sys
from jsonpath_ng import jsonpath, parse

print(sys.argv)

_, input, output = sys.argv

for (in_path, _, in_filenames) in os.walk(input):
    for in_filename in in_filenames:
        root, ext = os.path.splitext(in_filename)
        id = root.split('.')[0]
        if('json' not in ext): continue

        date, title = in_path.split('/')[-2:].replace('_', ' ')
        with open(os.path.join(in_path, in_filename)) as fin:
            sub = json.load(fin)

        out_filename = os.path.join(output, id + '.md')
        img_filename = id + '.webp'

        header = f'# {title}\n\n'
        f'[![{title}]({img_filename})](https://www.youtube.com/watch?v={id})'

        with open(out_filename, 'w') as f:
            f.write(header)
            for match in parse('$.events[*].segs').find(sub):
                f.write(''.join([seg['utf8'] for seg in match.value])) 

