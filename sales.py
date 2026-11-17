sales = []
def record_sale(inventory ,id,requested_quantity):
    product = inventory.find_product(id)

    if not product :
        print('Product not found!')
        return None
   
    if requested_quantity <= 0:
        raise ValueError('Quantity must be greater than Zero!')

    if not product.check_stock(requested_quantity):
        print(f"Only {product.quantity} item(s) are available.")
        return None
    
    total_price = product.price * requested_quantity
    product.reduce_stock(requested_quantity)


    sale = {
        'product_id' : product.id,
        'product_name' : product.name,
        'quantity': requested_quantity,
        'total_price' : total_price,
    }

    sales.append(sale)

    return sale