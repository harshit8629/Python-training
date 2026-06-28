FILE_NAME = "expenses.txt"


def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense Added")


def view_summary():
    summary = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                amount = float(amount)

                summary[category] = summary.get(category, 0) + amount

        print("\nExpense Summary")
        for category, total in summary.items():
            print(category, ":", total)

    except FileNotFoundError:
        print("No expense file found")


while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        try:
            add_expense()
        except ValueError:
            print("Invalid Amount")

    elif choice == "2":
        view_summary()

    elif choice == "3":
        break
