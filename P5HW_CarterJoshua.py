#Joshua Carter
#4/26/2024
#P5HW 
#Importing random numbers to add and subtract using loops and functions


import random

#setting random numbers from 1-500
def randonums():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

#addition functon
def addnums():
    num1, num2 = randonums()
    correctanswr = num1 + num2
    numguess = 0
    while True:
        useranswr = int(input(f'{num1} + {num2}\nEnter answer.: '))
        numguess += 1
        if useranswr < correctanswr:
            print('Sorry, guess is too low.')
            print('Try again: ')
            print()
        elif useranswr > correctanswr:
            print('Sorry, guess is too high.')
            print('Try again: ')
            print()
        else:
            print(f'Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses:', numguess)
            print()
            break
        
#subtraction function
def subnums():
    num1, num2 = randonums()
    correctanswr = num1 - num2
    numguess = 0
    while True:
        useranswr = int(input(f'{num1} - {num2}\nEnter answer.: '))
        numguess += 1
        if useranswr < correctanswr:
            print('Sorry, guess is too low.')
            print('Try again: ')
            print()
        elif useranswr > correctanswr:
            print('Sorry, guess is too high.')
            print('Try again: ')
            print()
        else:
            print(f'Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses:', numguess)
            print()
            break
        
#main function
def main():
    while True:
        print('Welcome to Math Quiz')
        print()
        print()
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        print()
        choice = input(f'Please choose one of the menu options: ')
        if choice == '1':
            addnums()
        elif choice == '2':
            subnums()
        elif choice == '3':
            print('Thank you for playing...')
            print('Bye!!')
            break
        else:
            print('ERROR!!! Please enter 1, 2, or 3.')
            print()

main()
