def xor(x, y):
    if (x == 0 and y == 1) or (y == 0 and x == 1):
        return 1
    return 0
 
 
a, b = map(int, input().split())
print(xor(a, b))