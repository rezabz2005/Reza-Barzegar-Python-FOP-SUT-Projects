counter_example = 0
def trans(num, base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base

    base_num = base_num[::-1]
    return base_num
result = None

while True:
    n, b = map(int, input().split())
    counter = 1

    if( n != -1 and b != -1):
        if( not( b <= 9 and b >= 2 )):
            result = "invalid base!"
            print("invalid base!")
            break
        else:
            for i in range(2,n+1,1):
                if( n%i == 0 ):
                    counter += i
                else:
                    pass
            counter_example += int(trans(counter, b))
    else:
        break

if( result == "invalid base!"):
    pass
else:
    print(counter_example)