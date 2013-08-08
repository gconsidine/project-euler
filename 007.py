#Greg Considine
#Project Euler -- Problem 7

import math

def primeCheck(n):
  
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      return False
    else:
      i += 1
  
  return True


primeCount = 1
lastPrime = 2
i = 3

while primeCount < 10001:
  
  if primeCheck(i) == True:
    primeCount += 1
    lastPrime = i
  
  i += 2

print(lastPrime)
print(primeCount)

'''
After refering to the wikipedia article on prime numbers, I learned a better
way to exhaustively check if a number is prime.  It's only necessary to check
if a number N is isn't evenly divisible by numbers 2 through sqrt(N).  If it
is, then it's not a prime.  Also, beyond the number 2, all numbers in the
sequence of primes are odd.  Knowing this, I started at 3 and incremented by
2 at the end of each loop.

I also used functions for the first time so far and I feel it's made the code
a lot more readable (and faster?).  I'm already cringing a bit at how I handled 
some of the earlier PE problems I did the other day.
'''


