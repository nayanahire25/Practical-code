""":In an e-commerce system, customer account IDs are stored in a list, and you are
tasked with writing a program that implements the following:
•Linear Search: Check if a particular customer account ID exists in the list.
•Binary Search: Implement Binary search to fi nd if a customer account ID exists,
improving the search efficiency over the basic linear)."""






print("=======================================")
print("CUSTOMER ID SEARCHING")
print("PRACT NO.2 BY NAYAN AHIRE")
print("=======================================")

# Function for linear search
def linear_search(l1):
    key = int(input("Enter Customer ID to search: "))


    for i in range(len(l1)):
        if l1[i] == key:
            print("Customer ID Found at index", i)
            return

    print("Customer ID Not Found")


# Function for binary search
def binary_search(l1):
    key = int(input("Enter Customer ID to search: "))

    # Sort list for Binary Search
    l1.sort()
    print("Sorted Customer IDs:", l1)

    low = 0
    high = len(l1) - 1

    while low <= high:
        mid = (low + high) // 2

        if l1[mid] == key:
            print("Customer ID Found at index", mid)
            return

        elif key < l1[mid]:
            high = mid - 1

        else:
            low = mid + 1

    print("Customer ID Not Found")


# Main Program
l1 = []

customer = int(input("Enter the total no of customer: "))

for i in range(customer):
    c = int(input("Enter the ID of customer: "))
    l1.append(c)

print("ID of customer:", l1)

while True:

    # Menu driven code
    print("=======================================")
    print("---- PROGRAM PREPARE BY NAYAN AHIRE----")
    print("=======================================")

    print("\n---------MENU---------")
    print("1. linear search")
    print("2. binary search")
    print("3. exit")

    ch = int(input("Choice: "))

    if ch == 1:
        linear_search(l1)

    elif ch == 2:
        binary_search(l1)

    elif ch == 3:
        print("\n============================")
        print(" THANK YOU FOR USING OUR PROGRAM")
        print(" PROGRAM PREPARE BY NAYAN AHIRE")
        print("=================================")
        print("\n-----------THANK YOU-----------")
        print("\n")
        exit()

    else:
        print("Invalid Choice")