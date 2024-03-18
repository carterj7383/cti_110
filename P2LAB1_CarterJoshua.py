#Joshua Carter
#02/28/2024
#P2LAB1 - Math expressions and f-string

print("---------Calculate the cost to drive 20, 75, & 500 miles---------")
print()
#Get input from user

mpg = float(input("Enter the car's MPG: "))
cost = float(input("Enter the cost per gallon of gas: "))

#Calculate the cost to drive 20, 75, & 500 miles

miles_20 = (20/mpg) * cost
miles_75 = (75/mpg) * cost
miles_500 = (500/mpg) * cost



print()

print(f"The cost to drive 20 miles is ${miles_20:.2f}")
print(f"The cost to drive 75 miles is ${miles_75:.2f}")
print(f"The cost to drive 500 miles is ${miles_500:.2f}")
