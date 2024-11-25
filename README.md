# **Faculty and Course Management System**
## **Overview**
This project is a simple yet effective Faculty and Course Management System built using Python, leveraging the power of Object-Oriented Programming (OOP). It allows users to manage courses, faculty members, and salary adjustments based on teaching workload.

The system is a command-line application that showcases OOP principles like encapsulation, inheritance, and object interaction. It's perfect for educational settings or administrative tasks, offering a hands-on way to practice and learn Python's OOP features.

## **Features**
### **Course Management:**
Add new courses with details like name, code, and credit hours.
Update existing course information.
Display a list of all available courses.
**Faculty Management:**
Add new faculty members with basic information like name and monthly salary. \
Assign courses to faculty members, tracking their teaching load. \
Automatically adjust the salary if teaching hours exceed 12 credit hours. \
### **Salary Adjustment:**
If a faculty member’s teaching load exceeds 12 credit hours, each additional credit hour adds a bonus to their monthly salary. \
### **File Structure**
Course.py: Contains the Course class to manage individual course details. \
Attributes: Course Name, Course Code, Credit Hour. \
Methods: Get and set course attributes. \
Faculty.py: Contains the Faculty class to manage faculty members. \
Attributes: Name, Monthly Salary, Assigned Courses, Total Credit Hours. \
Methods: Add courses, calculate salary adjustment, get faculty details. \
Main.py: Acts as the main entry point of the program. \
Command-line interface for managing courses and faculty. \
Options to create, update, and display courses and faculty information. 
## **Follow the on-screen instructions to manage courses and faculty:**
Choose options for course management to add, update, or view courses. \
Choose options for faculty management to add members, assign courses, and view details.
### **Example Commands**
### **Adding a New Course**
Enter option 1 for Course Management. \
Select option 1 to add a new course. \
Provide the course name, code, and credit hour when prompted.
### **Assigning a Course to Faculty**
Enter option 2 for Faculty Management. \
Select option 2 to assign a course. \
Provide the course name and faculty member's name to complete the assignment.
### **Future Enhancements**
Implement data persistence using a database or file storage. \
Add a graphical user interface (GUI) for better user experience. \
Implement user authentication for enhanced security. \
Add more detailed reports and statistics on faculty workload.
### **Contributing**
Feel free to open issues or submit pull requests for improvements and bug fixes. Contributions are always welcome!
