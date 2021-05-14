#Program Decode
#Reading an integer with multiple digits
#Each integer (comma separated) is code

def read_code():
    num = input('Enter the message: ')
    L = len(num)                    # Length of input string
    codeWord = []                   #To maintain a list of individual integers 
    #print(L)
    code = 0                        # Individual integer or code word
    for position in range(0,L):
        N = num[position]
        if N == ' ':                # ignore spaces, if any
            continue
        elif N == ',':              # Comma denotes end of the integer
            #print(code)
            codeWord.append(code)   # Add the code to the list codeWord
            code = 0                # Initialize individual integer 
        else:
            code = code*10 + int(N) # Each digit is added to the code
        if position == L-1:   
            #print(code)
            codeWord.append(code)   # Add the code to the list codeWord
        
    print(codeWord)
    return(codeWord)


def codeMsg(value, mode):
    punctuation = ['!', '?', ',','.', ' ', ';', '"', '\'']
    if mode == 0:
        message = chr(64+value)
    elif mode == 1:
        message = chr(96+value)
    else:
        message = punctuation[value - 1]
    return message

def decode(codeWord): 
    codeLength = len(codeWord)          # Number of code words or integers
    codeMode = 0                        # 0:Uppercase, 1:lowercase, 2:punctuation             

    message = []
    for i in range(0, codeLength):
        if codeMode == 0 or codeMode == 1:
            value = codeWord[i] % 27
        else:
            value = codeWord[i] % 9
        if value > 0:
            msg = codeMsg(value, codeMode)
            message.append(msg)
        else:
            codeMode = (codeMode + 1)% 3
    return(message)
                
#Program: Function calls 

codeWord = read_code()
message = decode(codeWord)
print(message)
