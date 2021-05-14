def maximum(list):
    max=list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(maximum([1,2,7,-4,0]))
