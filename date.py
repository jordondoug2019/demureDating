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

#Created a function that takes the input of the user and their date. 
#I used a while loop to continue accepting answers until a valid choice matched the Seafood Menu
#The for loop was used to iterate over the seafood menu and find the menu item that corresponded with the user Input
#Returns the menu choice
def get_choice(choice_prompt):
    while True:
        choice = input(choice_prompt)
        for category, items in seafoodMenu.Menu.items():
            if choice in items:
                return choice, items[choice][0]  # Returning the item name and its price
        print("Invalid choice, please select a valid menu item.")


#Assigned Function to get USer Choice
userChoice,userPrice= get_choice("What will you be having for dinner? ")
userDateChoice, userDatePrice=get_choice(f"What will {userInput} be having for dinner? ")
#Assigned function to userPrice and userDatePrice variable. The function took the parameters: The dictionary and user Input choice


# Get choices and prices for both user and their date
#The function get_choice is assigned to both Choices and Prices. 
#In one line of code, it will retrieve the users choice from the menu and its price
#userChoice, userPrice = get_choice("What will you be having for dinner? ")
#userDateChoice, userDatePrice = get_choice(f"What will {userInput} be having for dinner? ")

# Calculate total bill
total_bill = userPrice + userDatePrice
remaining_budget = budgetInput - total_bill

# Display the choices, the bill, and the remaining budget
print(f"\nYou ordered: {userChoice} - ${userPrice:.2f}")
print(f"{userInput} ordered: {userDateChoice} - ${userDatePrice:.2f}")
print(f"Your total bill is: ${total_bill:.2f}")
billAgreement=input(f"Do you agree to pay the bill? y/n?")
if billAgreement=="y":
    print(f"Remaining budget: ${remaining_budget:.2f}\n")
elif billAgreement== "n":
    print(f"It's Time to wash the dishes")
