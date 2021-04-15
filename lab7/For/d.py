a = int(input())
b = int(input())
c = 10
count = 0
while(a>0):
    if(a % 10 == b):
        count = count + 1
    c = c* 10 
    a = a // 10 
print(count) 