list=[]
for i in range (1,11):
  n=int(input('enter a number:'))
 lst.append(n)
 L=len(list)
   for i in range(0,L):
       for j in range (0,i):
           if list[i]<list[j]:
            temp=list[i]
          list[i]=list[j]
          list[j]=temp
    print(list)
           
