# time : O(n^m *m)
# space : O(m^2)
def canConstruct(target, wordBank):

    if target == '':
        return True
    for word in wordBank:
        if target[: len(word)] == word:
            if canConstruct(target[len(word):], wordBank):
                return True
    return False

print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef',
['e','eee','eeee','ee','eeeee']))