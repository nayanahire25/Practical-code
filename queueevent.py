# Function to add event
def add():
    e = input("Enter Event: ")
    queue.append(e)
    print("EVENT IS ADDED")


# Function to process event
def process():
    if queue == []:
        print("NO EVENT TO PROCESS")
    else:
        print("EVENT IS PROCESSED:", queue.pop(0))


# Function to display pending events
def display():
    print("PENDING EVENTS:", queue)


# Function to cancel event
def cancel():
    e = input("Enter Event to Cancel: ")

    if e in queue:
        queue.remove(e)
        print("EVENT IS CANCELLED")
    else:
        print("EVENT NOT FOUND")


# Main Program
queue = []

while True:

    print("\n---------MENU---------")
    print("1. Add Event")
    print("2. Process Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        add()

    elif ch == 2:
        process()

    elif ch == 3:
        display()

    elif ch == 4:
        cancel()

    elif ch == 5:
        print("THANK YOU")
        exit()

    else:
        print("Invalid Choice")