
company={}
employee_details={}

class Employee:
    def __init__(self, name, emp_id, title, dept):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.dept = dept
        employee_details[self.emp_id] = {"Name": self.name, "Title":self.title, "Department": self.dept}

    @classmethod
    def display_emp_detials(self, emp_id):
        print(employee_details[emp_id])    

    def __str__(self):
        return {"Employee Name": {self.name}, 
                "Employee ID": {self.emp_id}}

class Department(Employee):
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employee_list = []

    @classmethod    
    def add_emp(self, name, emp_id, title):
        new_employee = super().__init__(name, emp_id, title, self.dept_name)
        self.employee_list.append(new_employee)
        
    @classmethod
    def remove_emp(self, emp_name):
        for emp_name in self.employee_list:
            try:
                self.employee_list.remove(emp_name)   
            except ValueError as e:
                return (f"No employee was found for id:{emp_name}")
            
    @classmethod
    def get_all_emp(self):
        return self.employee_list
    
def add_dept(department,dept_id):
    company[f"{department}"] = Department(dept_name = department, dept_id = dept_id)

def remove_dept(dept_name):
    if dept_name in company:
        company.pop(dept_name)
    else:
        print(f"Department {dept_name} not found in the company")

def display_dept(company):
    for department_name in company.keys():
        print(department_name, end=" ")
