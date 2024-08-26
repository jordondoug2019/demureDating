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
print(userInput)
#User inputs their budget for the date 
#here, The user budget is automatically converted to a float. This is just in case the user has a budget that isn't a whole number 
#I used a format string to make the code look cleaner and easier to read.  
budgetInput= float(input(f"{userInput} is really lucky! What is the budget?"))
print(budgetInput)

#prints restuarant menu using a nested for loop. The loop goes through each key in the dictionary, 
# and for each key, it iterates over the corresponding values.
# I also added the title of each section of the menu and line breaks to make for a better user experience. 
print(f"Appetizers \n")
for key in seafoodMenu.Menu["AppMenu"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["AppMenu"][key]:
        print (value + "\n") 

print(f"Entrees \n")
for key in seafoodMenu.Menu["Entree"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["Entree"][key]:
        print (value + "\n")

print(f"Dessert \n")
for key in seafoodMenu.Menu["Dessert"]:
    print (key + "\n")
    for value in seafoodMenu.Menu["Dessert"][key]:
        print (value + "\n")