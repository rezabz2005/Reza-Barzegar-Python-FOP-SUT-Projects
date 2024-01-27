def pascal(number_value):
    a = [[] for i in range(0,number_value,1)]
    for i in range(0,number_value,1):
        for j in range(0,i+1,1):
            if( j < i ):
                if( j == 0 ):
                    a[i].append(1)
                else:
                    a[i].append( a[i-1][j-1] + a[i-1][j] )
            elif( j == i ):
                a[i].append(1)
    return a

number_value = int(input())

for i in range(0,number_value,1):
    for j in range(0,i+1,1):
        print(pascal(number_value)[i][j],end=" ")

    print()
