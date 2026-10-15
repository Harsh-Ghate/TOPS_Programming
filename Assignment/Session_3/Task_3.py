
"""Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'],
 convert all to floats and calculate the total cart value."""

Flipkart_list = ['199.99','299.50','150']
Total_cart_value = 0.0
for price in Flipkart_list:
    price = float(price)
    Total_cart_value += price
print(f"Total Value of your Flipkart Cart is : {Total_cart_value:.2f}")
