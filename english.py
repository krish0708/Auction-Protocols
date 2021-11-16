welcome = """
************************************************************
*                                                          *
*         Welcome to the ENGLISH AUCTION!                  *
*                                                          *
************************************************************
"""
print(welcome)
number_of_bids = 0
count = 0
item_no = 0
sold_items = 0
less_than_reserve = 0
zero_bids_items = 0
min_items = 2
bidarr=[]
while True:
    try:
        n = int(input("Enter the number of items available in the auction: "))
        if n < min_items:
            raise ValueError
    except ValueError:
        print ("Number of items have to be at least",+ min_items)
    else:
        current_highest_bid = [0.0]*n
        item_bids = [0]*n
        item_description = []*n
        reserve_price = []*n
        item_numbers = []*n
        buyer_no_Array = [0]*n
        break
    #TASK 1

for i in range(n):
    item_no = item_no + 1
    item_numbers.append(item_no)
    print ("ENTER DETAILS FOR ITEM NO.", item_no)
    description = input("Enter description for item no. " + str(item_no))
    item_description.append(description)
    reserve = float(input("Enter reserve price for item no. " + str(item_no)))
    reserve_price.append(reserve)
    print("#################################################################")
def Register():
  global buyer_no
  global password
  buyer_no = input("Username/buyer_no: ")
  password = input("Password: ")

  f = open("userinfo.txt", "a")
  f.write("--------------------")
  f.write("\n%s information:\n"%(buyer_no))
  f.write("%s \n"%(buyer_no))
  f.write("%s \n"%(password))
  f.write("--------------------")
def Login():
  global buyer_no
  global password
  f = open("userinfo.txt", "r")
  f.readline()
  f.readline()
  buyer_no = f.readline()
  password = f.readline()
  f.readline()
  return buyer_no
  return password
def CheckLogin():
    global buyer_no
    global password
    global login_no
    global loginpassword

    if (login_no == buyer_no , loginpassword == password):
      print("You´ve logged in sucesfully")

    elif (login_no == buyer_no , loginpassword != password):
      print("Wrong password")

    elif login_no != buyer_no and loginpassword == password:
        print("Wrong username")

    elif login_no != buyer_no and loginpassword != password:
        print("Wrong login information, restart the program and register to create an account")

    else:
        print("ERROR: Uknown error")
while count != "y":
    for i in range(n):
        print ("Item number:", item_numbers[i], "Description:", item_description[i], "Reserve price:", reserve_price[i])#, end = " ")
        print ("Current highest bid:", current_highest_bid[i], "No. of bids:", item_bids[i])#, end = " ") 
        print ("Buyer with highest bid:", buyer_no_Array[i])
        print("###########################################################")   

    choice = input("Do you want to bid for items in this auction? (y/n): ")

    if (choice == "y"):
        reg=input("are you registered? y to continue and n to register")
        if reg=='n':
            Register()
        elif reg=='y':
            print("--------LOGIN--------")
            login_no = input("Username: ")
            loginpassword = input("Password: ")
            Login()
            CheckLogin()
            
        
        item_choice = int(input("Enter the item number for your choice of item: "))
        if item_choice in item_numbers:
            index = item_numbers.index(item_choice)    
            while True:
                try:
                    bid_price = float(input("Please enter your bid: "))
                    if (bid_price <= current_highest_bid[index]):
                        raise ValueError
                except ValueError:
                    print ("Bid should be higher than the current highest bid!")
                else:
                    current_highest_bid[index] = bid_price
                    number_of_bids = int(item_bids[index]) + 1
                    item_bids[index] = number_of_bids
                    print ("Bids for", item_description[index], "are:", item_bids[index])
                    buyer_no_Array[index] = buyer_no
                    print("##############################################################")
                    break
        else: 
            print ("Invalid item code!") 
    elif (choice == "n"):
        count = input("END THE AUCTION? Enter 'n' to continue bidding or 'y' to end the auction: ")
#TASK 3
if (count == "y"):
    sold = False
    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] >= reserve_price[i]):
            sold = True
            sold_items = sold_items + 1
            print("item",item_numbers[i],"sold at",current_highest_bid[i],"to buyer with id",buyer_no_Array[i])
            print("#############################################################################")

    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] < reserve_price[i]):
            less_than_reserve = less_than_reserve + 1
            print ("Item code", item_numbers[i], "has not reached the reserve price.")
            print("#############################################################################")


    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] == 0):
            zero_bids_items = zero_bids_items + 1
            print ("Item code", item_numbers[i], "has not received any bids.")
            print("#############################################################################")

    print ("Number of items sold are:", sold_items)
    print ("Number of items that did not meet the reserve price are:" , less_than_reserve)
    print ("Number of items with no bids are:", zero_bids_items)
else:
    print ("Invalid input!")


