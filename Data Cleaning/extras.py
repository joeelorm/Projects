import random
from random import randint

tire_sizes = []
for s in range(0, 25760):
    n = random.randint(26, 29)
    tire_sizes.append(n)