l=[100,50,10,5,2,1]
for _ in range(int(input())):
    n=int(input())
    res=0
    for i in range(len(l)):
        res+=n//l[i]
        n%=l[i]
        if(n==0):
            break
    print(res)
