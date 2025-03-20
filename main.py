# insert student data into the list
def insert():
    global empdb
    global lst
    cl = []
    for i in lst:
        cl.append(input(f'Enter {i} '))
    empdb.append(cl)

def update(studentIndex):
    pass

def delete(studentIndex):
    pass

def show_one_student(studentIndex):
    global lst
    global empdb
    for attribute in range(0, 5):
            print(f"{lst[attribute].capitalize()}\t  : {empdb[studentIndex][attribute].capitalize()}")


def show_all_student():
    pass

def search(rollno) -> int:
    global empdb
    index = -1
    for student in empdb:
        if student[0] == rollno:
            index = empdb.index(student)
            return index
    return index

# empdb -> contains the data of the each student
empdb = []
# lst -> list contains all the essential attributes of the student
lst = ['name', 'rollno','semester', 'cgpa', 'email']

flag = True
while flag:
    menu_data = """\n\n\t\tMain Menu
    1 : Insert student details
    2 : Update student details
    3 : Delete student details
    4 : Show all students
    5 : Search students
    6 : Exit
    """
    choice = int(input(menu_data + 'Enter your choice : '))
    
    if choice == 1:
        # Insert parts
        insert()
        print(empdb)
    elif choice == 2:
        # Update parts
        pass
    elif choice == 3:
        # delete part here
        pass
    elif choice == 4:
        # showing part here
        pass
    elif choice == 5:
        # searching part here
        pass
    elif choice == 6:
        # for exiting from the loop
        stdRoll = input('Enter student roll no. : ')
        find = search(stdRoll)
        if stdRoll != -1:
            show_one_student(find)
        else:
            print(f"Student with roll no. {stdRoll} doesn't exist!")
    else:
        print('Enter a valid choice!')