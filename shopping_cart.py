cart = []
prices = {}
categories = set()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Total Bill")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        item = input("Item Name: ")
        price = float(input("Price: "))
        category = input("Category: ")

        cart.append(item)
        prices[item] = price
        categories.add(category)

    elif choice == "2":
        item = input("Item to remove: ")

        if item in cart:
            cart.remove(item)
            del prices[item]

    elif choice == "3":
        print("\nCart Items")

        for item in cart:
            print(item, "-", prices[item])

        print("Categories:", categories)

    elif choice == "4":
        total = sum(prices.values())
        print("Total Bill =", total)

    elif choice == "5":
        break
