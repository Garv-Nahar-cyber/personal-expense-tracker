# Personal Expense Tracker

expenses = []
total_expense = 0

print("================================")
print("     PERSONAL EXPENSE TRACKER")
print("================================")

name = input("Enter your name: ")
budget = float(input("Enter your monthly budget: ₹"))

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expense = [expense_name, amount, category]
        expenses.append(expense)

        total_expense = total_expense + amount

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")

        else:
            print("\n------ YOUR EXPENSES ------")

            for i in range(len(expenses)):
                print(i + 1, ".", expenses[i][0],
                      "- ₹", expenses[i][1],
                      "-", expenses[i][2])

    elif choice == "3":
        remaining = budget - total_expense

        print("\n------ SUMMARY ------")
        print("Name:", name)
        print("Monthly Budget: ₹", budget)
        print("Total Expense: ₹", total_expense)
        print("Remaining Money: ₹", remaining)

        if total_expense > budget:
            print("Warning: You have crossed your budget!")

        elif total_expense == budget:
            print("You have used your complete budget.")

        else:
            print("You are within your budget.")

    elif choice == "4":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")