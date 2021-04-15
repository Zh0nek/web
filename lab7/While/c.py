a = int(input())
b = 0
count = 0
while(b<=a and 2**count<=a):
    b = 2**count
    print(b)
    count = count + 1