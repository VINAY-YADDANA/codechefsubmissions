r=int(input())
#l=list(map(int,input().split()))[:n]
c=int(input())
#f=False
m=[]
for i in range(r):
    a=[]
    for j in range(c):
        v=int(input())
        a.append(v)
    m.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
        
