"""Build a console program that calculates and displays the final bill for a food delivery order
based on order value and delivery distance."""

print("Delivery Fee Calculator")

order_value=float(input("Enter the order value: Rupees "))
delivery_distance=float(input("Enter the delivery distance (in Kilometers): "))

# Calculate the delivery fee based on the order value and delivery distance
if order_value >= 500:
    delivery_fee = 0
elif delivery_distance >= 5:
    delivery_fee = 30
else:
    delivery_fee = 60

# Displaying the order value
print("Item Total: Rupees ", order_value)
# Dislpaying the delivery fee
print("Delivery Fee: Rupees ", delivery_fee)

# Calculate the final bill
final_bill = order_value + delivery_fee

# Display the final bill
print(f"Final Bill: Rupees {final_bill:.2f}")