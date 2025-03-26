import sys



def calculator():
    salary = float(input('Hello! Please enter your per hour salary here...'))
    if salary <= 0:
        print("Error! Values out of scope!")
        calculator()
    startTime = int(input('Enter your starting time in military time without colons!'))
    if startTime <= 0:
        print("Error! Values out of scope!")
        calculator()
    elif startTime >= 2400:
        print("Error! Values out of scope!")
        calculator()
    endTime = int(input('Enter your ending time in military time without colons!'))
    if endTime <= 0:
        print("Error! Values out of scope!")
        calculator()
    elif startTime >= 2400:
        print("Error! Values out of scope!")
        calculator()
    formula1 = endTime - startTime
    if formula1 <= 0:
        print("Error! Values out of scope!")
        calculator()
    elif formula1 >= 2400:
        print("Error! Values out of scope!")
        calculator()
    formula2 = formula1 / 60
    formula3 = formula2 * salary
    rounder = round(formula3, 2)
    print("Your salary is about...")
    print(rounder)
    print("Dollars!")
    main()


                 

def main():
    choice = int(input("Press 1 for salary calculator, press 2 to exit."))
    if choice == 1:
        calculator()
    elif choice == 2:
        sys.exit("Thank you!")


main()