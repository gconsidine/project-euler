#Greg Considine
#Project Euler -- Problem 15

def factorial(x):
  if x == 1:
    return x
  else:
    return x * factorial(x-1)

def choose(x, y):
  return factorial(x)/(factorial(x-y) * factorial(y))

gridWidth = 20
print(choose(gridWidth * 2, gridWidth))

'''
I knew how to solve this problem right away because I've been doing similar 
stuff in a math class.  I used a calculator to get the answer (40C20), but I
figured I'd implement factorial and choose functions anyway to continue the 
tradition of solving the problems with Python.
'''
