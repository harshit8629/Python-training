contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")

        duplicate = False

        for num in contacts.values():
            if num == number:
                duplicate = True
                break

        if duplicate:
            print("Number already exists")
        else:
            contacts[name] = number
            print("Contact Added")

    elif choice == "2":
        name = input("Enter name: ")
        print(contacts.get(name, "Not Found"))

    elif choice == "3":
        name = input("Name: ")

        if name in contacts:
            contacts[name] = input("New Number: ")
            print("Updated")
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "6":
        break

    else:
        print("Invalid Choice")
