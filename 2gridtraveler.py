## travel m*n grid with only right and down motion

def gridTraveler(m,n):
    if (m == 1 and n == 1):
        return 1
    elif (m == 0 or n == 0):
        return 0
    else:
        return gridTraveler(m,n-1) + gridTraveler(m-1,n)

print(gridTraveler(2,3))