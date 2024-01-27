class game:
  def __init__(self):
    self.menu = "log in/sign up menu"
    self.id = []
    self.name = []
    self.type = []
    self.password = []
    self.course_name = []
    self.course_id = []
    self.capacity = [0]*10
    self.total_students = [0]*10
    self.course_id_student = []
    self.index = 0
  def current(self):
    print(self.menu)
  def log_out(self):
      if( self.menu == "student menu" or self.menu == "professor menu" ):
        self.menu = "log in/sign up menu"
        print("logged out successfully!\nentered log in/sign up menu")
      else:
          print("invalid command")
  def sign_up(self, type, id, name, password):
    if( self.menu == "log in/sign up menu" ):
        for i in self.id:
          if( i == id ):
            print("id already exists")
            return
        self.id.append(id)
        self.name.append(name)
        self.type.append(type)
        self.password.append(password)
        self.course_id_student.append([])
        print("signed up successfully!")
    else:
      print("invalid command")
  def log_in(self, id, password):
    if( self.menu == "log in/sign up menu" ):
      if id in self.id:
        if( password == self.password[self.id.index(id)] ):
          print("logged in successfully!")
          self.index = self.id.index(id)
          if( self.type[self.id.index(id)] == "S" ):
            print("entered student menu")
            self.menu = "student menu"
          else:
            self.menu = "professor menu"
            print("entered professor menu")
        else:
          print("incorrect password")
      else:
        print("incorrect id")
    else:
      print("invalid command")
  def show_course_list(self):
    if( self.menu == "student menu" or self.menu == "professor menu" ):
      print("course list:")
      for i in range(len(self.course_id)):
        print(f"{self.course_id[i]} "
              f"{self.course_name[i]} "
              f"{self.total_students[i]}/{self.capacity[i]}")
    else:
      print("invalid command")
  def add_course(self, course_name, course_id, capacity):
    if( self.menu == "professor menu"):
      if course_id in self.course_id:
        print("course id already exists")
      else:
        if( course_id.isdigit() == True ):
          if (capacity.isdigit() == True):
            self.course_id.append(course_id)
            self.capacity.insert(self.course_id.index(course_id), capacity)
            self.course_name.append(course_name)
            print("course added successfully!")
          else:
            print("invalid course capacity")
        else:
          print("invalid course id")
    else:
      print("invalid command")
  def get_course(self, course_id):
    if(self.menu == "student menu" ):
      if course_id in self.course_id:
        if course_id not in self.course_id_student[self.index]:
          if( int(self.capacity[self.course_id.index(course_id)]) > self.total_students[self.course_id.index(course_id)]):
            self.course_id_student[self.index].append(course_id)
            self.total_students[self.course_id.index(course_id)] += 1
            print("course added successfully!")
          elif(int(self.capacity[self.course_id.index(course_id)]) == self.total_students[self.course_id.index(course_id)]):
            print("course is full")
        else:
          print("you already have this course")
      else:
        print("incorrect course id")
    else:
      print("invalid command")

g = game()

while True:
    string_value = input().lstrip().rstrip()

    if( string_value.split()[1] == "exit" ):
        break
    elif( string_value.split()[1] == "current" ):
        if( "edu" and "menu" and "current" ) in string_value:
            counter = 0
            if( string_value.split()[0] == "edu" and string_value.split()[2] == "menu" and string_value.split()[3] == "edu" ):
                for i in range(len(string_value)):
                    if( string_value[i] == " " ):
                        counter += 1
                if( counter == 3 ):
                    g.current()
                else:
                    print("invalid command")
            else:
                print("invalid command")
        else:
            print("invalid command")
    elif( string_value.split()[1] == "sign" ):
        if( "edu" and "sign" and "-i" and "-n" and "-p" ) in string_value:
            string_prime = "*.!@$%^&()"
            counter_prime = 0
            counter = 0
            if( string_value.split()[2] == "up" ):
                if( string_value.split()[3][1::] == "S" or string_value.split()[3][1::] == "P" ):
                    if( string_value.split()[4] == "-i" ):
                        if( string_value.split()[5].isdigit() == True ):
                            if( string_value.split()[6] == "-n" ):
                                if( string_value.split()[8] == "-p" ):
                                    if( len(string_value.split()[9].split()) == 1 and len(string_value.split()[9]) >= 4 ):
                                        for i in string_prime:
                                            if i in string_value.split()[9]:
                                                counter_prime = 1
                                                break
                                        if (counter_prime == 1):
                                            if( string_value.split()[10] == "edu" ):
                                                for i in range(len(string_value)):
                                                    if( string_value[i] == " " ):
                                                        counter += 1
                                                if( counter == 10 ):
                                                    g.sign_up(string_value.split()[3][1::], string_value.split()[5],
                                                              string_value.split()[7], string_value.split()[9])
                                                else:
                                                    print("invalid command")
                                            else:
                                                print("invalid password")
                                        else:
                                            print("invalid password")
                                    else:
                                        print("invalid password")
                                else:
                                    print("invalid name")
                            else:
                                print("invalid id")
                        else:
                            print("invalid id")
                    else:
                        print("invalid type")
                else:
                    print("invalid type")
            else:
                print("invalid command")
        else:
            print("invalid command")
    elif( string_value.split()[1] == "log" ):
        if( string_value.split()[2] == "in" ):
            if( "edu" and "log" and "-i" and "-p" ) in string_value:
                counter = 0
                if( string_value.split()[0] == "edu" ):
                    if( string_value.split()[3] == "-i" ):
                        if( string_value.split()[5] == "-p" ):
                            if( string_value.split()[7] == "edu" ):
                                for i in range(len(string_value)):
                                    if( string_value[i] == " " ):
                                        counter += 1
                                if( counter == 7 ):
                                    g.log_in(string_value.split()[4], string_value.split()[6])
                                else:
                                    print("invalid command")
                            else:
                                print("incorrect password")
                        else:
                            print("incorrect id")
                    else:
                        print("invalid command")
                else:
                    print("invalid command")
            else:
                print("invalid command")
        elif( string_value.split()[2] == "out" ):
            if( "edu" and "log" and "out" ) in string_value:
                counter = 0
                if( string_value.split()[0] == "edu" and string_value.split()[3] == "edu" ):
                    for i in range(len(string_value)):
                        if( string_value[i] == " " ):
                            counter += 1
                    if( counter == 3 ):
                        g.log_out()
                    else:
                        print("invalid command")
            else:
                print("invalid command")
        else:
            print("invalid command")
    elif( string_value.split()[1] == "show" ):
        if( "edu" and "show" and "course" and "list" ) in string_value:
            counter = 0
            if( string_value.split()[0] == "edu" and string_value.split()[2] == "course" and string_value.split()[3] == "list" and string_value.split()[4] == "edu" ):
                for i in range(len(string_value)):
                    if( string_value[i] == " " ):
                        counter += 1
                if( counter == 4 ):
                    g.show_course_list()
                else:
                    print("invalid command")
            else:
                print("invalid command")
        else:
            print("invalid command")
    elif( string_value.split()[1] == "add" ):
        if( "edu" and "course" and "-c" and "-i" and "-n" ) in string_value:
            counter = 0
            if( string_value.split()[0] == "edu" and string_value.split()[2] == "course" and string_value.split()[3] == "-c" ):
                if( string_value.split()[5] == "-i" ):
                    if( string_value.split()[7] == "-n" ):
                        if( string_value.split()[9] == "edu" ):
                            for i in range(len(string_value)):
                                if( string_value[i] == " " ):
                                    counter += 1
                            if( counter == 9 ):
                                g.add_course(string_value.split()[4], string_value.split()[6], string_value.split()[8])
                            else:
                                print("invalid command")
                        else:
                            print("invalid course capacity")
                    else:
                        print("invalid course id")
                else:
                    print("invalid course name")
            else:
                print("invalid command")
        else:
            print("invalid command")
    elif( string_value.split()[1] == "get" ):
        if( "edu" and "course" and "-i" ) in string_value:
            counter = 0
            if( string_value.split()[0] == "edu" and string_value.split()[2] == "course" and string_value.split()[3] == "-i" ):
                if( string_value.split()[5] == "edu" ):
                    for i in range(len(string_value)):
                        if( string_value[i] == " " ):
                            counter += 1
                    if( counter == 5 ):
                        g.get_course(string_value.split()[4])
                    else:
                        print("invalid command")
            else:
                print("invalid command")
        else:
            print("invalid command")
    else:
        print("invalid command")
