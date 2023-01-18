import concurrent
from concurrent.futures import ThreadPoolExecutor
def square(m):
    return m * m
with ThreadPoolExecutor() as executor:
    results = []
    for i in range(10):
        results.append(executor.submit(square, i))
for f in concurrent.futures.as_completed(results):
    print(f.result())