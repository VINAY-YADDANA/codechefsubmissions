ip=int(input())
for k in range(ip):
    s=0
    num=int(input())
    lis=list(map(int,input().split()))
    if(sum(lis)%2==0):
        print(0)
    else:
        for x in range(num):
            if(lis[x]==2):
                s=s+1
                break
        if(s!=0):
            print("1")
        else:
            print("-1")
