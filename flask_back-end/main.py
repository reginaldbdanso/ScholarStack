#!/bin/bash/python3
""" Student class module """
from management import SRMS
from student import Student

if __name__ == '__main__':
    srms = SRMS()
    running = True
    while running:
        print('''
        1. Add Student
        2. Update Student
        3. Delete Student
        4. Get Student
        5. Get All Students
        6. Exit
        ''')
        choice = input('Enter your choice:')
        if choice == '1':
            firstname = input('Enter firstname:')
            lastname = input('Enter lastname:')
            age = (input('Enter age:'))
            if age.isnumeric():
                age = int(age)
            else:
                age = 0 
            gender = input('Enter gender:')
            program = input('Enter program:')
            s = Student(firstname=firstname, lastname=lastname, age=age, gender=gender, program=program)
            srms.add_student(s)
            print(f'{s.get_fullname()} added to database successfully')

        elif choice == '2':
            id = input('Enter id:')
            if id == '':
                print('Id cannot be empty')
                continue
            firstname = input('Enter firstname:')
            lastname = input('Enter lastname:')
            age = (input('Enter age:'))
            if age.isnumeric():
                age = int(age)
            else:
                age = 0 
            gender = input('Enter gender:')
            program = input('Enter program:')
            obj = {}
            if len(firstname) > 0:
                obj['firstname'] = firstname
            if len(lastname) > 0:
                obj['lastname'] = lastname
            if age > 0:
                obj['age'] = age
            if len(gender) > 0:
                obj['gender'] = gender
            if len(program) > 0:
                obj['program'] = program
            srms.update_student(id, **obj)
            print(f'{id}\'s record updated successfully')

        elif choice == '3':
            id = input('Enter id:')
            if id == '':
                print('Id cannot be empty')
                continue
            srms.delete_student_by_id(id)
            print(f'{id}\'s record deleted successfully')

        elif choice == '4':
            if len(srms.get_students()) == 0:
                print('No records found')
                continue
            id = input('Enter id:')
            if id == '':
                print('Id cannot be empty')
                continue
            print(srms.get_student_by_id(id))

        elif choice == '5':
            if len(srms.get_students()) == 0:
                print('No records found')
                continue
            print(srms.get_students())

        elif choice == '6':
            srms.save()
            print('Exiting...')
            running = False
