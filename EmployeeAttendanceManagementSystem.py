

#5 EmployeeAttendanceManagementSystem

attendance = {}

def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    status = input("Enter attendance (P/A): ").upper()

    if status not in ["P", "A"]:
        print("Invalid status! Use P or A.\n")
        return

    if emp_id not in attendance:
        attendance[emp_id] = []

    attendance[emp_id].append(status)
    print("Attendance marked successfully.\n")

def calculate_working_days(emp_id):
    if emp_id in attendance:
        return attendance[emp_id].count("P")
    else:
        return 0

def generate_report():
    if not attendance:
        print("No attendance records found.\n")
        return

    print("\nAttendance Report")
    print("------------------")
    for emp_id, records in attendance.items():
        total_days = len(records)
        present_days = records.count("P")
        absent_days = records.count("A")

        print(f"Employee ID: {emp_id}")
        print(f"Total Days   : {total_days}")
        print(f"Present Days : {present_days}")
        print(f"Absent Days  : {absent_days}")
        print()

while True:
    print("1. Mark Attendance")
    print("2. Calculate Working Days")
    print("3. Generate Attendance Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        days = calculate_working_days(emp_id)
        print(f"Working Days for {emp_id}: {days}\n")
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("Exiting Attendance System 👋")
        break
    else:
        print("Invalid choice! Try again.\n")
