

#1	EmployeeSalaryCalculator System


def employee_details():
    name = input("Enter employee name: ")
    id = input("Enter employee ID: ")
    basic = float(input("Enter basic salary: "))
    return name, id, basic
def gross(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    gross_salary = basic + hra + da
    return gross_salary
def deductions(gross_salary):
    deduction_amount = 0.08 * gross_salary
    return deduction_amount
def display_final_salary(name, id, basic, gross_salary, deduction_amount):
    net_salary = gross_salary - deduction_amount
    print("\n------ Salary Details ------")
    print("Name       :", name)
    print("Employee ID:", id)
    print("Basic Pay  :", basic)
    print("Gross Pay  :", gross_salary)
    print("Deductions :", deduction_amount)
    print("Net Salary :", net_salary)
    print("----------------------------")

name,id,basic = employee_details()
gross_salary = gross(basic)
deduction_amount = deductions(gross_salary)
display_final_salary(name, id, basic, gross_salary, deduction_amount)
