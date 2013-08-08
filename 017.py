#Greg Considine
#Project Euler -- Problem 17

onesAndTeens = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens = {0: "", 1: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

j = 0
numString = ""
charCount = 0
for i in range(1,1000):
  
  if i < 20:
    numString += onesAndTeens[i]
  elif i < 100:
    i = str(i)
    tKey = int(i[0:1])
    oKey = int(i[1:])
    numString += tens[tKey] + onesAndTeens[oKey]
  elif i < 1000:
    i = str(i)
    hKey = int(i[0:1])
    tKey = int(i[1:2])
    oKey = int(i[2:])

    if tKey == 0 and oKey == 0:
      numString += onesAndTeens[hKey] + "hundred"
    elif tKey < 2:
      numString += onesAndTeens[hKey] + "hundredand" + onesAndTeens[int(str(tKey)+str(oKey))]
    else:
      numString += onesAndTeens[hKey] + "hundredand" + tens[tKey] + onesAndTeens[oKey]

numString += "onethousand"

print(len(numString))

'''
I wasted a good 10 - 15 minutes on this problem because I spelled "forty as
"fourty" -- I've committed the vim commands ":set spell" and ":set nospell"
to memory and I'll be sure to remember to ACTUALLY USE IT when working with
string data in the future.
'''
