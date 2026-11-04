"""problem statement :Write a Python program to manage the borrowing records of books in a
library. Implementthe following functionalities:• Compute the average number of books borrowed
by all library members.• Find the member with the highest and lowest number of borrowings in the
library.• Count the number of members who have not borrowed any books (denoted by aborrow
count of 0).• Display the most frequently borrowed book (i.e., the mode of borrow counts)."""






# Function of average
def average(l1):
    sum_of_books = sum(l1)
    print("average:", sum_of_books / len(l1))


def heighest(l1):
    maxi = 0
    for i in l1:
        if maxi < i:
            maxi = i
    print("heighest_no_of_books :", maxi)


def lowest(l1):
    mini = 700
    for i in l1:
        if mini > i:
            mini = i
    print("lowest_no_of_books :", mini)


def not_borrowed(l1):
    a = 0
    for i in l1:
        if i == 0:  
            a+=1       
    print("not borrowed books :", a)


def most_borrowed(l1):
    max_count = 0
    n = l1[0]

    for i in l1:
        count = 0
        for j in l1:
            if i == j:
                count += 1

        if count > max_count:
            max_count = count
            n = i

    print("most_borrowed_books :", n)


# Main program

l1 = []

n = int(input("Enter total no. of books "))

for i in range(0, n):
    b = int(input("books borrowed by student : "))
    l1.append(b)

print("borrowed books by student ", l1)

while True:

    # Menu driven code
    print("1.Average")
    print("2.heighest")
    print("3.lowest")
    print("4.not_borrowed")
    print("5.most_borrowed")
    print("6.exit")

    ch = int(input("Choice:"))

    if ch == 1:
        average(l1)

    elif ch == 2:
        heighest(l1)

    elif ch == 3:
        lowest(l1)

    elif ch == 4:
        not_borrowed(l1)

    elif ch == 5:
        most_borrowed(l1)

    elif ch == 6:
        exit()

    else:
        print("Invalid input")