
"""Create variables for order_total, delivery_region, and discount_percent to represent a Zomato order. 
Follow Python naming conventions and print a sentence using all three variables, 
like 'Order from [region] totals ₹[order_total] with [discount_percent]% discount.'"""

#order_total variable stores total value of the order
order_total = 700

#delivery_region variable stores the location of the order where it should be delivered
delivery_region = "Thaltej"

#discount_percent stores the amount of discount applied on the order
discount_percent = 15

print(f" Order placed from {delivery_region}\n The total value of order ₹{order_total}\n discount : {discount_percent}% ")