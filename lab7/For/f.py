num1 = int(input())
num2 = 0
count = 0
while(num1>0):
    count = num1 % 10
    num1 = num1 // 10
    num2 = num2 * 10 + count
print(num2)