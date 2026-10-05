from products import check_stock ,add_product, view_products, find_product

first = add_product(101,'Laptop',500,5)
print(f'New product : {first}')

view_products()
result = find_product(101)
print(result)

from products import add_product, find_product
from sales import record_sale

add_product(101, "Laptop", 500, 3)

result = record_sale(101, 2)

print("Sale result:", result)
print("Updated product:", find_product(101))