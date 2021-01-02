def canSum(targetSum, nums, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    elif targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    
    for i in nums:
        remainder = targetSum - i
        if canSum(remainder, nums) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

print(canSum(7,[2,3]))
print(canSum(300,[7,14]))