print("=======================================")
print(" EMPLOYEE SALARY SORTING")
print(" PRACT NO.3 BY NAYAN AHIRE")
print("=======================================")

# Main Program

def selection_sort(salary):

    n = len(salary)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if salary[j] < salary[min_index]:
                min_index = j

        salary[i], salary[min_index] = salary[min_index], salary[i]

    print("\nSalaries after Selection Sort:")
    print(salary)

    print("\nTop Five Highest Salaries:")
    for i in range(len(salary) - 1, max(len(salary) - 6, -1), -1):
        print(salary[i])


def bubble_sort(salary):

    n = len(salary)

    for i in range(n):
        for j in range(0, n - i - 1):
            if salary[j] > salary[j + 1]:
                salary[j], salary[j + 1] = salary[j + 1], salary[j]

    print("\nSalaries after Bubble Sort:")
    print(salary)

    print("\nTop Five Highest Salaries:")
    for i in range(len(salary) - 1, max(len(salary) - 6, -1), -1):
        print(salary[i])


salary = []

employee = int(input("Enter the total number of employees: "))

for i in range(employee):
    s = float(input("Enter the salary of employee: "))
    salary.append(s)

print("Employee Salaries:", salary)

while (1):

    # Menu Driven Code

    print("=======================================")
    print("---- PROGRAM PREPARE BY NAYAN AHIRE----")
    print("=======================================")

    print("\n---------MENU---------")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        
        selection_sort(salary)

    elif ch == 2:
       
        bubble_sort(salary)

    elif ch == 3:

        print("\n============================")
        print(" THANK YOU FOR USING OUR PROGRAM ")
        print(" Program Prepared By NAYAN AHIRE")
        print("=================================")
        print("\n-----------THANK YOU-----------")
        print("\n")
        exit()

    else:
        print("Invalid Choice! Please Enter Again.")