import time
import math

def is_prime(n):
    #Return true if n is a prime number, false otherwise
    if n == 1:
        return False #1 is not prime
    max_divisor = math.floor(math.sqrt(n))
    for divisior in range(2,1 + max_divisor):
        if n % divisior == 0:
            return False # n is not prime
    return True

# ===== Test Function =====
t0 = time.time()
for n in range(1,100000):
    print(n, is_prime(n))
t1 = time.time()
print("Time required: ", t1 - t0)

# ===== Time Function =====
#t0 = time.time()
#for n in range(1, 100000):
    #is_prime(n)
#t1 = time.time()
#print("Time required: ", t1 - t0)
