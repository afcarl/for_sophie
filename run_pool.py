from multiprocessing import Pool
from pool_example import mult

pool = Pool(8)
listing = list(range(100))

results = pool.map(mult, listing)
print(results)
