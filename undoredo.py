"""
Implementing a real-time undo/redo system for a text editing application using a Stack
data structure.

The system should support the following operations:
1. Make a Change
2. Undo Action
3. Redo Action
4. Display Document State

Name : Nayan Ahire
Roll No. : 7
Div : A
Batch : A
Date : 03/08/2026
"""

# Function to display document

def display_document(document):
    print("\nCurrent Document State:")
    print(document)


# Function to make a change

def make_change(document, undo_stack, redo_stack):

    undo_stack.append(document)

    change = input("Enter the new change: ")

    document = document + change

    redo_stack.clear()

    print("\nChange Made Successfully!")

    return document


# Function for Undo Action

def undo_action(document, undo_stack, redo_stack):

    if len(undo_stack) == 0:
        print("\nNothing to Undo!")

    else:
        redo_stack.append(document)

        document = undo_stack.pop()

        print("\nUndo Successful!")

    return document


# Function for Redo Action

def redo_action(document, undo_stack, redo_stack):

    if len(redo_stack) == 0:
        print("\nNothing to Redo!")

    else:
        undo_stack.append(document)

        document = redo_stack.pop()

        print("\nRedo Successful!")

    return document


# Main Program

document = ""

undo_stack = []

redo_stack = []

while(1):

    print("\n============================================================")

    print("-----------------PROGRAM PREPARED BY NAYAN AHIRE----------------")

    print("--------------------- MENU : ENTER YOUR CHOICE ---------------------")

    print("1. Make a Change")
    print("2. Undo Action")
    print("3. Redo Action")
    print("4. Display Document State")
    print("5. Exit")

    print("\n")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        document = make_change(document, undo_stack, redo_stack)

    elif ch == 2:

        document = undo_action(document, undo_stack, redo_stack)

    elif ch == 3:

        document = redo_action(document, undo_stack, redo_stack)

    elif ch == 4:

        display_document(document)

    elif ch == 5:

        print("=" * 90)

        print("----------------------THANK YOU FOR USING OUR PROGRAM----------------------")

        print("\n-------------------------- THANK YOU -------------")

        print("\n")

        exit(0)

    else:

        print("Invalid Choice! Please enter a valid choice.")