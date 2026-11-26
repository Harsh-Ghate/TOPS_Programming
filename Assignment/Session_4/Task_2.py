
"""<p>Add a cell that splits the record string "Toor Dal|1|168|42" with `split("|")`, 
then reads item, pack_kg, price_inr and stock using index positions, 
converts the numbers with `int()`, and prints a one-line sentence using `upper()` 
for the item name and `lower()` for the unit 'KG'.</p>"""


item = "Toor Dal|1|168|42"
item = item.split("|")

name = item[0].upper()
pack_kg = int(item[1])
price_inr = int(item[2])
stock = int(item[3])

unit = "KG".lower()

print(f"{name} - {pack_kg} {unit}, Price: ₹{price_inr}, Stock: {stock}")