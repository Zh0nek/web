a = int(input())
b = 0
count = 0
while(count <= a):
    if(2**count == a):
        print("YES")
        break
    count = count + 1
if(count > a):
    print("NO")