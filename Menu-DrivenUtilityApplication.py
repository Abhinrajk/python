#12 Menu-DrivenUtilityApplication
def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    else:
        print("Invalid choice")

def string_operations():
    s = input("Enter a string: ")
    print("1.Reverse  2.Uppercase  3.Length")
    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Result:", s[::-1])
    elif ch == 2:
        print("Result:", s.upper())
    elif ch == 3:
        print("Result:", len(s))
    else:
        print("Invalid choice")

def number_utilities():
    n = int(input("Enter a number: "))
    print("1.Even/Odd  2.Factorial")
    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Even" if n % 2 == 0 else "Odd")
    elif ch == 2:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial:", fact)
    else:
        print("Invalid choice")

def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1.Calculator")
        print("2.String Operations")
        print("3.Number Utilities")
        print("4.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            calculator()
        elif choice == 2:
            string_operations()
        elif choice == 3:
            number_utilities()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
main_menu()
