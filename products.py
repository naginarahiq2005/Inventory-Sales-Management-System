class Product:
    def __init__(self,id,name,price,quantity):

        if not id.strip():
            raise ValueError('Product ID cannot be empty.')
        if not name.strip():
            raise ValueError('Product name cannot be empty.')
        if price < 0 :
            raise ValueError('Price con not be negative.')
        if quantity <0 :
            raise ValueError('Quantity connot be negative.')
        

        self.id = id 
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Price : {self.price}')
        print(f'Quantity : {self.quantity}')
        print('_'*25,'\n')

    def check_stock(self,requested_quantity):
        return requested_quantity <= self.quantity
    
    def reduce_stock(self,sold_quantity):
        if sold_quantity <= 0:
            raise ValueError('Quantity must be greater than Zero!')
        
        if not self.check_stock(sold_quantity):
            raise ValueError('Not enough stack.')
        
        self.quantity -= sold_quantity


       

# def check_stock(available_quantity,requested_quantity):
#     if requested_quantity > available_quantity:
#         print('Not enough stock.')
#         print(f'Only {available_quantity} item are available.')
#         return False
#     return True

# products =[]

# def add_product(product_id,name,price,quantity):
#     product = {
#         'id' : product_id,
#         'name' : name,
#         'price': price,
#         'quantity' : quantity
#     }
#     products.append(product)
#     return product

# def view_products():
#     if not products:
#         print('No products avaliable.')
#         return
#     for product in products:
#         print(f'ID : {product['id']}')
#         print(f'Name : {product['name']}')
#         print(f'Price : {product['price']}')
#         print(f'Quantity : {product['quantity']}')
#         print('_'*25,'\n')

# def find_product(products_id):
#     for product in products:
#         if product['id'] == products_id:
#             return product
        
#     return None

# def validate_product(name,price,quantity):
#     if not name.strip():
#         return False
#     if price < 0 :
#         return False
#     if quantity < 0 :
#         return False
#     return True

