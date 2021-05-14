#python program to check if the input number is prime or not
# num=

#take input from user
num=int(input('enter a number:'))

#prime number are greater than :
if num>1:
    #check for factors
    for i in range (2,num):
        if (num%i)==0:
            print(num,'is not a prime number')
        else:
            print(num,'is a prime number')
