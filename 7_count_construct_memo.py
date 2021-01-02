def canConstruct(target, wordBank, memo={}):

    if target in memo:
        return memo[target]

    if target == '':
        return 1

    total = 0

    for word in wordBank:
        if target[: len(word)] == word:
            numWays = canConstruct(target[len(word):], wordBank, memo)
            total += numWays
    memo[target] = total
    return total

print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef',
['e','eee','eeee','ee','eeeee']))