books = []

def add_book():
    title = input("Enter book name: ")
    books.append(title)
    print("Book added successfully!")

def view_books():
    print("\nBooks in Library:")
    for book in books:
        print(book)

def search_book():
    title = input("Enter book name to search: ")
    print("Found!" if title in books else "Not Found!")

def remove_book():
    title = input("Enter book name to remove: ")
    books.remove(title)
    print("Book removed successfully!")

actions = {
    "1": add_book,
    "2": view_books,
    "3": search_book,
    "4": remove_book
}

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        break

    actions[choice]()

print("Thank you!")