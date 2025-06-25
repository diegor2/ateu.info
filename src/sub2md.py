import json
import os
import re
import sys
from jsonpath_ng import jsonpath, parse
from string import Template

template_header = '''
---
date: "$date"
title: > 
    $title
featured_image: "$img"
---
'''
template_video = '{{< video src="video" >}}'
template_youtube = '{{< youtube $id >}}'

databse = 'database'
content = 'content'
posts = 'posts'
output = os.path.join(content, posts)

for id in os.listdir(databse):
    print(id)
    out = os.path.join(output, id)
    vid = os.path.join(out,'video.mp4')
    if os.path.exists(vid):
        template = Template(template_header + template_video)
    else:
        template = Template(template_header + template_youtube)

    path = os.path.join(databse, id)
    map = {file.split('.')[0]:file for file in os.listdir(path)}

    meta_path = os.path.join(path, map['metadata']) if 'metadata' in map else None
    if meta_path and os.path.exists(meta_path):
        with open(meta_path) as f:
            metadata = json.load(f)
    else:
        print("Missing metadata, skipping")
        continue

    sub_path = os.path.join(path, map['subtitles']) if 'subtitles' in map else None
    if sub_path and os.path.exists(meta_path):
        with open(sub_path) as f:
            subtitles = json.load(f)
    else:
        print("Missing subtitles, skipping")
        continue

    markdown = os.path.join(out, 'index.md')
    header = template.substitute(
        {
            'date': re.sub(r'(....)(..)(..)', r'\1-\2-\3', metadata['upload_date']),
            'title': metadata['title'],
            'img': 'thumbnail.webp',
            'id': id,
        }
    )

    if not os.path.exists(out):
        os.makedirs(out)

    with open(markdown, 'w') as f:
        f.write(header)
        for match in parse('$.events[*].segs').find(subtitles):
            f.write(''.join([seg['utf8'] for seg in match.value])) 
