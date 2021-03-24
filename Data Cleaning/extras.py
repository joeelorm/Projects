import random
from random import randint
from datetime import datetime, timedelta

tire_sizes = []
for s in range(0, 25760):
    n = random.randint(26, 29)
    tire_sizes.append(n)


min_year=2017
max_year=datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+2
end = start + timedelta(days=365 * years)

for i in range(25760):
    dates_times = start + (end - start) * random.random()