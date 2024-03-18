#Joshua Carter
#03/01/2024
#P1HW2
#F-Strings


print ("This program calculates and displays travel expenses")
print ()
#Get budget from user
budget = int(input ("Enter budget: "))
print ()
#Get destination from user
dest = input("Enter your travel destination: ")
print ()
#Get gas expense from user
gas = int(input("How much do you think you will spend on gas? "))
print ()
#Get hotel expense from user
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print ()
#Get food expense from user
food = int(input("Last, how much do you need for food? "))
print ()

print("------------Travel Expenses------------")
print(f'Location: {dest:}')
print(f'Initial Budget: ${budget:.2f}')
print(f'Fuel: ${gas:.2f}')
print(f'Accommodation: ${hotel:.2f}')
print(f'Food: ${food:.2f}')
print("---------------------------------------")

rem = budget - (gas + hotel + food)
print(f'Remaining Balance: ${rem:.2f}')
