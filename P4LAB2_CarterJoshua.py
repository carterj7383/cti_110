#Joshua Carter
#03/27/24
#P4LAB2
#10.17 LAB: Output range with increment of 5


var1 = int(input("Enter the smallest number: "))
var2 = int(input("Enter the largest number: "))

#While var1 is larger, allow the user to re-enter the values

while var1 >= var2:
    print("Second integer can't be less than the first.")
    var1 = int(input("Enter the smallest number: "))
    var2 = int(input("Enter the largest number: "))

#While loop broken, vales entered correctly.
    
for num in range(var1, var2+1, 5):
    print(num, end =" ")

#end =" " to print on same line
