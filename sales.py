from products import find_product,check_stock
sales = []
def record_sale(products_id,requested_quantity):
    product = find_product(products_id)

    if product is None:
        print('Product not found!')
        return None
   
    if requested_quantity <= 0:
        print('Quantity must be greater than Zero!')

    available_quantity = product['quantity']

    if not check_stock(available_quantity,requested_quantity):
        return None
    
    total_price = product['price'] * requested_quantity
    
    product['quantity'] -= requested_quantity

    sale = {
        'product_id' : products_id,
        'product_name' : product['name'],
        'quantity': requested_quantity,
        'total_price' : total_price
    }

    sales.append(sale)

    return sale