
# CHECK OPERATOR
def is_operator(c):
    return c in '+-*/'


# BUILD EXPRESSION TREE
def build_expression_tree(prefix):
    stack = []

    for c in reversed(prefix):

        if not is_operator(c):
            stack.append({'val': c, 'left': None, 'right': None})

        else:
            node = {'val': c, 'left': None, 'right': None}

            node['left'] = stack.pop()
            node['right'] = stack.pop()

            stack.append(node)

    return stack[-1] if stack else None


# POSTORDER TRAVERSAL (NON-RECURSIVE)
def postorder_traversal(root):
    if root is None:
        print("TREE IS EMPTY.")
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node['left']:
            stack1.append(node['left'])

        if node['right']:
            stack1.append(node['right'])

    print("POST-ORDER TRAVERSAL:", end=' ')

    while stack2:
        node = stack2.pop()
        print(node['val'], end=' ')

    print()


# DELETE TREE
def delete_tree(node):
    if node is None:
        return

    delete_tree(node['left'])
    delete_tree(node['right'])

    print("DELETING NODE:", node['val'])

    node['left'] = None
    node['right'] = None


# MAIN PROGRAM
print("***** PRACTICAL NO : 11 PREFIX TO POSTORDER *****")
print("***** PROGRAM PREPARED BY NAYAN AHIRE *****")

root = None

while True:

    print("\n========================================")
    print("              MENU")
    print("========================================")
    print("1. ACCEPT PREFIX EXPRESSION AND BUILD TREE")
    print("2. DISPLAY POST-ORDER TRAVERSAL")
    print("3. DELETE THE TREE")
    print("4. EXIT")
    print("========================================")

    ch = int(input("ENTER YOUR CHOICE: "))

    if ch == 1:
        prefix_expr = input("ENTER PREFIX EXPRESSION: ")

        root = build_expression_tree(prefix_expr)

        print("EXPRESSION TREE BUILT SUCCESSFULLY.")

    elif ch == 2:
        postorder_traversal(root)

    elif ch == 3:
        if root is None:
            print("TREE IS ALREADY EMPTY.")

        else:
            delete_tree(root)
            root = None

            print("ALL NODES DELETED. TREE IS NOW EMPTY.")

    elif ch == 4:
        print("=" * 90)
        print("THANK YOU FOR USING OUR PROGRAM!")
        exit(0)

    else:
        print("INVALID CHOICE! PLEASE ENTER A VALID CHOICE.")