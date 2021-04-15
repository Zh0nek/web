import math 
num = int(input())
count = 0
for i in range(1, int(math.sqrt(num))): 
    if num % i == 0: 
        count = count + 2
print(count+(int(math.sqrt(num))**2==num))