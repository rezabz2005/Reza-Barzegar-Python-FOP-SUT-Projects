mode_input = input()

if( mode_input != "sum" and mode_input != "average" and mode_input != "lcd" and mode_input != "gcd" and mode_input != "min" and mode_input != "max"):
    print("Invalid command")
else:
    example_list = []

    def lcd(x, y):
        mox = 1
        moy = 1
        while( x*mox != y*moy ):
            if( x*mox < y*moy ):
                mox += 1
            else:
                moy += 1
        result = x*mox

        return result
    def gcd(x, y):
        while(y):
            x, y = y, x%y
        return x

    while True:
        a = input()
        if( a == "end" ):
            break
        else:
            example_list.append(a)

    for i in range(0,len(example_list),1):
        example_list[i] = int(example_list[i])

    if( mode_input == "sum" ):
        counter = 0
        for i in range(0,len(example_list),1):
            counter += example_list[i]
        print(counter)
    elif( mode_input == "average" ):
        counter = 0
        for i in range(0,len(example_list),1):
            counter += example_list[i]
        average = counter/len(example_list)
        average = float(average)
        average = round(average, 2)
        print(average)
    elif( mode_input == "lcd" ):
        num1 = example_list[0]
        num2 = example_list[1]
        lcd1 = lcd(num1,num2)

        for i in range(2,len(example_list),1):
            lcd1 = lcd(lcd1, example_list[i])
        print(lcd1)
    elif( mode_input == "gcd" ):
        num1 = example_list[0]
        num2 = example_list[1]
        gcd1 = gcd(num1, num2)

        for i in range(2,len(example_list),1):
            gcd1 = gcd(gcd1, example_list[i])
        print(gcd1)
    elif( mode_input == "min" ):
        print(min(example_list))
    elif( mode_input == "max" ):
        print(max(example_list))