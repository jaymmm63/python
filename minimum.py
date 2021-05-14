def smallest(list):
    min=list[0]
    for a in list:
        if a < min:
            min=a
    return min
print(smallest([1,2,-8,0]))
