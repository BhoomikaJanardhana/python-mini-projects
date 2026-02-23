balance = 10000

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful!")
        print("Updated Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))

        if balance - amount < 500:
            print("Minimum ₹500 must remain in account!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Updated Balance:", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")