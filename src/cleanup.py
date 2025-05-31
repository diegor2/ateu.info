import os
import shutil

files = ['metadata.json', 'subtitles.pt-orig.json3']

databse = 'database'
posts = os.path.join('content', 'posts')

for id in os.listdir(databse):
    data_path = os.path.join(databse, id)
    post_path = os.path.join(posts, id)
    for file in files:            
        file_path = os.path.join(data_path, file)
        if not os.path.exists(file_path):
            print(f'Missing {file_path}, removing {id}')
            shutil.rmtree(data_path, ignore_errors= True)
            shutil.rmtree(post_path, ignore_errors= True)
            break
    thumb_path = os.path.join(post_path, 'thumbnail.webp')
    if not os.path.exists(thumb_path):
        print(f'Missing {thumb_path}, removing {id}')
        shutil.rmtree(data_path, ignore_errors= True)
        shutil.rmtree(post_path, ignore_errors= True)
        