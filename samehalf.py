#PGM to find same half
x=input()
l=len(x)
s,ss=0,0
mid=l//2
print(mid)
if(x[:mid]==x[mid:]):
    print(x[:mid],x[mid:])
    print("YEs")
else:
    print("No")
for i in range(len(x)//2):
    s+=int(x[i])
for j in range(len(x)//2,len(x)):
    ss+=int(x[j])
print(s,ss)
if(s==ss):
    print("yes")
    print(s,ss)
else:
    print("no")
    
