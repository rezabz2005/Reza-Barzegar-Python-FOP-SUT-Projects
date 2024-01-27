value_right = int(input())
value_left = int(input())

n = int(input())

a = []

#input_numbers

for i in range(0,n,1):
    a.append(None)
for i in range(0,n,1):
    a[i] = int(input())

#creating_binary_for_values

value_left = value_left << 32
new_value = value_left + value_right

#checking

for i in range(0,n,1):
    if( (new_value >> a[i]) % 2 != 0 ):
        print("yes")
    else:
        print("no")
