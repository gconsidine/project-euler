#Greg Considine
#Project Euler -- Problem 3

num = 600851475143
i = num
j = 2
largestPrimeFactor = 0

while j <= num / 2:
  
  if num % j == 0:
    i = num / j
    
  if num % i == 0 and (i % 2 != 0 or i == 2) and i != num:
    k = 2

    while k <= i: 
      if k != i and i % k == 0:
        break
      else:
        if k >= i / 2:
          largestPrimeFactor = i
          break
        
        k += 1

  if largestPrimeFactor != 0:
    break
  
  j += 1
  
print(largestPrimeFactor)

'''
My first attempt to solve this problem was sort of brute force, I had lists
involved and iterated through an entire large number, one smaller number at
a time searching for factors.  Once I found a factor, I would search through
it one number at a time to check if it was divisible by any number other than
itself and 1 (i.e. prime).

This worked fine for smaller numbers, but was definitely not cutting it for
finding the largest prime factor of a 12 digit number.

I optimized in the following ways:

-Removed lists entirely (they served no purpose)

-Rather than incrementing through the large number, i.e. finding the smallest
 factors first, I reversed the loop, decrementing and breaking as soon as the
 first prime factor is found.

-Stopped plus-one incrementation and instead divided the number in question 
 with by an incrementing value (e.g. 600851 / 2 -> 600851 / 3 -> 600851 / 4)
 after first confirming the remainder of the division operation would 
 equal zero.  I incremented starting at 2 and ignored anything greater
 than 1/2 the number in question since it would be impossible to have 
 a factor larger than 1/2 the number other than the number itself.

-Adjusted the inner loop so that it doesn't increment higher than 1/2 of 
 the potential prime factor.  Anything above 1/2 of the value can be
 discared for the same reasons as above.

-Ignore even factors (other than two) when found right away since there are
 no even prime numbers other than 2.

Interesting to note than an 11 digit number takes hardly any time at all, but
the 12 digit number took roughly an hour.  That could just be because the 
largest prime factor of 600851475143 is relatively small.

'''
