import getpass
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
welcome = """
************************************************************
*                                                          *
*             Welcome to the AUCTION!                      *
*                                                          *
************************************************************
"""
print(welcome)
biderarr=[]
bidarr=[]
count=0
id=0
bid=0
end=0
print("item Description: WOODEN CHAIR")
print("Base Price: 500")
print("###########################################################")
base=500
while end != "y":
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
      count=count+1
   #b_no = int(input("Enter your buyer ID: "))
    #id=int(input("Enter your buyer ID: "))
      if login_no in biderarr:
          print("bid already present for the given id")
          continue
      else:
          biderarr.insert(count,login_no)
          bid = int(getpass.getpass("Enter your bid: "))
          if bid<base:
              print("price less than base")
          else:
              bidarr.insert(count,bid)
              print("Bid recorded")
              print("############################################################")
  else:
    print("invalid choice")
  if  (choice=="n"):
    end= input("END AUCTION? (y/n)")
    print("################ BIDDING ENDS ##############################")
if (end=="y"):
  maximum=0
  max2=0
  value=base
  for i,value in enumerate(bidarr):
    if value>maximum:
        maximum=value
        index=i
  
  num=bidarr
  num.remove(max(num))
  print("the auction is won by buyer with ID",biderarr[index],"at a price",max(num)+1)
  end = """
************************************************************
*                                                          *
*         End of AUCTION! Thank you for coming!!           *
*                                                          *
************************************************************
"""
print(end)
