def postRetirement(savings, growthRates, expenses):
    retirementFundYearly = []
    retirementFund = savings

    for x in range (0, len(growthRates)):
        retirementFund = retirementFund * (1 + 0.01 * growthRates[x]) - expenses
        retirementFundYearly.append(retirementFund)

    return retirementFundYearly


def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    return savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

print testPostRetirement()
