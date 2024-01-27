a = int(input())
b = int(input())

counter1 = 0
x = a ^ b
x = x << 1

while True:
    x = x >> 1
    if( x > 2 ):
        if( x%2 == 1 ):
            counter1 += 1
        else:
            pass
    else:
        break

print(counter1 + 1)
