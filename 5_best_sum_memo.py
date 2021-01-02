def bestSum(targetSum, nums, memo={}):
    
    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    shortCombination = None
    for n in nums:
        remainder = targetSum -n
        remainderResult = bestSum(remainder, nums)
        if remainderResult != None:
            combination = [*remainderResult, n]
            if shortCombination == None or len(combination) < len(shortCombination):
                shortCombination = combination
    memo[targetSum] = shortCombination
    return memo[targetSum]

print(bestSum(7,[5,3,4,7]))