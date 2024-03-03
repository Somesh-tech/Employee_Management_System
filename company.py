from empployee import *

while True:

    menu_options = """ Please select anyone of the following: 
                1. Add Employee
                2. Remove Employee
                3. Show Employee Details
                4. Add Department
                5. Remove Department
                6. Show All Department Details
                7. Show all the employees
                """
    

    def menu():
        print(menu_options)
        user_input = input("Please provide the option: ")
        return user_input

    choice = menu()

    def add_employee():
        data = input("Provide Employee Name, Employee ID, Employee Title, Department Name: ")
        name, emp_id, title, dept_name = data.split(",")
        dept = Department(dept_name)
        details = dept.add_emp(name=name, emp_id=emp_id, title=title, dept=dept_name)
        print(f"Employee has been added : {details}")
        print(60 * "-")

    def delete_employee():
        data = input("Please provide employee ID : ")
        details = Department.remove_emp(data)
        print(details)
        print(60 * "-")

    def employee_list():
        emp_id = input(str("Provide Employee ID "))
        if emp_id in employee_details.keys():
            print(employee_details[emp_id])
        else:
            print(f"No Employee with id :{emp_id}")
        print(60 * "-")

    def new_dept():
        name = input("Please provide the Department Name: ")
        try:
            add_dept(name)
            print(f" Department {name} successfully added !")
        except Exception as e:
            print(f"{e}")
        print(60 * "-")

    def delete_dept():
        name = input("Please provide the Department Name: ")
        try:
            remove_dept(name)
            
        except Exception as e:
            print(f"{e}")
        print(60 * "-")

    def all_dept():
        print(dept_details)
        print(60 * "-")

    def all_emp():
        print(employee_details)
        print(60 * "-")

    if (choice) == "1":
        add_employee()
    if (choice) == "2":
        delete_employee()
    if (choice) == "3":
        employee_list()
    if (choice) == "4":
        new_dept()
    if (choice) == "5":
        delete_dept()
    if (choice) == "6":
        print(display_dept())
    if (choice) == "7":
        print(employee_details)
