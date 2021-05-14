k=4
rows=10
for i in range (0,rows+1):
    for space in range (1,(rows-i)+1):
        print(end='')
    while k!=(2*i-1):
        print('*',end='')
        k=k+1
    k=4
    print()
