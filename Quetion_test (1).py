class crab:
    def __init__(self):
        self.string = ""
    def change(self, string_copy):
        self.string = ""
        self.string += string_copy + string_copy[0:10:]
        self.string = self.string.replace("tt","o")
        return self.string
class sponge(crab):
    example_list = []
    def __init__(self,string):
        super().__init__()
        self.string = string
        self.string = self.change(self.string)
        for key, value in enumerate(str(len(self.string))):
            self.example_list.append(value)
        self.string = ""
        def mergeSort(myList):
            if len(myList) > 1:
                mid = len(myList) // 2
                left = myList[:mid]
                right = myList[mid:]

                mergeSort(left)
                mergeSort(right)

                i = 0
                j = 0

                k = 0

                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        myList[k] = left[i]

                        i += 1
                    else:
                        myList[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    myList[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    myList[k] = right[j]
                    j += 1
                    k += 1
            return myList
        for i in range(len(mergeSort(self.example_list))):
            self.string += str(mergeSort(self.example_list)[i])
    def get_item(self):
        return self.string
class squid:
    example_list = []
    def __init__(self):
        self.string = ""
    def change(self, string_copy):
        self.string = string_copy
        for key, value in enumerate(string_copy):
            self.example_list.append(value)
            if( value == "x" ):
                self.string += str(key)
                break
        for i in range(2,len(self.example_list),1):
            if( self.example_list[i-2] == self.example_list[i-1] == self.example_list[i] ):
                self.string = self.string.replace(self.example_list[i-2]+
                                                  self.example_list[i-1]+
                                                  self.example_list[i],"(0_0)")
        return self.string
c = crab()
sq = squid()
string_value = input()
string_prime = string_value[::-1]
if( string_value[0:1:] == "m" or string_value[0:2:] == "sb" or string_value[0:1:] == "s" ):
    if( string_value[0:1:] == "m" ):
        print(c.change(string_value))
    elif(string_value[0:2:] == "sb"):
        sp = sponge(string_value)
        print(sp.get_item())
    elif( string_value[0:1:] == "s" ):
        print(sq.change(string_value))
elif( string_prime[0:1:] == "m" or string_prime[0:2:] == "sb" or string_prime[0:1:] == "s" ):
    if( string_prime[0:1:] == "m" ):
        print(c.change(string_prime))
    elif(string_prime[0:2:] == "sb"):
        sp = sponge(string_prime)
        print(sp.get_item())
    elif( string_prime[0:1:] == "s" ):
        print(sq.change(string_prime))
else:
    print("invalid input")