
# 11 Modular Reporting System

def sales_report():
    print("Sales Report Generated")

def inventory_report():
    print("Inventory Report Generated")

def employee_report():
    print("Employee Report Generated")

def generate_report(report_name, reports):
    if report_name in reports:
        reports[report_name]()
    else:
        print("Report not available")

reports = {
    "sales": sales_report,
    "inventory": inventory_report,
    "employee": employee_report
}

generate_report("sales", reports)
generate_report("inventory", reports)
generate_report("employee", reports)
generate_report("finance", reports)
