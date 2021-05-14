def quantile(L):
     
    q = int(input('Enter the value of n: '))
    n= len(L)
    
    for i in range (0, n-1):
        for j in range (i+1, n):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    print(L)

    partition = n/q
    start = partition - 1  
    i = 1
    print('n-quantiles:')
    while start < n-1:
        position = int(start + 0.5)   #rounded off to the nearest integer
        print(i,' :  ',l[position])
        start = start + partition
        i = i+1
        
     
l = [1,2,2,2,2,3,4,5,5,6,6, 5,5,6, 6,3,3,5]

quantile(l)
