for _ in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i*arr[i] - (n-1-i) * arr[i]
    print(sum)
    
or
result,i=0,0
while(i<len(arr)):
    result=i*arr[i]-(len(arr)-i-1)*arr[i]
    i+=1
