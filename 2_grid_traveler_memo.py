## travel m*n grid with only right and down motion
 
def gridTraveler(m,n,memo={}):
    key = f'{m},{n}'
    if key in memo:
        return memo[key]
    elif (m == 1 and n == 1):
        return 1
    elif (m == 0 or n == 0):
        return 0
    else:
        memo[key] = gridTraveler(m,n-1,memo) + gridTraveler(m-1,n,memo)
    return memo[key]

print(gridTraveler(18,18))