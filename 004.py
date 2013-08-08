#Greg Considine
#Project Euler -- Problem 4

x = 999
y = 999
found = False

while x > 900:
  while y > 900: 
    xy = x * y
    
    strA = str(xy)[:3]
    strB = str(xy)[3:]
    strBRev = strB[::-1]

    if strA == strBRev:
      print(x, ' * ', y, ' = ', strA, strB)
      found = True
      break
    
    y -= 1

  if found == True:
    break

  x -= 1
  y = 999

'''
My first approach to this problem was to methodically multiply 3-digit 
values larger than 900 (e.g. 999x999, 999x998, ..., 999x900, 998x999, 998x998, 
..., 998x900) and break at the first sign of a numerical palindrome. It seemed
likely to me that a palindromic number would appear early and there wouldn't be 
any need to search beyond that -- which ended up being true.
'''
