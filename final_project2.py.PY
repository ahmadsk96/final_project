import uuid
"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Ahmad Skaik
Delivery Date : 21-06-2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)


myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))

class Course:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.course_id = myuuid



    # TODO 3 define static variable indicates total student count

class Student:
    count = 0
    courses = []

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, name, age, number, courses):
        Student.count += 1
        self.name = name
        self.age = age
        self.number = number
        self.student_id = uuid.uuid4()
        self.courses = courses

    # TODO 5 define a method to enroll new course to student courses list

    def enrollcourse(self, name, mark):
        newcourse= Course(name, mark)
        self.courses.append(newcourse)


    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        for x in self.courses:
            print(x.name, x.mark)
           
        # TODO 6 print student courses with their marks


    # method to get student_average as a value
    def get_student_average(self):
            my_sum = 0
            for x in self.courses:
                my_sum += x.mark
            my_avg = my_sum / len(self.courses)
            return my_avg

        # TODO 7 return the student average



# in Global Scope
# TODO 8 declare empty students list
std_list=[]


    # TODO 9 handle Exception for selection input
while True:
    try:
        selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))
        break
    except:
        print("Invalid Value")

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 11 create student object and append it to students list
        student1= Student(student_name,student_age, student_number,[])
        std_list.append(student1)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = int(input("Enter Student Number"))
        # TODO 12 find the target student using loops and delete it if exist ,
        #  if not print ("Student Not Exist")
        student_found = False
        for student in std_list:
            if student.number == student_number:
                std_list.remove(student)
                student_found = True
                break
        if student_found:
            print("Student deleted successfully.")
        else:
            print("Student does not exist.")


    elif selection == 3:
        student_number = int(input("Enter Student Number"))
        # TODO 13 find the target student using loops and print student detials  if exist ,
        #  if not print ("Student Not Exist")
        student_found = False
        for student in std_list:
            if student.number == student_number:
                print("Student Details:")
                print("Name:", student.name)
                print("Student Number:", student.number)
                student_found = True
                break
            if not student_found:
                print("Student does not exist.")

    elif selection == 4:
        student_number = int(input("Enter Student Number"))
        # TODO 14 find the target student using loops and get student average  if exist ,
        #  if not print ("Student Not Exist")
        student_found = False
        for student in std_list:
            if student.number == student_number:
                my_avg = student.get_student_average()
                print("Student Average Grade:", my_avg)
                student_found = True
                break

            if not student_found:
                print("Student does not exist.")


    elif selection == 5:
        student_number = int(input("Enter Student Number"))
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
        student_found = False
        for student in std_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = int(input("Enter Course Mark: "))
                course = Course(course_name, course_mark)
                student.courses.append(course)
                student_found = True
                break
            if student_found:
                print("Course added successfully.")
            else:
                print("Student does not exist.")



    else:
        # TODO 16 call a function to exit the program
        def exit_program():
            print("Exiting the program...")
            exit()


        exit_program()
