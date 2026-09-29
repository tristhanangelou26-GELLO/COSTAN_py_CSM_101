students = {
    "ana": 85,
    "ben": 98,
    "carlo": 78,
    "diana": 95,
}
print("Student grade")
print("ana: ", students["ana"])
print("ben: ", students["ben"])

students["ella"] = 88
students["gello"] = 90

students["carlo"] = 82
students["diana"] = 91
name1 = input("enter students name: ")
grade1 = int(input("enter grade: "))
students[name1] = grade1
print(students)
print("--updated students grades--")
print("_____________________________")
for name, grade in students.items():
    print(name, ":",grade)

search = input("\nEnter students name to search: ")
if search in students:
    print(search,"has a grade of",students[search])
else:
    print("students not found")