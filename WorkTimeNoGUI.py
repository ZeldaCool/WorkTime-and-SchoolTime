import sys

global completeitinerary
global completecalculator
global Dict
Dict = {}

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

def itinerarymaker():
    global item, time, dayDue, moneyMade
    firstTime = True
    stop = int(input("Would you like to continue? 1 for yes, 2 for no."))
    counter = 0
    while True:
        if stop == 1:
            if firstTime == True:
                counter += 1
                item = str(input("Enter your item's name..."))
                time = float(input("About how many hours will this take you?"))
                dayDue = str(input("Enter the day it is due..."))
                bonus = int(input("Is there a bonus with completion? 1 for yes, 2 for no"))
                if bonus == 1:
                    moneyMade = str(input("Enter how much the bonus is..."))
                    Dict['To Do'] = {'name': item, 'how long this will take': time, 'Day it needs to be done': dayDue,
                                     'bonus': moneyMade}
                    itinerarymaker()
                else:
                    itinerarymaker()
            else:
                counter += 1
                stop = int(input("Would you like to continue? 1 for yes, 2 for no."))
                item = str(input("Enter your item's name..."))
                time = int(input("About how many hours will this take you?"))
                dayDue = str(input("Enter the day it is due..."))
                bonus = int(input("Is there a bonus with completion? 1 for yes, 2 for no"))
                if bonus == 1:
                    moneyMade = str(input("Enter how much the bonus is..."))
                    countered = str(counter)
                    Dict['To Do' + countered] = {'name': item, 'how long this will take': time, 'Day it needs to be done': dayDue,
                                     'bonus': moneyMade}
                    itinerarymaker()
                else:
                    itinerarymaker()

        else:
            countered = str(counter)
            Dict['To Do' + countered] = {'name': item, 'how long this will take': time, 'Day it needs to be done': dayDue}
            print(Dict)
            main()

def main():
    choice = int(input("Press 1 for itinerary, press 2 for salary calculator, press 3 to exit."))
    if choice == 1:
        itinerarymaker()
    elif choice == 2:
        calculator()
    else:
        sys.exit("Thank you!")


main()