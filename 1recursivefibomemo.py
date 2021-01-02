def fib(n,memo = {}):

    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

print(fib(50))


def fibhelp(n):
    memo = {0:0,1:1}
    def helper(n):
        if n not in memo:
            memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    return helper(n)

print(fibhelp(50))