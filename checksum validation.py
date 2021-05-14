# Program to evaluate LUHN checksum Validation
# Input identification number num


num = input('Enter the identification number: ')

sum = 0              # Sum of digits is sum
numLength = len(num) # Number of digits in num

if numLength%2 == 0:  # Case1: Code for even-digit number
    for i in range(0, numLength):
        digit = int(num[i])
        if i%2 == 1:
            #print('Digit: ', digit)  
            sum = sum + digit
        else:
            doubleDigit = digit * 2
            if doubleDigit > 9:
                leftDigit = str(doubleDigit)[0]
                rightDigit = str(doubleDigit)[1]
                sumIntermediate = int(leftDigit) + int(rightDigit)
                sum = sum + sumIntermediate
                #print('Double Digit: ', digit, ' and Sum: ', sumIntermediate)
            else:
                sum = sum + doubleDigit
                #print('Double Digit: ', doubleDigit)

else:                # Case2: Code for odd-digit number
    for i in range(0, numLength):
        digit = int(num[i])
        if i%2 == 0:
            #print('Digit: ', digit)  
            sum = sum + digit
        else:
            doubleDigit = digit * 2
            if doubleDigit > 9:
                leftDigit = str(doubleDigit)[0]
                rightDigit = str(doubleDigit)[1]
                sumIntermediate = int(leftDigit) + int(rightDigit)
                sum = sum + sumIntermediate
                #print('Double Digit: ', digit, ' and Sum: ', sumIntermediate)
            else:
                sum = sum + doubleDigit
                #print('Double Digit: ', doubleDigit)
    
#print('Sum of the digits of ',num,' is ', sum)
if sum%10 == 0:
    print('Valid Identification Number')
else:
    print('Invalid Identification Number')






    



    
    

    

