class Course:
    def __init__(self,courseName,courseCode,creditHour):
        self.__courseName = courseName
        self.__courseCode = courseCode
        self.__creditHour = creditHour
    def getName(self):
        return self.__courseName
    def getCode(self):
        return self.__courseCode
    def getCredit(self):
        return self.__creditHour
    def setName(self,courseName):
        self.__courseName = courseName
    def setCode(self,courseCode):
        self.__courseCode = courseCode
    def setCredit(self,courseCredid):
        self.__creditHour = courseCredit
    
    def __str__(self):
        return f'Course Name: {self.__courseName}\n Course Code: {self.__courseCode}\n Credit Hour: {self.__creditHour}'

