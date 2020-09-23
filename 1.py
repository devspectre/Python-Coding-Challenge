import sys
import time
from concurrent.futures import ThreadPoolExecutor

# sample input for f() and g()
# def f(num=None):
#         time.sleep(10)
#         return 123
# def g(num=None):
#         time.sleep(10)
#         return 345

input_string = ''
for line in sys.stdin:
    if 'q' == line.strip():
        break
    input_string += line
    
exec(input_string)

executor = ThreadPoolExecutor(max_workers=2)
f_ = executor.submit(f)
g_ = executor.submit(g)

print(max(f_.result(), g_.result()))