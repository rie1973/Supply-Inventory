# Ann Smith
# July 4th, 2022
#
# Python Program #4
#
# This program will help a client order parts, help the company track track inventory,
# and print a receipt of all ordered parts with a grand total for the entire order.

supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'

# Your code goes here

import json
import math

supplier_data = json.loads(supplier_data)


#introduction to ordering system
print()
print("Welcome to the parts ordering system. Please enter in a part name, followed by a quantity.");
print()

# print list of available parts
print("Parts for order are:")
print()

for element in supplier_data['parts']:
    print (f"{element}")
    print()

    
#set variables
create_order = True
entered_order = {}
enter_quantity = ()
val_new = ()
total = 0
total_part_price = 0


while create_order:

    print()

# enter part name and create report, with the need to reflect zero entries
    first_enter_part = input("Please enter a part name, or quit to exit: ")
    print()
    
    if first_enter_part.lower() == "quit":

        print()
        print()
        print("Your order")
        print()
        
        for key, value in entered_order.items():
            price = supplier_data[key]['price']
            
            total_part_price = price *  float(entered_order[key]) 
            total = total_part_price + total

            print(key, "-", entered_order[key], "@", supplier_data[key]['price'], "=", "{:.2f}".format(total_part_price))         
            print()

        print(f"Total: $", "{:.2f}".format(total))
        print()
        print("Thank you for using the parts ordering system!")
        break
        
#vaidate user input

    #validate part
    enter_part = first_enter_part.lower()
    if enter_part not in supplier_data['parts']:
        print()
        print("Error, part does not exist. Try again")
        continue

    #validate order quantity
    enter_quantity = input("Please enter in a quantity to order: ")

    for key, value in supplier_data.items():
        if key == enter_part:
            if int(enter_quantity) > value['quantity'] or int(enter_quantity) < 0:
                print()
                print("Error, only", value['quantity'], enter_part, "are available!")
            continue

    #set key and value to create new dictionary
    key = enter_part
    value = enter_quantity
    flag = True

    #create new dictionary to hold parts and amount ordered    
    if key not in entered_order and int(enter_quantity) > 0 and int(enter_quantity) <= supplier_data[key]['quantity']:

        entered_order[key] = value
        
    # compare new dictionary to supplier data, validate that accumulated part quantity
    # does not exceed supplier_data quantity

    elif key in entered_order and int(enter_quantity) > 0: 
        val_new = entered_order[key]
        val_new = int(val_new) + int(enter_quantity)
           
        available_stock = supplier_data[key]['quantity'] - int(entered_order[key])

        if int(val_new) > int(supplier_data[key]['quantity']):
            
            print("Error, only", available_stock, enter_part, "are available!")
            
            flag = False
        
        if flag == True:
            entered_order[key] = val_new
            

