#To reverse a string
n='nkcollege'
r1 =''
r2 =''
s=len(n)
i=0
j= -1
while i < s:
    r1 = r1 + n[s-i-1]
    i=i+1
    j=j+1
    r2 = r2 + n[s-j-1]        
print('String1 is',r1)
print('String2 is',r2)


