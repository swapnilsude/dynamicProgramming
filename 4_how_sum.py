# time: O(n^m * m)
# space: O(m)

def howSum(targetSum, nums):
    if targetSum == 0:
        return []
    elif targetSum < 0:
        return None
    else:
        for n in nums:
            remainder = targetSum -n
            remainderResult = howSum(remainder, nums)
            if remainderResult != None:
                return [*remainderResult, n]
        return None

print(howSum(7,[2,3]))
# print(howSum(300,[7,14]))