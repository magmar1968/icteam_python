class Person():
    def __init__(self,_name,_surname,_age):
        self.name = _name
        self.surname = _surname
        self.age = _age


    def print_stats(self):
        print("name:    " + str(self.name))
        print("surname: " + str(self.surname))
        print("age:     " + str(self.age))

class Student(Person): 
    def __init__(self, _name = str, _surname = str, _age = int, _rejected = bool):
        super().__init__(_name, _surname, _age)
        self.rejected = _rejected
    
    def print_stats(self):
        super().print_stats()
        print("rejected:"+ str(self.rejected))

class Super_student(Student):
    def __init__(self, _name = str, _surname = str, _age = int, _rejected = bool, _power = str):
        super().__init__(_name, _surname, _age, _rejected)
        self.power = _power

    def print_stats(self):
        super().print_stats()
        print("power:   " + str(self.power))

class Teacher(Person):
    def __init__(self, _name = str, _surname = str, _age = int, _subject = str):
        super().__init__(_name, _surname, _age)
        self.subject = _subject


    def print_stats(self):
        super().print_stats()
        print("subject: " + str(self.subject))


choice = 0
students = []
super_students = []
teachers = []

print("Every time you must choose the kind of person data")
print("to insert:                                        ")
print("  - s   student                                   ")
print("  - ss  super student                             ")
print("  - t   teacher                                   ")
print("  - q   quit                                      ")

 
while(choice != 'q'):
    choice = input("kind of person:  ")    
    if(choice != 'q'):
        name = input( "name: ")
        surname = input( "surname: ")
        age = input("age: ")

     
    if( choice == 's'):
        rejected = input("has the student have been rejected? (1 yes - 0 no): ")
        students.append(Student(name,surname,age,rejected))

    elif( choice == "ss"):
        rejected = input("has the student have been rejected? (1 yes - 0 no): ")
        power = input("insert the student amazing super power!: ")
        super_students.append(Super_student(name,surname,age,rejected,power))

    elif( choice == 't'):
        subject = input("insert teached subject: ")
        teachers.append(Teacher(name,surname,age,subject))
    

print("\nthe class composition:")
print("list of all student:")
for student in students:
    student.print_stats()

print("list of super students:")
for super_student in super_students:
    super_student.print_stats()

print("list of teachers:")
for teacher in teachers:
    teacher.print_stats()

