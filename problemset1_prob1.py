
x = 1
counter = 0

while True:
    isPrime = True
    for y in range(2, x):
        if x % y == 0:
            isPrime = False
            break

    if isPrime:
        counter += 1


    if counter == 1000:
        print x
        break

    x += 2
