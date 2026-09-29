students={"ana":[90,85,82],
          "kirk":[72,73,78]
          }
students={"ana":(90,88,92),
          "kirk":(87,85,86)

}

for name, grade in students.items():
    print(name,*grade)