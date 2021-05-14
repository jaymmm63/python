nterms=10

#first two terms
n1=0
n2=1
count=2

#check if the number of terms is valid or not
if nterms<= 0:
    print('please enter a positive integar')

elif nterms==1:
        print('fibonacci sequence upto',nterms,':')
        print(n1)

else:
        print('fibonacci sequence upto',nterms,':')
        print(n1,',',n2,end=',')

        while count<nterms:
            nth=n1+n2
            print(nth,end=',')



            #updated values:
            n1=n2
            n2=nth
            count=count+1
