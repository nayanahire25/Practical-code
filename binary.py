









print("=======================================")
print("       CUSTOMER ID SEARCHING")
print("     PRACT NO.2 BY NAYAN AHIRE")
print("=======================================")

#Main Program

def linear_search(l1):
    key = int(input("Enter Customer ID to search: "))

    for i in range(len(l1)):
        if l1[i] == key:
            print("Customer ID Found at index", i)
            return

    print("Customer ID Not Found")


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


l1 = []

customer = int(input("Enter the total no of customer: "))

for i in range(customer):
    c = int(input("Enter the ID of customer: "))
    l1.append(c)

print("ID of customer:", l1)

while (1):
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
        print(" THANK YOU FOR USING OUR PROGRAM ")
        print(" Program Prepared By  NAYAN AHIRE")
        print("=================================")
        print("\n-----------THANK YOU-----------")
        print("\n")
        
        exit()