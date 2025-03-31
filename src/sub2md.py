import json
import os
import re
import shutil
import sys
from jsonpath_ng import jsonpath, parse
from string import Template

_, input, output = sys.argv


template = Template('''
---
date: '$date'
title: '$title'
---

[Video](https://www.youtube.com/watch?v=$id)

![capa]($img)
''')

for id in os.listdir('database'):
    path = os.path.join(input, id)
    map = {file.split('.')[0]:file for file in os.listdir(path)}

    with open(os.path.join(path, map['metadata'])) as f:
        metadata = json.load(f)

    with open(os.path.join(path, map['subtitles'])) as f:
        subtitles = json.load(f)

    out = os.path.join(output, id)
    markdown = os.path.join(out, 'index.md')
    header = template.substitute(
        {
            'date': re.sub(r'(....)(..)(..)', r'\1-\2-\3', metadata['upload_date']),
            'title': metadata['title'],
            'img': map['thumbnail'],
            'id': id,
        }
    )

    if not os.path.exists(out):
        os.makedirs(out)

    shutil.copy(os.path.join(path, map['thumbnail']), out)

    with open(markdown, 'w') as f:
        f.write(header)
        for match in parse('$.events[*].segs').find(subtitles):
            f.write(''.join([seg['utf8'] for seg in match.value])) 
