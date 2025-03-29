import json
import sys
import re
import os
from jsonpath_ng import jsonpath, parse

print(sys.argv)

_, input, output = sys.argv

for (in_path, _, in_filenames) in os.walk(input):
    for in_filename in in_filenames:
        root, ext = os.path.splitext(in_filename)
        id = root.split('.')[0]
        if('json' not in ext): continue

        date, title = in_path.split('/')[-2:]
        print(date, title, id)

        with open(os.path.join(in_path, in_filename)) as fin:
            sub = json.load(fin)

        output_path = os.path.join(output, date, title.replace('_', ' '))
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        out_filename = os.path.join(output_path, id + '.md')
        print(out_filename)

        with open(out_filename, 'w') as fout:
            fout.write(f'# {title}\n\n')
            fout.write(f'<iframe width="560" height="315" src="http://www.youtube.com/embed/{id}" ' +
                    'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; ' +
                    'clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" ' +
                    'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n\n')
            for match in parse('$.events[*].segs').find(sub):
                fout.write(''.join([seg['utf8'] for seg in match.value])) 

