#These two problems are correct, but nonideal implementations. For problem 3
#I started using a more elegant solution.
#So.. look at that problem for a more elegant approach if you want!

def nestEggFixed(salary, save, growthRate, years):
    yearlyAccountTotalList = []
    firstYear = salary * save * 0.01
    yearlyAccountTotalList.append(firstYear)
    if years > 1:
        for x in range (0, years - 1):
            yearlyAccountTotalList.append(yearlyAccountTotalList[x] * (1 + 0.01 *growthRate) +
            salary * save * 0.01)
    return yearlyAccountTotalList

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    return savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]


def nestEggVariable(salary, save, growthRates):
    yearlyAccountTotalList = []
    firstYear = salary * save * 0.01
    yearlyAccountTotalList.append(firstYear)
    if len(growthRates) > 1:
        for x in range (1, len(growthRates)):
            yearlyAccountTotalList.append(yearlyAccountTotalList[x-1] * (1 + 0.01 *growthRates[x]) +
            salary * save * 0.01)
    return yearlyAccountTotalList



def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

print testNestEggVariable()
