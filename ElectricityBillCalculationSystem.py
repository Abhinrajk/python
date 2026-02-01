
# 6 Electricity Bill Calculation System

def input_units():
    units = int(input("Enter units consumed: "))
    return units

def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

    return bill

def generate_bill_summary(units, bill):
    print("\n----- Electricity Bill Summary -----")
    print(f"Units Consumed : {units}")
    print(f"Total Bill     : ₹{bill:.2f}")
    print("-----------------------------------")

units_consumed = input_units()
total_bill = calculate_bill(units_consumed)
generate_bill_summary(units_consumed, total_bill)
