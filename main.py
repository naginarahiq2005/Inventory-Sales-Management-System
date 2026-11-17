from products import Product
from Inventory import Inventory
from sales import record_sale, sales
from reports import (
    view_sales,
    inventory_report,
    low_stock_report,
    revenue_report,
)
from storage import load_data,save_data

inventory, saved_sales = load_data()
sales.extend(saved_sales)

while True:
    print('========== Inventory and Sales Managment System ===========')
    try:
        choice = int(input('''Enter yor Option :
    1 : Add Product
    2 : View Products
    3 : Find product
    4 : Record Sale
    5 : View Sales
    6 : Inventory Report
    7 : Low Stock Report
    8 : Revenue Report 
    9 : Exit
        \n'''))
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if choice == 1:
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, price, quantity)
            if inventory.add_product(product):
                save_data(inventory, sales)
        except ValueError as error:
            print(f"Could not add product: {error}")
    
    elif choice == 2:
        inventory.view_products()

    elif choice == 3:
        id_2 = input('Enter Product ID :')
        product = inventory.find_product(id_2)

        if product is None:
            print("Product not found.")
        else:
            product.display()


    elif choice == 4:
        id_3 = input('Enter Product ID :')
        
        try:
            quantity = int(input("Enter quantity to sell: "))
            sale = record_sale(inventory, id_3, quantity)

            if sale is not None:
                print("Sale recorded successfully.")
                print(f"Product: {sale['product_name']}")
                print(f"Quantity sold: {sale['quantity']}")
                print(f"Total price: {sale['total_price']}")
                save_data(inventory, sales)
        except ValueError as error:
            print(f"Could not record sale: {error}")

    elif choice == 5:
        view_sales(sales)

    elif choice == 6:
        inventory_report(inventory)

    elif choice == 7:
        low_stock_report(inventory)

    elif choice == 8:
        revenue_report(sales)

    elif choice == 9:
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid Option.')