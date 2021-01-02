# time: O(n * m^2)
# space: O(m^2)

def howSum(targetSum, nums, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    elif targetSum == 0:
        return []
    elif targetSum < 0:
        return None
    else:
        for n in nums:
            remainder = targetSum -n
            remainderResult = howSum(remainder, nums)
            if remainderResult != None:
                memo[targetSum] = [*remainderResult, n]
                return memo[targetSum]
        
        memo[targetSum] = None
        return None

print(howSum(7,[2,3]))
print(howSum(300,[7,14]))