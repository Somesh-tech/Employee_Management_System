from empployee import *

def menu():
    user_input = input(
        """ Please select anyone of the following: 
            1. Add Employee
            2. Remove Employee
            3. Show Employee Details
            4. Add Department
            5. Remove Department
            6. Show All Department Details
            7. Show all the employees
        """)
    return user_input
input = menu()

if int(input) == 1 :
    name, emp_id, title = input(str("Provide Employee Name, Employee ID, Employee Title  (Note: provide comma seperated values) ").split(","))
    add = Department.add_employee(name=name, emp_id=emp_id, title=title)

if int(input) == 2 :
    name, emp_id, title = input(str("Provide Employee Name"))
    add = Department.remove_emp(emp_name=name)

if int(input) == 3 :
    emp_id = input(str("Provide Employee ID "))
    add = Employee.display_emp_detials(emp_id=emp_id)

if int(input) == 4 :
    dept_name, dept_id = input(str("Provide Department Name, Department ID (Note: provide comma seperated values) ").split(","))
    add = add_dept(dept_name=dept_name, dept_id=dept_id)

if int(input) == 5:
    name = input(str("Provide Department Name" ))
    add = remove_dept(dept_name = name)

if int(input) == 6 :
    print(display_dept())

if int(input) == 7:
    print(Department.get_all_emp())
