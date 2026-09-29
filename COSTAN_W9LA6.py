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

match tanflav:
    case flavor if flavor in tanpizza_menu:
        print(f"YOU HAVE SELECTED {flavor.upper()} PIZZA")
        tansize = input("ENTER SIZE (SMALL/MEDIUM/LARGE): ").strip().lower()

        match tansize:
            case size if size in tanpizza_menu[flavor]:
                PRIZE = tanpizza_menu[flavor][size]
                print(f"PRICE: {PRIZE}")
            case _:
                print("Invalid size selected.")
    case _:
        print("Invalid flavor selected.")