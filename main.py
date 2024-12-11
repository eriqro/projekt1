import csv
import os
from text import welcome

products = []

def load_data(filename): 
    products = [] 
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            products.append({"id": id, "name": name, "desc": desc, "price": price, "quantity": quantity})
    for x in open(filename): 
        print(x)
        print("-" * 110)
    return products

def get_product(products, id):
    for product in products:
        if product['id'] == id:
            return product
        
def add_product():
    id = int(input("ID: "))
    name = input("Namn: ")
    desc = input("Info: ")
    price = float(input("Pris: "))
    quantity = int(input("Antal: "))
    products.append({"id": id, "name": name, "desc": desc, "price": price, "quantity": quantity})
    print("Produkten har lagts till")

def remove_product():
    id = int(input("Id av produkten som ska bort: "))
    product = get_product(products, id)
    if product:
        products.remove(product)
        print("Produkten har tagits bort")
        
    else:
        print("Produkten hittades inte")

while True:
    os.system('CLS')
    welcome()
    products = load_data('db_inventory.csv')  

    print("""
    1. Add a new product
    2. Remove an existing product
    3. View all products
    4. Edit a product by ID
    5. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        print("\nAvailable Products:")
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
        input("\nPress Enter to return to the main menu.")
    elif choice == "4":
        id_to_edit = int(input("Enter the ID of the product you want to edit: "))
        product = get_product(products, id_to_edit)
        if product:
            print(f"Editing Product - ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
            product['name'] = input("Enter new name (leave blank to keep current): ") or product['name']
            product['desc'] = input("Enter new description (leave blank to keep current): ") or product['desc']
            product['price'] = float(input("Enter new price (leave blank to keep current): ") or product['price'])
            product['quantity'] = int(input("Enter new quantity (leave blank to keep current): ") or product['quantity'])
            print("Product updated successfully.")
        else:
            print("Product not found.")
        input("\nPress Enter to return to the main menu.")
    elif choice == "5":
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to return to the main menu.")
