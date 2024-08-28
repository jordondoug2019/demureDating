import seafoodMenu
#User inputs who is on the date with them
#User inputs their budget for the date
#Print the restaurant menu (your group created this!) 
#User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
#Script tells the user how much money they have left after each order.
#At the end of the date user must agree to pay the bill and then their final budget is shown to them.


#Welcome Screen 
print("Welcome to Demure Dating!")

#User inputs who is on the date with them
userInput= input("Please enter the name of your date")


#User inputs their budget for the date 

#here, The user budget is automatically converted to a float. This is just in case the user has a budget that isn't a whole number 
#I used a format string to make the code look cleaner and easier to read.  
budgetInput= float(input(f"{userInput} is really lucky! What is the budget?"))


#Print the restaurant menu (your group created this!) 

#prints restuarant menu using a nested for loop. The loop goes through each key in the dictionary, 
# and for each key, it iterates over the corresponding values.
# I also added the title of each section of the menu and line breaks to make for a better user experience. 
print(f"Appetizers \n")
for key in seafoodMenu.Menu["AppMenu"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["AppMenu"][key]:
        print (f"{value} \n") 

print(f"Entrees \n")
for key in seafoodMenu.Menu["Entree"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["Entree"][key]:
        print (f"{value} \n") 

print(f"Dessert \n")
for key in seafoodMenu.Menu["Dessert"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["Dessert"][key]:
        print (f"{value} \n") 


#User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
#Script tells the user how much money they have left after each order.

#Take user menu choice and date menu choice 
#Get corresponding prices for each meal and subtract total from budget 
#Budget - (userChoice + UserDateChoice)
#need conditonals?



userChoice = input("What will you be having for dinner? ")
userDateChoice=input(f"What will {userInput} have for dinner? ")
#created a for loop that iterates over the seafood Menu items. 
#The key variable= key of Menu dictionary(AppMenu, Entree, and Dessert)
#The value variable= Keys of the AppMenu, Entree, and Dessert
#the userChoice and UserDateChoice= the input from user
#If the input is within the Keys of one of the menus(AppMenu, Entree, Dessert,)
# it will 
for key, value in seafoodMenu.Menu.items():
    if userChoice in value:
        print(key)
        print(value)
        userPrice=value[userChoice][0]
        print(userPrice)
    if userDateChoice in value:
        print(value)
        userDatePrice=value[userDateChoice][0]
        print(userDatePrice)
        totalBill= userPrice + userDatePrice
print(totalBill)
remainingBudget= budgetInput - totalBill
print(remainingBudget)
    #make totalbill function def totalbill (userprice, userdateprice 
#Script tells the user how much money they have left after each order.
#totalBill= userPrice + userDatePrice
#print(totalBill)
#At the end of the date user must agree to pay the bill and then their final budget is shown to them.







# Calculate total bill
#total_bill = userPrice + userDatePrice
#remaining_budget = budgetInput - total_bill

# Display the choices, the bill, and the remaining budget

