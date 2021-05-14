# change the value for different values.
num=7

num=int(input('enter a number:'))
factorial=1

#checking of numbers
if num < 0:
    print('factorial does not exists')
elif num == 0:
    print('factorial of 0 is 1')
else:
    for i in range (1,num+1):
        factorial = factorial*i
    print('the factorial of ',num,'is',factorial)
