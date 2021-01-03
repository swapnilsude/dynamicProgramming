def allConstruct(target, wordBank, memo = {}):
    
    if target in memo:
        return memo[target]

    if (target == ''):
        return [[]]

    result = []

    for word in wordBank:
        if target[: len(word)] == word:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = [[word] + way for way in suffixWays]
            if targetWays:
                result.extend(targetWays)
    
    memo[target] =result
    return result


print(allConstruct('purple',['purp','p','ur','le','purpl']))