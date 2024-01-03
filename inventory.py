
#========call on table==========

from tabulate import tabulate

#========The beginning of the class==========

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity} available "

#=============Shoe list===========

shoes_list = []

#==========Functions outside the class==============

def read_shoes_data():  # this reads the data from txt file 
   
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoes_list.append(shoe)
    except FileNotFoundError:
        print("File inventory.txt not available") # encase we cant find the file
    return shoes_list

def capture_shoes(): 

    country = input("Enter country of the shoe :\n ")
    code = input("Enter code of the shoe : \n")
    product = input("Enter what type of shoe it is : \n")
    cost = float(input("Enter the cost of shoe :\n "))
    quantity = int(input("Enter quantity of shoes eg (4): \n"))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe) # added to just terminal 
    print(f"\n{quantity} {product} ({code}) added to inventory, Thank you!")

 
#========== Incase file lol  ==============

    #with open('tasks.txt', 'w') as file:
        #file.write('\n'.join((f'\n{country},{code},{product},{cost},{quantity}')))
    #print("\nThank you, your product has been loaded!\n")

def view_all(): # added to table
    table = []
    for shoe in shoes_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]) # to fill the table
    headers = ["Country", "Code", "Product", "Cost", "Quantity"] # top headings
    print(tabulate(table, headers=headers, tablefmt= 'grid')) # call on import (type of table)

def re_stock():
    min_quantity = None
    min_shoe = None
    for shoe in shoes_list:
        if min_quantity is None or shoe.quantity < min_quantity: # goes through each quant and /shoe
            min_quantity = shoe.quantity
            min_shoe = shoe
    if min_shoe: # when min is found
        choice = input(f"Add {min_quantity} quantity of {min_shoe.product}? (yes/no): ")
        if choice.lower() == "yes":
            new_quantity = int(input("Enter the new quantity: "))
            min_shoe.quantity = new_quantity
            print(f"\n{min_shoe.product} ({min_shoe.code}) restocked to {new_quantity} units!")

def search_shoe():
    code = input("Enter the shoe code: ") 
    found_shoes = []
    for shoe in shoes_list:
        if shoe.code == code: # because we used class we don't want to have use part [1] (strip , ect.)
            found_shoes.append(shoe)
    return found_shoes

def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}): Value - {value}") 

def highest_qty():
    max_quantity = None
    max_shoe = None
    for shoe in shoes_list:
        if max_quantity is None or shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_shoe = shoe
    if max_shoe:
        print(f"The shoe with the highest quantity is {max_shoe.product} ({max_shoe.code} please be advised to on Sale)") # blackfriday


print("Welcome to Nike Shoe Inventory !")
print("Keep track of your Nike shoe inventory with style.")

#==========Main Menu=============

shoes_list = read_shoes_data() 

#========== We like swish Nike ==============

while True:
    print("\n===== Main Menu =====")
    print("1. Capture New Shoe")
    print("2. View All Shoes")
    print("3. Re-stock new Nike Shoes")
    print("4. Search for Shoe")
    print("5. Calculate Value per Item")
    print("6. Identify Highest Quantity Shoe")
    print("7. Exit /TT ")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        found_shoes = search_shoe()
        if found_shoes:
            print("\nSearch Result:")
            for shoe in found_shoes:
                print(shoe)
        else:
            print("No shoe found with the provided code.")
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        print("\nThank you for using Nike Shoe Inventory . Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# had fun thank you