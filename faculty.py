from first import Course

class Faculty:
    def __init__(self,Name,monthly_salary):
        self.__name = Name
        self.__monthly_salary = monthly_salary
        self.__courses = []
        self.__creditHour = 0

    def add_course(self,course):
        self.__courses.append(course)
        self.__creditHour += course.getCredit()
        if self.__creditHour >=12:
            additional_credit = self.__creditHour - 12
            self.__monthly_salary = self.__monthly_salary + (additional_credit * 2800)
    def getName(self):
        return self.__name
    def __str__(self):
        return f'Instructor Name: {self.__name}\n Salary:  {self.__monthly_salary}\n Earned CreditHour: {self.__creditHour}'

