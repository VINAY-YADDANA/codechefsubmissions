for _ in range(int(input())):
    x=input()
    if(x[::-1]==x[::]):
        print("wins")
    else:
        print("loses")
 or
 
for _ in range(int(input())):
    x=int(input())
    rem,s,t=0,0,x
    while(x>0):
        rem=x%10
        s=s*10+rem
        x=x//10
    if(t==s):
        print("wins")
    else:
        print("loses")
        
