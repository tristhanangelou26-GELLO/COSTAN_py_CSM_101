tan = {}

number = int(input("enter number of students: "))

for i in range(number):
    print("\nstudent", i + 1)

    name = input("Enter students name: ")

    grade1 = float(input("enter first grade: "))
    grade2 = float(input("enter second grade: "))
    grade3 = float(input("enter third grade: "))

    tan[name] = (grade1, grade2, grade3)

    print("\n____________ STUDENTS RECORDS ____________")

for name, grades in tan.items():
    average = sum(grades) / len(grades)

    print(name, *grades, " average: ", round(average, 2))

highest = 0
namehighest = " "
tally = 0

for name, grade in tan.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "average:", average)
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print(f"student {namehighest} got the highest average: {highest}")
print(f"there are {tally} grades which are bellow 75.")