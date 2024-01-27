number_value = int(input())

example_list =[]
listt = []
copy_list = []
s = []
A = ""
j = 0

while True:
    a = input()

    if( a == "END"):
        break
    else:
        example_list.append(a)
for i in range(0,len(example_list),1):
    A += str(example_list[i])
s = A.split("B")
for m in range(1, number_value + 1, 1):
    listt.append(".")
for m in range(0, example_list.count("B") + 1, 1):
    copy_list.append(listt)
for i in range(0,len(s),1):
    copy_list[i] = ["."]*number_value
    copy_list[i][j] = "*"
    for k in s[i]:
        if( k == "L" ):
            if( j == 0 ):
                pass
            else:
                j -= 1
                copy_list[i][j] = "*"
        else:
            if( j == number_value - 1 ):
                pass
            else:
                j += 1
            copy_list[i][j] = "*"
    copy_list[i][j] = "*"
if( j != number_value -1 ):
    for i in range(0,example_list.count("B")+1,1):
        for j in range(0,number_value,1):
            print(copy_list[i][j],end=" ")
        print()
    print("There's no way out!")
elif( copy_list[example_list.count("B")][number_value-1] == "."):
    for i in range(0,example_list.count("B")+1,1):
        for j in range(0,number_value,1):
            print(copy_list[i][j],end=" ")
        print()
    print("There's no way out!")
else:
    for i in range(0,example_list.count("B")+1,1):
        for j in range(0,number_value,1):
            print(copy_list[i][j],end=" ")
        print()
