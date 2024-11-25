from first import Course
from faculty import Faculty

def main():
    courses = []
    Faculties = []
    while True:
        inp = input("""
        1) Enter (1) For Course Related
        2) Enter (2) For Faculty Related
        3) Enter (0) For Exit
        """)
        
        # For Course Related Information
        if inp == '1':
            while True:
                course_inp = input("""
                1) For Adding Course 
                2) For Course Information
                3) For Updating Course Name
                4) For Updating Course Code
                5) For Updating Course Credit
                0) Return to Main Menu
                """)
                if course_inp == '1':
                    name = input('Enter Course Name: ')
                    code = input('Enter Course Code: ')
                    credit = int(input('Enter Course Credit: '))
                    cr = Course(name, code, credit)
                    courses.append(cr)
                elif course_inp == '2':
                    for course in courses:
                        print(course)
                        print('-'*10)
                elif course_inp == '3':
                    name = input('Enter Course Name: ')
                    temp = False
                    for course in courses:
                        if course.getName() == name:
                            new_name = input('Enter New Name: ')
                            course.setName(new_name)
                            print('Change Successfully')
                            temp = True
                            break
                    if not temp:
                        print('Course Not Found')
                elif course_inp == '4':
                    name = input('Enter Course Name: ')
                    temp = False
                    for course in courses:
                        if course.getName() == name:
                            new_code = input('Enter New Code: ')
                            course.setCode(new_code)
                            print('Change Successfully')
                            temp = True
                            break
                    if not temp:
                        print('Course Not Found')
                elif course_inp == '5':
                    name = input('Enter Course Name: ')
                    temp = False
                    for course in courses:
                        if course.getName() == name:
                            new_credit = int(input('Enter New Credit: '))
                            course.setCredit(new_credit)
                            print('Change Successfully')
                            temp = True
                            break
                    if not temp:
                        print('Course Not Found')
                elif course_inp == '0':
                    break

        # For Faculty Information 
        elif inp == '2':
            while True:
                faculty_inp = input("""
                1) For Adding New Member (Name And Salary is necessary info)
                2) For Adding Course 
                3) For Information of Faculty
                0) To return to Main menu
                """)
                
                if faculty_inp == '1':
                    name = input('Name of Faculty Member: ')
                    salary = int(input('Member Salary: '))
                    f = Faculty(name, salary)
                    Faculties.append(f)
                    print('Added Successfully')
                
                elif faculty_inp == '2':
                    course_name = input('Enter Course Name You want to add: ')
                    course_found = False
                    for course in courses:
                        if course.getName() == course_name:
                            course_found = True
                            faculty_name = input('Enter Name of Faculty Member: ')
                            faculty_found = False
                            
                            for faculty in Faculties:
                                if faculty.getName() == faculty_name:  
                                    faculty.add_course(course)
                                    print('Course added successfully to the faculty member.')
                                    faculty_found = True
                                    break
                            
                            # If the faculty member is not found
                            if not faculty_found:
                                print('Faculty Member not found. Please add the member first if necessary.')
                            
                            break
                    
                    if not course_found:
                        print('Course Not Found')
                
                elif faculty_inp == '3':
                    for faculty in Faculties:
                        print(faculty)
                
                elif faculty_inp == '0':
                    break

        if inp == '0':
            break

main()
