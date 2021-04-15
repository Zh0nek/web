a = int(input())
c = 10
count = 0
while(a>0):
    count = count + a % 10  
    a = a // 10
print(count) 