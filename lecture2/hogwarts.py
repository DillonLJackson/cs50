students = ["hermione", "harry", "ron"]

for student in students:
    print(student)

 #---------------------------

students = ["hermione", "harry", "ron"]

for i in range(len(students)):
    print(i + 1, students[i])

#----------------------------

students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#-----------------------------


students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

#-----------------------------

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")