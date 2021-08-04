x=int(input())
for _ in range(x):
    f=False
    n=int(input())
    if(n==1):
        f=True
    elif(n>1):
        for i in range(2,n):
            if(n%i==0):
                f=True
                break
    if(f==True):
        print("no")
    else:
        print("yes")
    
            
