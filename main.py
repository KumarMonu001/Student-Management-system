
empbd = []

flag = True
while flag:
    menu_data = """\n\n\t\tMain Menu
    1 : Insert student details
    2 : Update student details
    3 : Delete student details
    4 : Show all students
    5 : Search students
    5 : Exit
    """
    choice = int(input(menu_data + 'Enter your choice : '))
    
    if choice == 1:
        cl = []
        lst = ['rollno', 'name', 'email', 'semester', 'cgpa']
        for i in lst:
            cl.append(input(f'Enter {i}'))
        empbd.append(cl)
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
    elif choice == 5:
        # for exiting from the loop
        pass
    else:
        print('Enter a valid choice!')