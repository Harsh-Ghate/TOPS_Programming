
"""<p>Open 'kirana_basics.ipynb' and clean 4 messy item names stored in variables:
" toor-DAL 1kg ", "SUGAR (loose)"," aashirvaad atta-10KG" and "tata-salt 1kg ". Use `strip()`, 
`replace()` and `title()` so each prints in title case with no extra spaces or hyphens, for example 
'Toor Dal 1Kg'.Constraint: Do not use `re` or any import.</p>"""

messy_varaible1 = " toor-DAL 1kg "
messy_varaible2 = "SUGAR (loose)"
messy_varaible3 = " aashirvaad atta-10KG"
messy_varaible4 = "tata-salt 1kg "
print(messy_varaible1.strip().replace("-"," ").title())
print(messy_varaible2.strip().replace("-"," ").title())
print(messy_varaible3.strip().replace("-"," ").title())
print(messy_varaible4.strip().replace("-"," ").title())