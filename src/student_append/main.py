import os

os.system("clear")

students = []

with open('students.txt', 'r') as file:
    for line in file:
        if '.' in line:
            students.append(line.split('.', 1)[1].strip())


def menu():
    User = input("Input User's name: ")
    on = True
    while on:
        os.system("clear")
        match int(input(f"Good day user {User}, what would you like to do today?\n[1] input student name\n[2] show student\n[3] exit\nenter choice: ")):
            case 1:
                os.system("clear")
                adding = True
                while adding:
                    fname = input(
                        "kindly input the first name of the student to add in the list.\n")

                    lname = input(
                        "kindly input the last name of the student to add in the list.\n")

                    names = fname.capitalize() + " " + lname.capitalize()
                    students.append(names)

                    again = input(
                        "Would you like to add another student? (Y/n)")
                    if again.lower() == 'n':
                        adding = False

                with open('students.txt', 'w') as this:
                    for index, student in enumerate(students, 1):

                        this.write(f'{index}. {student}\n')
            case 2:
                os.system("clear")
                with open('students.txt', 'r') as this:

                    data = this.read()
                    input(f"{data}\npress enter to continue...")
            case 3:

                os.system("clear")
                on = False

            case _:
                input(
                    "Value Error: please input the correct displayed integer!\nPress enter to continue...")


menu()
