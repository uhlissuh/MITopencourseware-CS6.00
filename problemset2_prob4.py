n = 6
biggestNonSolutionOfN = 0
isSolutionCounter = 0
tup = (6, 9, 20)


while True:
    isSolution = False
    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):
                if tup[0] * a + tup[1] * b + tup[2] * c == n:
                    isSolution = True
    if isSolution:
        isSolutionCounter += 1
    else:
        isSolutionCounter = 0
        biggestNonSolutionOfN = n
    if isSolutionCounter == 5:
        print biggestNonSolutionOfN
        break
    n += 1
