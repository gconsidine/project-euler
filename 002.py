#Greg Considine
#Project Euler -- Problem 2

fib = [1,1,2]
i = 2
evenFibSum = 2

while fib[i] < 4000000:
  fib.append(fib[i] + fib[i-1])
  i += 1
  
  if fib[i] % 2 == 0:
    evenFibSum += fib[i]

print(evenFibSum)
