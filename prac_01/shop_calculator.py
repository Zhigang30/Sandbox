"""
CP1404/CP5632 - Practical
"""

while True:
    num_items = int(input("Number of items: "))
    if num_items >= 0:
        break
    print("Invalid number of items!")

total_price = 0

for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

print(f"Total price for {num_items} items is ${total_price:.2f}")
