from sales import sales
from products import products

def view_sales():
    if sales is None:
        print('No sales recorded yet.')
        return None
    print('=== Sales Report ===')
    for item in sales:
        print(f'Product : {sales['product_name']}')
        print(f'Quantity sold : {sales['quantity']}')
        print(f'Total_price : {sales['total_price']}')
        print('_'*25)


def calculate_total_revenue():
    total_revenue = 0

    for sale in sales:
        total_revenue +=sale['total_price']

    return total_revenue

def inventory_report():
    print('===== Inventory Report =====')
    if not products:
        print('No product available.')
        return 
    for product in products:
        print(f'Product Name : {product['name']}')
        print(f'Price : {product['price']}')
        print(f'Quantitiy : {product['quantity']}')
        print('_'*30)

def low_stock_report():
    print('====== Low Product ======')
    if not products:
        print('No product available.')
        return
    
    low_stock_report = False

    for product in products:
        if product['quantity'] <= 3:
            print(f'Product Name : {product['name']}')
            print(f'Quantitiy : {product['quantity']}')
            print('_'*30)  
            low_stock_report = True

    if not low_stock_report:
        print('No low_stock products found.')


def revenue_report():
    print('=== Revenue Report ===')
    total_revenue = calculate_total_revenue()
    print(F'Total Revenue : {total_revenue}')


from sales import record_sale
from products import add_product

add_product(2,'Mouse',20,10)
record_sale(2,3)
revenue_report()