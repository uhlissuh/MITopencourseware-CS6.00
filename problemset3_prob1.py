from string import *

def countSubStringMatch(target, key):
    index = 0
    counter = 0
    while True:
        result = target.find(key, index)
        if result != -1:
            counter += 1
            index = result + len(key)
        else:
             break
    return counter

print countSubStringMatch("lovelovelovelove", "love")

def countSubStringMatchRecursive(target, key):
    if target.find(key) != -1:
        result = target.find(key);
        smallerString = target[result + len(key):len(target)]
        return 1 + countSubStringMatchRecursive(smallerString, key)
    else:
        return 0
print countSubStringMatchRecursive("love you love you   ", "love")
