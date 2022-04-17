import csv # csv manipulation library
from prettytable import from_csv
from prettytable import PrettyTable

def average_fun(inventory): # find average of prices
    # control variables
    count = 0
    average = 0
    sum = 0
    for item in inventory:
        count = count + 1 # counting item numbers
        sum = sum + float(item[5]) # calculating price sum
    average = sum / count
    average = format(average, ".2f") # format average to 2 decimal points
    return average

def least_quantity(inventory): # find the item with least quantity
    i = inventory[1][4] # get an item quantity for comparison basis ( initial minimum )
    minItem = None # control variable
    for item in inventory:
        if int(item[4])<int(i): # if item quantity less than the initial minimum
            minItem = item # get items details
            i = int(item[4]) # update minimum quantity
    minItem.pop(6) # remove total from the table
    minItem.append("Least Quantity Item") # mark item with status for function 8
    return minItem

def minimum_price(inventory):
    i = inventory[1][5] # initial minimum price
    minItem = None
    for item in inventory:
        # if item price less than initial minimum
        if float(item[5])<float(i):
            i = item[5] # update initial minimum
            minItem =item # store items data
    minItem.pop(6) # remove total price column form the table
    minItem.append("Min Price Item") # mark the row with status
    return minItem

def maximum_price(inventory):
    i = inventory[1][5] # initial maximum value
    maxItem = None
    for item in inventory:
        # if item value greater than initial max
        if float(item[5]) >float(i):
            i = item[5] # update i
            maxItem = item # strore item data
    maxItem.pop(6) # remove total price column
    maxItem.append("Max Price item ") # mark row with the status
    return maxItem

def add_Item(inventory): # add item function
    print("Item Addition to stock")
    car_make = input("Enter The Car Make: ")
    car_model = input("Enter The Car Model: ")
    part_no = input("Enter Part No.: ")
    part_name = input("Enter Part Name: ")
    part_Quantity = input("Enter Part Quantity: ")
    part_price = input("Enter Part Price: ")
    # append user input to the 2d list
    inventory.append([part_no, part_name, car_make,car_model,part_Quantity,part_price])
    with open("inventory.csv", 'w', newline="") as CSV:
        writer = csv.writer(CSV, delimiter=',')
        writer.writerows(inventory)
        print("Part Added")
    pass

def update_inventory_item(inventory): # updaye item quantity and/or price
    prt_no = input("Enter Part No to edit:  ")
    # looping through the list, to find the prt no entered
    x = PrettyTable()
    x.field_names = ["PartNo", "PartName", "Make", "Model", "Quantity", "Price"]
    for item in inventory:
        if prt_no==item[0]: # if prt no found
            x.add_row(item)
            print(x)
            update = input(" Enter Quantity to be updated (-/+): \n") # type '-' before the number to cut from the stock
            item[4]= int(item[4]) + int(update) # update quantity attribute in the list
            answer = input("Do You Want To Update The Price? (Y/N)\n")
            if answer in ["y","Y"]: # if the user wants to update the price
                newPrice = input("Enter New Price: ")
                item[5] = newPrice
            else: pass
    with open("inventory.csv", 'w', newline="") as CSV: # save changes to the file.
        writer = csv.writer(CSV, delimiter=',')
        writer.writerows(inventory)
        print("Updated")
    pass

def delete_item(inventory): # remove an item from the list
    prt_no = input("Enter Part No to edit:  ")
    for item in inventory: # search for the part number
        if prt_no == item[0]:
            inventory.remove(item) # Remove the item from the list
            print(item)
            answer = input("Remove and Save? (Y/N) ") # validate with the user
            if answer in ["y","Y"]:
                with open("inventory.csv", 'w', newline="") as CSV: # save cahnges to the file
                    writer = csv.writer(CSV, delimiter=',')
                    writer.writerows(inventory)
                    print("Deleted")
    pass

def total_price_column(inventory): # add total price column to the table and calculate values ( price * Quantity)
    for item in inventory:
        item[5]= format(float(item[5]),".2f")
        total_price = int(item[4])*float(item[5])
        item.append(format(total_price,".2f"))
    return  inventory

def print_inventroy(inventory): # print inventory table
    with open("inventory.csv") as fp: # opening CSV file
        mytable = from_csv(fp) # using prettytable function and creating the ASCII tabel
        print(mytable) # print the table
    pass

def re_oreder_list(inventory):
    x = PrettyTable() # temp list to store items with quantity < 4
    x.field_names = ["PartNo", "PartName", "Make", "Model", "Quantity", "Price"]
    for item in inventory:
        if int(item[4]) < 4: # if quantity is less than 4
            x.add_row(item) # append the item to the Re-Order list
    # print the Re-Order list
    print(x)
    pass

def view_items_less_than_price(inventory):
# gets price from the user
    threshHold = input("Please Enter ThreshHold Price: ")
    x = PrettyTable()  # temp list holding pretty yable and computed data within the threshHold
    x.field_names = ["PartNo", "PartName", "Make", "Model", "Quantity", "Price"]
    for item in inventory:
        # if item price greater than threshhold price
        if float(item[5])>float(threshHold):
            # append it to the items list
            x.add_row(item)
    # print list of items with price less than user input
    print(x)
    pass

def greater_than_average(inventory):
    average = average_fun(inventory) # get the average
    x = PrettyTable()  # temp list holding pretty yable and computed data greater than average
    x.field_names = ["PartNo", "PartName", "Make", "Model", "Quantity", "Price"]
    for item in inventory:
        # search the list/ compare price to the average. if greater, add to the list
        if float(item[5])> float(average):
            x.add_row(item)
    # print list of items with greater than average price
    print(x)
    pass

def inventory_net_worth(inventory): # obtain total sum of all total prices. sum of ( Quantity*Price )
    inventory = total_price_column(inventory) # make sure program is using the list with total price column
    price = 0
    for item in inventory:
        price = price + float(item[6]) # calculate sum per item total price
    price = format(price, ".2f") # format to two decimal points
    return price

def calculate_stocks(inventory):
    x = PrettyTable()
    x.field_names = ["PartNo", "PartName", "Make", "Model", "Quantity", "Price", "Status"]
    average =average_fun(inventory) # call average function and obtain average
    stocks = inventory_net_worth(inventory) # call total inventory function and obtain total stock value
    minimum_quantity = least_quantity(inventory) # find the item with least quantity
    min_price = minimum_price(inventory) # find the item with minimum price
    max_price = maximum_price(inventory) # find the item with maximum price
    x.add_row(max_price) # append reults to a list to for tabulate function
    x.add_row(min_price)
    x.add_row(minimum_quantity)
    print(f"The Average Price is : {average}") # using F-String to print the average
    print(f"The Total Stock Value Is : {stocks}") # using F-String to print stock value
    # Format statistical items into a table
    print(x)
    pass

with open("inventory.csv", 'r') as CSV: # opens inventory in read mode
    data = csv.reader(CSV, delimiter=',') # using CSV reader.
    inventory = []
    for row in data: # reading data and storing them in a 2d list
        inventory.append(row)
    Exit= True #exit Flag
    inventory.pop(0)
    while(Exit):
        # Display menu
        print("****Inventory Control System****")
        print("[1] Add Part")
        print("[2] Update Part")
        print("[3] Remove Part")
        print("[4] Display Inventory")
        print("[5] Display Re-Order List")
        print("[6] Parts Above Given Price")
        print("[7] Parts Above The Average Price")
        print("[8] Stock Statistics")
        print("[9] Exit")
        choice = input("Enter Function Number: ")
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("invalid choice type again")
            continue
        elif choice == "1":
            add_Item(inventory)
        elif choice == "2":
            update_inventory_item(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            print_inventroy(inventory)
        elif choice == "5":
            re_oreder_list(inventory)
        elif choice == "6":
            view_items_less_than_price(inventory)
        elif choice == "7":
            greater_than_average(inventory)
        elif choice == "8":
            calculate_stocks(inventory)
        else:
            Exit= False
