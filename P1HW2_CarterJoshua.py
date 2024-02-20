#Joshua Carter
#02/19/2024
#P1HW2
#Using IDLE to create and test a program

print ("This program calculates and displays travel expenses")

#Get budget from user
budget = int(input ("Enter budget: "))

#Get destination from user
dest = input ("Enter your travel destination: ")

#Get gas expense from user
gas = int(input ("How much do you think you will spend on gas? "))

#Get hotel expense from user
hotel = int(input ("Approximately, how much will you need for accomodation/hotel? "))

#Get food expense from user
food = int(input ("Last, how much do you need for food? "))

print ("------------Travel Expenses------------")

print("Location: ", dest)
print ("Initial Budget: ", budget)

print ("Fuel: ", gas)
print ("Accomodation: ", hotel)

print ("Food: ", food)

rem = budget - (gas + hotel + food)

print ("Remaining Balance: ", rem)







