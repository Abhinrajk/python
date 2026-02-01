

# 8 LibraryManagementSystem

library = {}

def add_book(book_id, title, author, copies):
    library[book_id] = {
        "Title": title,
        "Author": author,
        "Copies": copies
    }
    print("Book added successfully!")

def issue_book(book_id):
    if book_id in library:
        if library[book_id]["Copies"] > 0:
            library[book_id]["Copies"] -= 1
            print("Book issued successfully!")
        else:
            print("Book not available!")
    else:
        print("Book not found!")


def return_book(book_id):
    if book_id in library:
        library[book_id]["Copies"] += 1
        print("Book returned successfully!")
    else:
        print("Book not found!")

def search_book(title):
    found = False
    for book_id, details in library.items():
        if title.lower() in details["Title"].lower():
            print("\nBook Found:")
            print(f"Book ID : {book_id}")
            print(f"Title   : {details['Title']}")
            print(f"Author  : {details['Author']}")
            print(f"Copies  : {details['Copies']}")
            found = True
    if not found:
        print("Book not found!")

add_book(1, "Python Programming", "Guido van Rossum", 3)
add_book(2, "Data Structures", "Mark Allen", 2)

issue_book(1)
return_book(1)
search_book("Python")
