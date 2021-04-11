ip=int(input())
for lms in range(0,ip):
    nums=[]
    n,s=list(map(int,input().split()))
    for iiitk in range(0,n):
        nums.append(tuple(map(int,input().split())))
    nums.sort(key = lambda x: x[1])
    for value in nums[::-1]:
        if value[0]>s:
            continue
        else:
            print(value[1])
            break
