#Greg Considine
#Project Euler -- Problem 6

import math

sumOfSquares = 0
sumSquared = 0
sum = 0

for i in range(1,101):
  sumOfSquares += math.pow(i, 2)
  sum += i

sumSquared = math.pow(sum, 2)

print(sumSquared - sumOfSquares)

'''
This problem was pretty simple.  I went with my first instinct and there wasn't
any need to optimize.
'''
