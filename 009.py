#Greg Considine
#Project Euler -- Problem 9

import math

def coprime(x,y):
  min = x if x < y else y
  
  for i in range(2, math.ceil(math.sqrt(min)) + 1):
    if x % i == 0 and y % i == 0:
      return False

  return True

def odd(x):
  if x % 2 == 0:
    return False
  else:
    return True

def pythagorean(x,y,z):
  if (math.pow(x,2) + math.pow(y,2)) == math.pow(z,2):
    return True
  else:
    return False

m = 2
n = 1
a = b = c = 0
total = 0
found = False

while found == False:
  
  while n < 100 and found == False:
    if coprime(m,n) and odd(m-n):
      a = (math.pow(m,2) - math.pow(n,2))
      b = 2 * m * n
      c = (math.pow(m,2) + math.pow(n,2))

      if pythagorean(a,b,c):
        total = a + b + c

        if total == 1000:
          found = True
          print(a * b * c)
           
        n += 1

    else:
      n += 1
  
  m += 1
  n = 1

'''
This was probably the most challenging problem yet and my solution isn't very
elegant.  I had to read up on Pythagorean triples and coprime numbers.  I used
Euclid's formula to generate pythagorean triples with incrementing values of
m and n.  I was going to manually increase the limits of n if no solution
was found -- not exactly a one-size-fits-all algorithm but it works.
'''
