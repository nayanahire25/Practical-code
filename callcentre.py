
# Queue
User_id_queue = []

# Add Call
def add_call():
    user_id = []

    user_id.append(input("Enter Customer ID: "))
    user_id.append(int(input("Enter Call Time (in minutes): ")))

    User_id_queue.append(user_id)

    print("Call added successfully!")


# Answer Call
def answer_call():
    if len(User_id_queue) == 0:
        print("Queue is empty.")
    else:
        call = User_id_queue.pop(0)

        print("Answering Call:")
        print("Customer ID:", call[0])
        print("Call Time:", call[1], "minutes")


# View Queue
def view_queue():
    if len(User_id_queue) == 0:
        print("Queue is empty.")
    else:
        print("Calls currently in the queue:")

        for i in range(len(User_id_queue)):
            print(
                "Customer ID:", User_id_queue[i][0],
                "| Call Time:", User_id_queue[i][1], "minutes"
            )


# Check Queue Empty
def is_queue_empty():
    if len(User_id_queue) == 0:
        print("Queue is Empty.")
    else:
        print("Queue is Not Empty.")


# Main Program
while (1):

    print("\n===========================================================")
    print("----------------- PROGRAM PREPARED BY NAYAN AHIRE ----------------")
    print("--------------------- MENU : ENTER YOUR CHOICE ---------------------")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")
    print("\n")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add_call()

    elif ch == 2:
        answer_call()

    elif ch == 3:
        view_queue()

    elif ch == 4:
        is_queue_empty()

    elif ch == 5:
        print("=" * 90)
        print("---------------------- THANK YOU FOR USING OUR PROGRAM ----------------------")
        print("\n-------------------------- THANK YOU --------------------------")
        print("\n")
        exit(0)

    else:
        print("Invalid Choice! Please enter a valid choice.")
