# time : O(n *m^2)
# space : O(m^2)

def canConstruct(target, wordBank, memo={}):

    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in wordBank:
        if target[: len(word)] == word:
            if canConstruct(target[len(word):], wordBank, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False

print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef',
['e','eee','eeee','ee','eeeee']))