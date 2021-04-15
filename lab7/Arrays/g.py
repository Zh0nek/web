# number of elements
n = int(input())
# Below line read inputs from user using map() function
a = list(map(int,input().strip().split()))[:n]
for i in range(n-1, -1, -1):
    print(a[i])