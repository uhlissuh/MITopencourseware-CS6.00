def subStringMatchExact(target, key):
    index = 0
    resultTuple = ()
    if len(key) == 0:
        return resultTuple
    while True:
        result = target.find(key, index)
        if result != -1:
            resultTuple = resultTuple + (result,)
            index = result +len(key)
        else:
            break
    return resultTuple



def constrainedMatchPair(firstMatch, secondMatch, length):
    resultTuple = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                resultTuple = resultTuple + (n,)
    return resultTuple



def subStringMatchOneSub(target, key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # print ""
        # print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        # print 'match1',match1
        # print 'match2',match2
        # print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers



def subStringMatchExactlyOneSub(target,key):
    subOnlyTuple = ()
    allAnswers = subStringMatchOneSub(target, key)
    exact = subStringMatchExact(target, key)
    for x in exact:
        for y in allAnswers:
            if y != x:
                subOnlyTuple = subOnlyTuple + (y,)
    return subOnlyTuple


print subStringMatchExactlyOneSub("alissa is better than alyssa", "alissa")
