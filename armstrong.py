#Armstrong numbers between a range
x=int(input())
for i in range(x):
    num=i
    res=0
    n=len(str(i))
    while(i!=0):
        d=i%10
        res+=d**n
        i=i//10
    if(res==num):
        print(num)
     
