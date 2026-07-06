from datetime import datetime

today = datetime.now().strftime("%A")

subtotal = 0

print("Enter the price and quantity for each item.")
print("Enter 0 for the quantity when you are finished.")

while True:
    quantity = int(input("Quantity: "))

    if quantity == 0:
        break

    price = float(input("Price: $"))
    subtotal += price * quantity

discount = 0

if (today == "Tuesday" or today == "Wednesday") and subtotal >= 50:
    discount = subtotal * 0.10
    subtotal = subtotal - discount

elif today == "Tuesday" or today == "Wednesday":
    amount_needed = 50 - subtotal
    print(f"Spend ${amount_needed:.2f} more to receive the discount.")

sales_tax = subtotal * 0.06
total = subtotal + sales_tax

print(f"Discount amount: ${discount:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total amount due: ${total:.2f}")

