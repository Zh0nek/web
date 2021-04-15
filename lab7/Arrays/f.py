# number of elements
n = int(input())
answer = 0
# Below line read inputs from user using map() function
a = list(map(int,input().strip().split()))[:n]
for i in range(n-2, 0, -1):
    if(a[i]>a[i-1] and a[i]>a[i+1]):
        answer = answer + 1
print(answer)