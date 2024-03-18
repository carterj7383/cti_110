#Joshua Carter
#02/28/2024
#P2LAB2 - Math expressions and f-strings

#Get info from user

num1 = float(input("Enter your float: "))
num2 = float(input("Enter your float: "))
num3 = float(input("Enter your float: "))
num4 = float(input("Enter your float: "))

#Calculate the product
product = num1 * num2 * num3 * num4

#Calculate the average
avg = (num1 + num2 + num3 + num4) / 4

print()
print()

#Output with no decimal 

print(f'The product of the number is {product:.0f}.')
print(f'The average of the numbers are {avg:.0f}.')

print()
print()

#Output with three decimal places

print(f'The product of the number is {product:.3f}.')
print(f'The average of the numbers are {avg:.3f}.')
