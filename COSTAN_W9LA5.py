tangrd = int(input("Enter your grade:"))

match tangrd:
    case t if 90 <= t <= 100:
        print("EXCELLENT")
    case t if 80 <= t <= 89:
        print("very good")
    case t if 75 <= t <= 79:
        print("passed")
    case t if 0 <= t <= 74:
        print("failed")
    case _:
        print("invalid")

