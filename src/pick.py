import os
import random

with open('index.db') as f:
    ids = f.read().splitlines()

locals = os.listdir('database')
valid = [id for id in ids if id not in locals]

chosen = random.choice(valid)
print(chosen)
