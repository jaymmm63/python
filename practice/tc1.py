def myValue(p):
    if len(p)==1:
        return p[0]
    return p[0]* myValue(p[1:]) 
	
myData = [1, 2, 3, 4, 5]
x = myValue(myData)
print(x)
