company = {}
employee_details = {}
dept_details = {}


class Employee:
    def __init__(self, name:str, emp_id:int, title:str, dept:str):
        self.emp_name = name
        self.emp_id = emp_id
        self.emp_title = title
        self.emp_dept = dept
        if self.emp_id not in employee_details:
            employee_details[self.emp_id] = {
                "Name": self.emp_name,
                "Title": self.emp_title,
                "Department": self.emp_dept,
            }
        else:
            print("Id already exist , please use another id")

    @classmethod
    def display_emp_detials(self, emp_id:int):
        print(employee_details[emp_id])

    def __str__(self):
        return {"Employee Name": {self.emp_name}, "Employee ID": {self.emp_id}}


class Department(Employee):
    def __init__(self, dept_name:str):
        self.dept_name = dept_name
        self.employee_list = []

    @classmethod
    def add_emp(self, name:str, emp_id:int, title:str, dept:str):
        new_employee = Employee(name=name, emp_id=emp_id, title=title, dept=dept)
        dept_details[new_employee.emp_dept] = [
            new_employee.emp_title,
            new_employee.emp_name,
            new_employee.emp_id,
        ]
        if emp_id not in employee_details.keys():
            employee_details[emp_id] = [
                new_employee.emp_title,
                new_employee.emp_name,
                new_employee.emp_dept,
            ]
        else:
            ("Duplicate emp_id cannot exists !")
        print(employee_details)
        return {
            "Emp_name": new_employee.emp_name,
            "Emp_id": new_employee.emp_id,
            "Emp_title": new_employee.emp_title,
        }

    @staticmethod
    def remove_emp(emp_id:int):
        if emp_id in employee_details:
            try:
                employee_details.pop(emp_id)
            except Exception as e:
                return f"{e}"
        else:
            return f"No employee was found for id:{emp_id}"

    @classmethod
    def get_all_emp(self):
        return self.employee_list


def add_dept(department :str):
    new_dept = Department(dept_name=department)
    for dept, details in dept_details.items():
        if dept == new_dept.dept_name:
            company[f"{department}"] = details
        else:
            company[f"{department}"] = None
            print("Its a new Department hence no employees are allocated as of now. ")


def remove_dept(dept_name:str):
    if dept_name in company:
        company.pop(dept_name)
    else:
        print(f"Department {dept_name} not found in the company")


def display_dept():
    print(f"{dept_details}")
