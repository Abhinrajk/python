

#3 SimpleBankingApplication

balance = 0.0


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposited successfully.")
    else:
        print("Invalid amount!")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance and amount > 0:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance or invalid amount!")


def check_balance():
    print("Current Balance:", balance)



while True:
    print("\n---- Simple Banking Application ----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you for using the banking application.")
        break
    else:
        print("Invalid choice. Try again.")

