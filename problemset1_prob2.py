import math

def sumOfLogs(n):
  x = 1
  sumLogs = 0

  for x in range(1, n):
      isPrime = True
      for y in range(2, x):
        if x % y == 0:
          isPrime = False
          break

      if isPrime:
        sumLogs += math.log(x)

      x += 2

  print sumLogs, n, sumLogs/n

sumOfLogs(100)
