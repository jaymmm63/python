def mode(L):
    n= len(L)
    freq = []
    element = []
    for i in range (0, n):
        if L[i] in element:
            ind = element.index(L[i])
            freq[ind] = freq[ind]+1
        else:
            element.append(L[i])
            freq.append(1)
    maxFreq = 0
    for i in range (0, len(element)):
        if freq[i] > maxFreq:
            maxFreq = freq[i]
            location = i
    print('Mode = ', element[location])
    
l = [1,2,2,2,2,3,4,5,5,6,6, 5,5,6, 6,3,3]
mode(l)
