
# Hash Table Size
SIZE = 10

# Create Hash Table using Chaining
Hash_table = [[] for i in range(SIZE)]


# Hash Function - Division Method
def hash_function(key):
    return key % SIZE


# Insert Key
def insert_key():
    key = int(input("Enter Key: "))

    index = hash_function(key)

    Hash_table[index].append(key)

    print("Key inserted successfully!")


# Search Key
def search_key():
    key = int(input("Enter Key to Search: "))

    index = hash_function(key)

    if key in Hash_table[index]:
        print("Key found at index:", index)
        return

    print("Key not found.")


# Delete Key
def delete_key():
    key = int(input("Enter Key to Delete: "))

    index = hash_function(key)

    if key in Hash_table[index]:
        Hash_table[index].remove(key)

        print("Key deleted successfully!")
    else:
        print("Key not found.")


# Display Hash Table
def display_table():
    print("\nHash Table:")

    for i in range(SIZE):
        print("Index:", i, "| Chain:", Hash_table[i])


# Main Program
while True:

    print("\n===========================================================")
    print("----------------- PROGRAM PREPARED BY NAYAN AHIRE ----------------")
    print("--------------------- MENU : ENTER YOUR CHOICE ---------------------")

    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Hash Table")
    print("5. Exit")

    print("===========================================================")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        insert_key()

    elif ch == 2:
        search_key()

    elif ch == 3:
        delete_key()

    elif ch == 4:
        display_table()

    elif ch == 5:
        print("=" * 90)
        print("---------------------- THANK YOU FOR USING OUR PROGRAM --------------------")
        print("\n")
        exit(0)

    else:
        print("Invalid Choice! Please enter a valid choice.")
