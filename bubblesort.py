#bubble sort algo
lis=list(map(int,input().split()))
print("Unsorted list:",lis)
for i in range(len(lis)-1):
    for j in range(len(lis)-1-i):
        if(lis[j]>lis[j+1]):
            lis[j],lis[j+1]=lis[j+1],lis[j]
print("SORTED LIST:",lis)

#Print index of duplicate elements
lis1=list(map(int,input().split()))
list2=[ i for i in range(len(lis1)) if lis1[i]==1]
print(list2)

#Binart search
