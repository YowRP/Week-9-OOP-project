import json
import os

INVENTORY_FILE = "inventory.json"

class Product:

    def __init__ (self, product_id, name, price, stock):

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock  = stock

    def update_stock(self, quantity):

        if quantity < 0 :
            return False

        else:
            self.__stock = quantity
            return True

    def display_information (self):
        print (f"Product ID:  {self.__product_id} | Product Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def get_product_id (self):
         get_product_ID = self.__product_id
         return get_product_ID

    def to_dict(self):
        return {"Product ID": self.__product_id, "Product Name": self.__name, "Price": self.__price, "Stock": self.__stock}

class Inventory:

    def __init__ (self):
        self.__products = []

    def add_product (self, product):
        for i in self.__products:
            if i.get_product_id() == product.get_product_id():
                return False

        self.__products.append(product)
        return True 

    def search_product (self, product_id):
        for i in self.__products:
            if i.get_product_id() == product_id:
                return i

        return None

    def display_all(self):
        if not self.__products: #Or can add len(self.__products) == 0:
            print ("The Inventory is empty, please fill in something!")
            return 

        for i in self.__products:
            i.display_information()
            
    def get_all_as_dicts(self):
        result = []
        for i in self.__products:
            result.append(i.to_dict())
        return result

def save_inventory (inventory):
    with open (INVENTORY_FILE, "w") as f:
        json.dump(inventory.get_all_as_dicts(), f, indent = 4)

def load_inventory ():
    inventory = Inventory ()
    if os.path.exists(INVENTORY_FILE):
        print("Inventory.json Found")
        with open (INVENTORY_FILE, "r") as f:
            data = json.load(f)
            for i in data:
                product = Product(i["Product ID"], i["Product Name"], i["Price"], i["Stock"])
                inventory.add_product(product)
    else:
        print("Inventory not found.")

    return inventory

def main():
    inventory = load_inventory()

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter the price of the product: ").strip())
                stock = int(input("Enter the stock amount of the product: ").strip())
            except ValueError:
                print("Invalid input, Product not added.")
                continue

            product = Product(product_id , name, price, stock)
            if inventory.add_product(product):
                print("Product added succesfully!")

            else:
                print("Product already exists.")

        elif choice == "3":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found")
                continue

            try:
                new_stock = int(input("Enter the new stock quantity: ").strip())

            except ValueError:
                print("Invalid value. Stock not updated.")
                continue

            if product.update_stock(new_stock):
                print("Stock updated sucessfully.")

            else:
                print("Stock cannot be negative. Stock not updated.")

        elif choice == "4":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found")
            else:
                product.display_information()


        elif choice == "5":
            save_inventory(inventory)
            print("Inventory Saved")

        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved")
            print("Thank you for your use!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
    