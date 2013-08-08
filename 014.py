#Greg Considine
#Project Euler -- Problem 14

def evenNext(x):
  return x / 2

def oddNext(x):
  return 3 * x + 1

seqCount = 0
maxCount = 0
maxStart = 0
current = 2
startValue = 2
for i in range(1, 1000001):
  
  seqCount = 1
  current = startValue = 2 + i
  while current != 1:
    
    if current % 2 == 0:
      current = evenNext(current)
      seqCount += 1
    else:
      current = oddNext(current)
      seqCount += 1

  if seqCount > maxCount:
    maxCount = seqCount
    maxStart = startValue
  
print("Starting Value -> ", maxStart, " produces largest sequence (", maxCount, ")")

'''
1m19.218s execution time.  A little bit on the slow side, but passable.  This 
was my first exposure to Collatz Sequences.  Pretty weird.
'''
