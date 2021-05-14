#python to check if the input number is odd or even
#a number is even if the division by 2 give a remainder of 0
#if remaindder is 1 ,it is odd number 
num=int(input('enter a digit:'))
if (num%2)==0:
    print('{0}is even'.format(num))
else:
    print('{0}is odd'.format(num))
