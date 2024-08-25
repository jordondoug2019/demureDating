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

#print(seafoodMenu.Menu["AppMenu"]["Name"][0][2])
#[print(f"{key}: {value}") for key, value in seafoodMenu.Menu.items("AppMenu")]
for key in seafoodMenu.Menu["AppMenu"]:
    print (key)
    for value in seafoodMenu.Menu["AppMenu"][key]:
        print (value)
