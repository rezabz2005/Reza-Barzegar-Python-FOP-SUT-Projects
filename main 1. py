def value(n, m):
    while m != 0:
        other_value = n & m
        n = n ^ m
        m = other_value << 1

    return (n)

n = int(input())
m = int(input())
k = int(input())

if( value(n, m) == k ):
    print(k)
    print("YES")
else:
    print(value(n, m))
    print("NO")


