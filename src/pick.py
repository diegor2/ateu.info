import os
import random
import sys

skip_existing = False
only_existing = False

if len(sys.argv) > 1:
    if sys.argv[1] == '-n':
        skip_existing = True
    elif sys.argv[1] == '-x':
        only_existing = True
    elif sys.argv[1] == '-a':
        pass
else:
    skip_existing = True # default to -n

with open('index.db') as f:
    ids = f.read().splitlines()
locals = os.listdir('database')

if skip_existing:
    valid = [id for id in ids if id not in locals]
elif only_existing:
    valid = locals
else:
    valid = ids

chosen = random.choice(valid)
print(chosen)
