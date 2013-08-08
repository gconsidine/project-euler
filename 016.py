#Greg Considine
#Project Euler -- Problem 16

import math

value = '{0:d}'.format(int(math.pow(2,1000)))

sum = 0
for digit in value:
  sum += int(digit)

print(sum)

'''
Python can handle large numbers, so calculating 2^1000 wasn't an issue, but
supressing scientific notation was.  I needed the result of 2^1000 to be 
stored longhand so I could use a for-in loop to sum 1 digit at a time
of the total value 2^1000.  I had to read up a bit on the newer 'advanced
string formatting' to make that happen.
'''
