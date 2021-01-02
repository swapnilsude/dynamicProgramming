def canSum(targetSum, nums):
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    
    for i in nums:
        remainder = targetSum - i
        if canSum(remainder, nums) == True:
            return True

    return False

print(canSum(7,[2,3]))
print(canSum(300,[7,14]))