
records = {"gello":{"Studid": "5001",
            "Grade": [90,85,86,82,83,90,92]
             },
           "carl": {"Studid": "5002",
             "Grade": [72,75,69,80,84,75,85]
             },
           "ayon":{"Studid": "5003",
              "Grade": [77,70,75,75,74,77,75]    }
            }


Search = input("ENTER NAME PLS: ").lower()

if Search in records:
    print("\nStudent found")
    print("Student name:", Search)
    print("student ID:", records[Search]["Studid"])

    grade = records[Search]["Grade"]

    print("GRADES: ", grade)

    Average = sum(grade) / len(grade)
    print("AVERAGE: ",round(Average,2))

    if min(grade) < 60:
        print("CANDIDATE FOR INTERVENTION")
    else:
        print("NO INTERVENTION NEEDED")

        print("HIGHEST GRADE:", max(grade))
        print("LOWEST GRADE: ",min(grade))

else:
    print("STUDENT NOT FOUND")