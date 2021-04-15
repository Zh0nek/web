a = int(input())
summa = 0
pow_2 = 1
b = 0
while(a>0):
    b = a % 10
    summa = summa + b*pow_2
    pow_2 = pow_2*2
    a = a // 10
print(summa)