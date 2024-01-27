num1, num2 = map(int, input().split())
counter = 0

if( num2 >= num1 ):
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                counter = counter + 1
    print("main order - amount:",counter)
else:
    for num in range(num2, num1+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                counter = counter + 1
    print("reverse order - amount:",counter)