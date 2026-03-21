print("Expense Tracker")
expenses = []
while True:
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Category report")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            expenses.append((amount, category))
            print("Expense added successfully!")
    elif choice == '2':
            print("Expenses:")
            for expense in expenses:
                print(f"Amount: {expense[0]}, Category: {expense[1]}")
    elif choice == '3':
            category_report = {}
            for expense in expenses:
                if expense[1] in category_report:
                    category_report[expense[1]] += expense[0]
                else:
                    category_report[expense[1]] = expense[0]
            print("Category Report:")
            for category, total in category_report.items():
                print(f"Category: {category}, Total Expense: {total}")
    elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
    else:
            print("Invalid choice. Please try again.")
        

