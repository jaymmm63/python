#for example of a recursive formula to
#find the factorial of number

def calc_factorial(x):
    if x==1:
        return 1
    return(x*calc_factorial(x-1))
num=5
print('the factorial of',num,'is',calc_factorial(num))
