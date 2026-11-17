class Inventory:
    def __init__(self,):
        self.products = []

   
    def find_product(self,id):
        for product in self.products:
            if product.id == id:
                return product
        return None
    
    def add_product(self,product):
        if self.find_product(product.id) is not None:
            print('This product ID already exists.')
            return False

        self.products.append(product)
        print('Product added successfully.')
        return True
       
 
    def view_products(self):
        if not self.products:
            print('No products avaliable.')
            return
        
        for product in self.products:
            product.display()