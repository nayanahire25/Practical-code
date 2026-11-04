
# Hash Table
Hash_table = []

SIZE = int(input("PLEASE ENTER THE SIZE OF TABLE: "))

# Create Hash Table
Hash_table = [-1] * SIZE


# Hash Function
def hash_function(key):
    return key % SIZE


# Insert Key
def insert_key():
    key = int(input("Enter Key: "))

    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if Hash_table[new_index] == -1:
            Hash_table[new_index] = key

            print("Key inserted successfully!")
            return

    print("Hash Table is Full!")


# Search Key Element
def search_key():
    key = int(input("Enter Key to Search: "))

    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if Hash_table[new_index] == key:
            print("Key found at index:", new_index)
            return

    print("Key not found.")


# Delete Key
def delete_key():
    key = int(input("Enter Key to Delete: "))

    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if Hash_table[new_index] == key:
            Hash_table[new_index] = -1

            print("Key deleted successfully!")
            return

    print("Key not found")


# Display Hash Table
def display_table():
    print("\nHash Table")

    for i in range(SIZE):
        print("Index:", i, "| Key:", Hash_table[i])


# Main Program
while True:

    print("\n---------------- HASH TABLE ----------------")
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Hash Table")
    print("5. Exit")
    print("--------------------------------------------")

    ch = int(input("Enter your choice: "))

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
        print("---------------- THANK YOU FOR USING OUR PROGRAM ----------------")
        print("\n---------------- THANK YOU ----------------")
        print("\n")
        exit(0)

    else:
        print("Invalid Choice! Please enter a valid choice.")