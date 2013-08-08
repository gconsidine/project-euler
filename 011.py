#Greg Considine
#Project Euler -- Problem 11

#The given 20 x 20 grid of 2-digit numbers -- 400 values.
grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

#The numbers are loaded into a single list
numCount = 0
nums = []
i = 0
while numCount < 400:
  
  nums.append(int(grid[i:i+3]))
  numCount += 1
  i += 3

#The list is broken down to 20 number rows, and each row is added to the new list
rows = []
for i in range(0, 20):
  rows.append(nums[i*20:(i*20) + 20])

#Find horizontal max
horMax = 0
for row in rows:
  
  i = 0
  while i < len(row) - 3:
    temp = row[i] * row[i+1] * row[i+2] * row[i+3]
    
    if temp > horMax:
      horMax = temp
    
    i += 1

#Find vertical max
verMax = 0
for i in range(0,20):
  
  j = 0
  while j < 17:
    temp = nums[(j*20) + i] * nums[((j+1)*20) + i] * nums[((j+2)*20) + i] * nums[((j+3)*20) + i]
    
    if temp > verMax:
      verMax = temp
    
    j += 1

#Find diagonal (left to right) max
diaLeftMax = 0
for i in range(0,17):

  j = 0
  while j < 17:
    temp = nums[(i*20) + j] * nums[((i+1)*20) + j+1] * nums[((i+2)*20) + j+2] * nums[((i+3)*20) + j+3]

    if temp > diaLeftMax:
      diaLeftMax = temp
  
    j += 1

#Find diagonal (right to left) max
diaRightMax = 0
for i in range(0,17):
  
  j = 20
  while j > 3:
    temp = nums[(i*20) + j-1] * nums[((i+1)*20) + j-2] * nums[((i+2)*20) + j-3] * nums[((i+3)*20) + j-4]
    
    if temp > diaRightMax:
      diaRightMax = temp

    j -= 1

#Find largest max value
maxes = [horMax, verMax, diaLeftMax, diaRightMax]

print(max(maxes))

'''
This problem was a little bit hard to wrap my head around in the beginning.  I
created two seperate lists: one gigantic list of all 400 values in sequential
order, and a list of lists containing rows of 20 values (effectively recreating
the grid).  It seemed easiest to knock out the horizontal and vertical
possibilities, so that's what I started with first.  I originally attempted to
knock out all diagonal possibilities in a single algorithm, but realized
that was needlessly complex.  

I first dealt with left-to-right diagonals, then right-to-left diagonals 
seperately. After a max was found for each horizontal, vertical,
left-to-right diagnoals, and right-to-left diagonals.  I found the max
value of those values which yielded the correct answer.

I was hung up for maybe 5-10 minutes because I was adding values in the
right-to-left diagonal algorithm instead of multiplying and I didn't 
see it.  I guess that's what I get for writing sloppyish code this go
around.
'''
