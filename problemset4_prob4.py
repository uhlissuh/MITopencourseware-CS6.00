import math 

def nestEggVariable(salary, save, growthRates):
    yearlyAccountTotalList = []
    firstYear = salary * save * 0.01
    yearlyAccountTotalList.append(firstYear)
    if len(growthRates) > 1:
        for x in range (1, len(growthRates)):
            yearlyAccountTotalList.append(yearlyAccountTotalList[x-1] * (1 + 0.01 *growthRates[x]) +
            salary * save * 0.01)
    return yearlyAccountTotalList


def postRetirement(savings, growthRates, expenses):
    retirementFundYearly = []
    retirementFund = savings

    for x in range (0, len(growthRates)):
        retirementFund = retirementFund * (1 + 0.01 * growthRates[x]) - expenses
        retirementFundYearly.append(retirementFund)

    return retirementFundYearly


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):

    preRetirementList = nestEggVariable(salary, save, preRetireGrowthRates)
    finalYearSavings = preRetirementList.pop()

    low = 0
    high = finalYearSavings
    guess = (low + high) / 2.0
    while True:
        lastYearAlive = postRetirement(finalYearSavings, postRetireGrowthRates, guess).pop()
        if math.fabs(lastYearAlive) < epsilon:
            break
        if lastYearAlive > epsilon:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    return guess



def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    return expenses
    # Output should have a value close to:
    # 1229.95548986

print testFindMaxExpenses()
