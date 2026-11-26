"""
<p>Add a cell that slices the SKU code "KIR-2025-GUJ-00123" to get the year, 
the state code and the serial number using indexing and slicing with at least one negative index, 
and prints the reversed SKU using `[::-1]`.</p>
"""

SKU_code = "KIR-2025-GUJ-00123"
print(f"Year: {SKU_code[4:8]}") 
print(f"State Code: {SKU_code[9:12]}")
print(f"Serial Number: {SKU_code[-5:]}")
print(f"Reversed SKU: {SKU_code[::-2]}")