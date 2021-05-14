def median(L):
    n= len(L)
    
    for i in range (0, n-1):
        for j in range (i+1, n):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    print(L)
    if n%2 == 0:
        middle1 = n/2
        middle2 = middle1 - 1
        med = (L[middle1] + L[middle2])//2
    else:
        med = L[(n+1)//2]
    print('Median = ', med)
l = [1,5,7,6,8]
median(l)
