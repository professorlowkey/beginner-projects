# Peter Roll Centre

menu = {"roll": 0.72,
        "eggroll": 0.48,
        "noodles": 0.84,
        "maggi": 0.60,
        "samosa": 0.08,
        "lassi": 0.24}

cart = []
total = 0
print("------ PETER ROLL CENTRE ------")
for key, value in menu.items():
    print(f"{key:18}: ${value:.2f}")
print("-------------------------------")

while True:
    food = input("Select an item (q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is: ${total:.2f}")
