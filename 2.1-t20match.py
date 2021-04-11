# cook your dish here
(x,y,z)=map(int,input().split(' '))
r=20-y
r1=r*6*6
r2=r1+z
#print(x,r2)
if(x>=r2):
    print("NO")
else:
    print("YES")
