# cook your dish here
x=int(input())
for _ in range(x):
    n=int(input())
    fact=1
    for i in range(1,n):
        fact+=fact*i
    print(fact)
