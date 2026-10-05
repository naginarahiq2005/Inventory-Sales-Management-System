def check_stock(available_quantity,requested_quantity):
    if requested_quantity > available_quantity:
        print('Not enough stock.')
        print(f'Only {available_quantity} item are available.')
        return False
    return True

products =[]

def add_product(product_id,name,price,quantity):
    product = {
        'id' : product_id,
        'name' : name,
        'price': price,
        'quantity' : quantity
    }
    products.append(product)
    return product

def view_products():
    if not products:
        print('No products avaliable.')
        return
    for product in products:
        print(f'ID : {product['id']}')
        print(f'Name : {product['name']}')
        print(f'Price : {product['price']}')
        print(f'Quantity : {product['quantity']}')
        print('_'*25)

def find_product(products_id):
    for product in products:
        if product['id'] == products_id:
            return product
        
    return None
