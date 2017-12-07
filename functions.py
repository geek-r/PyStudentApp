students =[]


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    for i in students_titlecase:
        print(i)



def add_student(name, student_id=1):
    student = {'name': name, 'student_id': student_id}
    students.append(student)



def save_file(student):
    try:
        f = open("students.txt",'a')
        f.write(student + "\n")
        f.close()
    except:
        print('Could Not save the file')


def read_file():
    try:
        f = open("students.txt",'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except:
        print("Could Not Read the file")



# def variable_args(name, **kwargs): #**kwargs denotes the variabel arguments with dictionary form
#     print(name)
#     print(kwargs["description"],kwargs["feedback"])


read_file()
print_student_titlecase()
ch = raw_input("Do you want to add students?")
while(ch == 'Y' or ch == 'y'):

    student_name = raw_input("Enter Student name: ")
    student_id = raw_input("Enter student id: ")
    add_student(student_name, student_id)
    save_file(student_name)
    read_file()
    print_student_titlecase()
    ch = raw_input("Do you want to add students(Y/N)?")
