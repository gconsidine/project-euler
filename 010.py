#Greg Considine
#Project Euler -- Problem 10

import math

def isPrime(x):
  
  i = 2
  while i <= math.ceil(math.sqrt(x)):
    if x % i == 0:
      return False
    else:
      i += 1

  return True

i = 3
sum = 2
prime = 3

while i < 2000000:
  if isPrime(i):
    prime = i
    sum += prime
  i += 2

print(sum)

'''
The solution isn't as optimized as it could be (it takes about 30 seconds to 
find the sum of primes < 2000000), but it's adequate.  If it took much longer
I would have given more consideration to optimization.
'''

