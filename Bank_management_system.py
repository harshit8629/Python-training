balance = 1000

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Updated Balance:", balance)

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    balance -= amount
    print("Updated Balance:", balance)

actions = {
    "1": check_balance,
    "2": deposit,
    "3": withdraw
}

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "4":
        break

    actions[choice]()