students = [
    "Kristen Gozun",
    "Matthew Cruz",
    "Daniel Cuevas",
    "Samantha Daniel",
    "Christine Coste",
    "Aira Sabino",
    "Xian Anunciacion",
    "Ian Selom",
    "Samuel Icalia",
    "Samantha Salazar",
    "John Doe",
    "Prince Gian",
    "Gian Anunciacion"
]

file = open("students(sir's_version).txt", "w")

for index, student in enumerate(students, 1):
    file.write(f"{index}. {student}\n")
    print(f"{index}. {student}")

for i in range(3):
    fname = input("\nwhat is the student's first name\nenter:")
    lname = input("\nwhat is the student's last name\nenter:")
    name = fname + ' ' + lname
    students.append(name)

for index, student in enumerate(students, 1):
    file.write(f"{index}. {student}\n")
    print(f"{index}. {student}")
