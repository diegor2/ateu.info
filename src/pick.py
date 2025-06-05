import os
import random
import sys

# defaults
skip_existing = True
only_existing = False

if sys.argv[1] == '-n':
    skip_existing = True
elif sys.argv[1] == '-x':
    only_existing = True
elif sys.argv[1] == '-a':
    pass

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
