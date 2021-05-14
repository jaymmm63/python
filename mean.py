def mean(L):
    n= len(L)
    total = 0
    for i in range (0, n):
        total = total + L[i]
    print('Mean = ', total/n)


l = [12,11,23]
mean(l)

