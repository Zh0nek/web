# number of elements
n = int(input())
# Below line read inputs from user using map() function
a = list(map(int,input().strip().split()))[:n]
for i in a: 
    if(i%2 == 0):
        print(i)