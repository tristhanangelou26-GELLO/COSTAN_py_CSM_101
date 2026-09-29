tanpizza_menu = {
    "hawaiian": {"small": 200, "medium": 350, "large": 500},
    "pepperoni": {"small": 220, "medium": 380, "large": 550},
    "cheese": {"small": 180, "medium": 300, "large": 450},
    "fourcheese": {"small": 250, "medium": 400, "large": 600},
    "tacopizza": {"small": 230, "medium": 390, "large": 580},
}

tanflav = input(
    "Enter the pizza flavor you want (HAWAIIAN/PEPPERONI/CHEESE/FOURCHEESE/TACOPIZZA): "
).strip().lower()

if tanflav in tanpizza_menu:
    print(f"YOU HAVE SELECTED {tanflav.upper()} PIZZA")

    tansize = input("ENTER SIZE (SMALL/MEDIUM/LARGE): ").strip().lower()

    if tansize in tanpizza_menu[tanflav]:
        PRIZE = tanpizza_menu[tanflav][tansize]
        print(f"PRICE: {PRIZE}")
    else:
        print("Invalid size selected.")
else:
    print("Invalid flavor selected.")