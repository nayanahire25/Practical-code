
# INSERTION
def insert(root, key):
    if root is None:
        return {'key': key, 'left': None, 'right': None}

    if key < root['key']:
        root['left'] = insert(root['left'], key)

    elif key > root['key']:
        root['right'] = insert(root['right'], key)

    return root


# SEARCH
def search(root, key):
    if root is None:
        return False

    if key == root['key']:
        return True

    elif key < root['key']:
        return search(root['left'], key)

    else:
        return search(root['right'], key)


# FIND MINIMUM VALUE
def min_value_node(root):
    while root['left'] is not None:
        root = root['left']

    return root


# DELETION
def delete(root, key):
    if root is None:
        return root

    if key < root['key']:
        root['left'] = delete(root['left'], key)

    elif key > root['key']:
        root['right'] = delete(root['right'], key)

    else:
        if root['left'] is None:
            return root['right']

        elif root['right'] is None:
            return root['left']

        temp = min_value_node(root['right'])
        root['key'] = temp['key']
        root['right'] = delete(root['right'], temp['key'])

    return root


# DISPLAY
def inorder(root):
    if root is not None:
        inorder(root['left'])
        print(root['key'], end=" ")
        inorder(root['right'])


# MAIN PROGRAM
root = None

# TAKE INITIAL KEYS FROM USER
n = int(input("ENTER NUMBER OF INITIAL KEYS TO INSERT: "))

print("ENTER THE KEYS:")

for i in range(n):
    key = int(input("ENTER KEY: "))
    root = insert(root, key)


# MENU
while True:

    print("\n========================================")
    print("       BINARY SEARCH TREE MENU")
    print("========================================")
    print("PROGRAM PREPARED BY NAYAN AHIRE")
    print("1. INSERT A KEY")
    print("2. SEARCH FOR A KEY")
    print("3. DELETE A KEY")
    print("4. DISPLAY BST")
    print("5. EXIT")
    print("========================================")

    ch = int(input("ENTER YOUR CHOICE: "))

    if ch == 1:
        key = int(input("ENTER KEY TO INSERT: "))
        root = insert(root, key)
        print("KEY INSERTED SUCCESSFULLY!")

    elif ch == 2:
        key = int(input("ENTER KEY TO SEARCH: "))

        if search(root, key):
            print("KEY FOUND IN BST.")
        else:
            print("KEY NOT FOUND IN BST.")

    elif ch == 3:
        key = int(input("ENTER KEY TO DELETE: "))

        if search(root, key):
            root = delete(root, key)
            print("KEY DELETED SUCCESSFULLY!")
        else:
            print("KEY NOT FOUND IN BST.")

    elif ch == 4:
        print("INORDER TRAVERSAL:")
        inorder(root)
        print()

    elif ch == 5:
        print("=" * 90)
        print("THANK YOU FOR USING OUR PROGRAM!")
        exit(0)

    else:
        print("INVALID CHOICE! PLEASE ENTER A VALID CHOICE.")
