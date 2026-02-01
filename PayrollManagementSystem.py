
# 7 PayrollManagementSystem

def add_employee(emp_id, name, basic_salary):
    return {
        "Employee ID": emp_id,
        "Name": name,
        "Basic Salary": basic_salary
    }

def calculate_salary(basic_salary, bonus=0, deductions=0):
    net_salary = basic_salary + bonus - deductions
    return net_salary

def apply_bonus_deductions(employee, bonus=0, deductions=0):
    employee["Bonus"] = bonus
    employee["Deductions"] = deductions
    employee["Net Salary"] = calculate_salary(
        employee["Basic Salary"],
        bonus,
        deductions
    )
    return employee

def generate_payroll_report(employee):
    print("\n------ Payroll Report ------")
    print(f"Employee ID   : {employee['Employee ID']}")
    print(f"Name          : {employee['Name']}")
    print(f"Basic Salary  : ₹{employee['Basic Salary']}")
    print(f"Bonus         : ₹{employee.get('Bonus', 0)}")
    print(f"Deductions    : ₹{employee.get('Deductions', 0)}")
    print(f"Net Salary    : ₹{employee['Net Salary']}")
    print("-----------------------------")


emp = add_employee(101, "Abhin Raj", 30000)

emp = apply_bonus_deductions(emp, bonus=5000)

generate_payroll_report(emp)
