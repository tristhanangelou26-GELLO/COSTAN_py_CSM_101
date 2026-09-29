TANname = input("enter your name: ").title()
TANmnth = int(input("Enter Month: "))


if TANmnth >=1 and TANmnth <=3:
     NAT = ("Rainy: Not a good month to travel due to flooding in many areas")
elif TANmnth >= 4 and TANmnth <= 5:
     NAT = ("Summer: A good time to travel")
elif TANmnth >=6 and TANmnth <=8:
     NAT = ("Mixed Weather: Typhoon may come and the country may experience typhoon or good weather")
elif TANmnth >=  9 and TANmnth <= 12:
     NAT = ("Christmas Vibe: Still a mixed weather")

else:
    print("invalid")
print(f"Hey {TANname}")
print(f"{NAT}")



