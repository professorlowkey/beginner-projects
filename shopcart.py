# Shopping Cart

foods = []
prices = []
total = 0
print("----- YOUR CART ORDER -----")
while True:
    food = input("enter food to buy (Q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART ORDER -----")
for food in foods:
    print(food)
    for price in prices:
        total += price

print(f"your total price is: ${total}")
