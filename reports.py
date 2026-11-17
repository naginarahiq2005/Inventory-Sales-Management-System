from sales import sales

def view_sales(sales):
    if not sales :
        print('No sales recorded yet.')
        return 
    
    print('=== Sales Report ===')
    for sale in sales:
        print(f'Product : {sale['product_name']}')
        print(f'Quantity sold : {sale['quantity']}')
        print(f'Total_price : {sale['total_price']}')
        print('_'*25)


def calculate_total_revenue(sales):
    return sum(sale["total_price"] for sale in sales)

def inventory_report(inventory):
    print('===== Inventory Report =====')

    if not inventory.products:
        print('No product available.')
        return 
    
    for product in inventory.products:
        print(f'Product Name : {product.name}')
        print(f'Price : {product.price}')
        print(f'Quantitiy : {product.quantity}')
        print('_'*30)

def low_stock_report(inventory):
    print("===== Low Stock Report =====")

    if not inventory.products:
            print("No products available.")
            return

    found_low_stock = False

    for product in inventory. products:
        if product.quantity <= 3:
            print(f'Product Name : {product.name}')
            print(f'Quantitiy : {product.quantity}')
            print('_'*30,'\n')  
            found_low_stock = True

    if not found_low_stock:
        print('No low_stock products found.')


def revenue_report(sales):
    print('\n=== Revenue Report ===')
    total_revenue = calculate_total_revenue(sales)
    print(F'Total Revenue : {total_revenue}\n')