#Greg Considine
#Project Euler -- Problem 5

divisor = 2
dividend = 20
found = False

while True:
  
  while divisor <= 20:
    
    if dividend % divisor == 0:
      if divisor == 20:
        found = True
        print(dividend)
      else:
        divisor += 1
    else:
      break
    
    if found == True:
      break
    
  if found == True:
    break
  else:
    dividend += 20
    divisor = 2

'''
First attempt was painfully slow, so I optimized in the following ways:

-Since all numbers are divisible by 1, I set the divisor starting value equal
 to 2.

-In order for the dividend to have a divisor of 20 without remainder,
 then the dividend must be some multiple of 20 -- so I incremented 
 the dividend by 20 at the end of the outer loop.
'''
