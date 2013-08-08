#Greg Considine
#Project Euler -- Problem 12

import math

# Returns the number of divisors for any given number (triangular numbers in
# this case).
def getDivisorCount(n):
  
  divCount = 1
  i = 2
  while i <= math.sqrt(n):
    
    if n % i == 0:
      divCount += 1

    i += 1

  return divCount * 2

# Exhuastively search through positive integers searching for the first 
# triangular number to have over 500 divisors.
tNum = 3
divCount = 0
i = 2
while True:
  
  tNum += (i+1)
 
  if tNum % 2 == 0:
    divCount = getDivisorCount(tNum)
    print("Triangular Number: ", tNum, " Divisor Count: ", divCount)
  
  if divCount > 500:
    print(tNum)
    break
 
  i += 1

'''
I was stumped on this one for quite a while until I read an interesting tidbit
about the count of divisors of a given number.  It's only necessary to count
the divisors less than or equal to the square root of a number.  If you double
that, you get the total count of divisors for the number.  Very useful
considering we're not interested in WHAT the divisors are, only how many
there are.  

Implementing this idea drastically reduced the execution time to
a mere 9.140s compared to the tens of minutes the brute-force method was 
taking before I force-quit.
'''
