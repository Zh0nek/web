# number of elements
n = int(input())
count = 0
# Below line read inputs from user using map() function
a = list(map(int,input().strip().split()))[:n]
for i in a: 
    if(i > 0):
       count = count + 1
print(count) 