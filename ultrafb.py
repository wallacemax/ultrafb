import numpy as np
from numba import vectorize
import numba as nb
import time

@vectorize(nopython=True)
def fizzbuzz(val):
    if val % 15 == 0:
        return -3
    elif val % 3 == 0:
        return -2
    elif val % 5 == 0:
        return -1
    else:
        return val    

f = 10000000

start = time.time_ns()
fizzbuzz(nb.arange(f))
elapsed = time.time_ns() - start
print(f"run time for {f} items is {elapsed//10E6} ms")
print(f"run time for {f} items is {elapsed} ns")

#raw
#64.9MiB 0:00:20 [3.11MiB/s] [                                          <=>                                                               ]

#drop to integers
#53.5MiB 0:00:27 [1.92MiB/s] [                                                        <=>                                                 ]

#drop to integers w vectorize
#53.5MiB 0:00:37 [1.42MiB/s] [                                                                           <=>                              ]

#jit, but no parallel
#53.5MiB 0:00:15 [3.48MiB/s] [                               <=>                                                                          ]


