def IsAscending(a,b):    #Function to check the increasing or desreasing order
    if a < b:
        ascending = 1         #in ascending order
    elif a > b:
        ascending = -1        #not in ascending order
    else:
        ascending = 0         #not sure whether in ascending order or not
    return ascending

def IsSorted(L):             #Function to check whether the list is sorted
    n = len(L)
    previous = L[0]
    current = L[1]
    
    ascending = IsAscending(previous, current)

    for i in range (2, n):
        previous = current
        current = L[i]
        if ascending == 1:                 #previous element is smaller than current element
            if previous <= current:    #ascending order is maintained
                continue
            else:
                return 0                          #descending order is not maintained; not sorted
        elif ascending == -1:              #previous element is greater than current element
            if previous >= current:
                continue                          #descending order is maintained
            else:
                return 0                           #descending order is not maintained; not sorted
        else:
            ascending = IsAscending(previous, current)   
                                       #not sure whether in ascending order or not; elements are equal 
    return 1          #list is sorted

l = [1,2,2,2,2,3,4,5,5,6,6, 5,5,6, 6,3,3,5]
result = IsSorted(l)
print(l)
if result == 0:
    print('Given list is not a sorted list')
else:
    print('Given list is a sorted list')

l.sort()
result = IsSorted(l)
print(l)
if result == 0:
    print('Given list is not a sorted list')
else:
    print('Given list is a sorted list')
