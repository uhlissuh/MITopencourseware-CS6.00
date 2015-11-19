def subStringMatchExact(target, key):
    index = 0
    resultTuple = ()
    print "key is", key
    if len(key) == 0:
        print "hi"
        return resultTuple
    while True:
        result = target.find(key, index)
        if result != -1:
            resultTuple = resultTuple + (result,)
            index = result +len(key)
        else:
            break
    return resultTuple
