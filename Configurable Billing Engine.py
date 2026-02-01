
# 10 Configurable Billing Engine
def generate_bill(amount, tax_function):
    tax = tax_function(amount)
    total = amount + tax
    return {
        "Base Amount": amount,
        "Tax": tax,
        "Total Amount": total
    }
def tax_region_a(amount):
    return amount * 0.10

def tax_region_b(amount):
    return (amount * 0.05) + 50

def tax_region_c(amount):
    return amount * 0.18

def display_bill(bill, region_name):
    print(f"\n----- Bill Summary ({region_name}) -----")
    print(f"Base Amount : ₹{bill['Base Amount']}")
    print(f"Tax         : ₹{bill['Tax']:.2f}")
    print(f"Total       : ₹{bill['Total Amount']:.2f}")
    print("-----------------------------------")

amount = 1000

bill_a = generate_bill(amount, tax_region_a)
display_bill(bill_a, "Region A")

bill_b = generate_bill(amount, tax_region_b)
display_bill(bill_b, "Region B")

bill_c = generate_bill(amount, tax_region_c)
display_bill(bill_c, "Region C")
