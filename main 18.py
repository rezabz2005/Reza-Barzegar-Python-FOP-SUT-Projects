def length(string_one, string_two):
    counter = 0
    if( len(string_one) > len(string_two) ):
        string_two += "_" * (len(string_one) - len(string_two))
    elif( len(string_two) > len(string_one) ):
        string_one += "_" * (len(string_two) - len(string_one))
    for value1, value2 in zip(string_one, string_two):
        if( value1 != value2 ):
            counter += 1
    return counter
def words(number,string_one, string_two):
    string_one = string_one.replace(".","").replace("،","").replace(":","").split()
    for i in string_one:
        if( length(i, string_two) <= number ):
            print(i)
number_value = int(input())
string_one = input()
string_two = input()
words(number_value, string_one, string_two)
