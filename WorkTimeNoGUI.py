import sys

global it, stop, firstuse, prename, pretime, predue,ib

firstuse = True

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



def itinerary(myarray):
    global stop,prename,pretime,firstuse, predue, it,ib
    print("Welcome to itinerary builder.")
    stop = int(input("Press one to continue, press two to quit."))
    while True:
        while stop != 2:
            while firstuse:
                it = []
                prename = str(input("Enter the name of the work to-do task..."))
                pretime = str(input("Enter how long this will take you..."))
                predue = str(input("Enter the date it is due..."))
                it.append(["Item name:", prename,"Rough time it will take to complete task:", pretime, "Date due:", predue])
                print(it)
                firstuse = False
                itinerary(it)
            name = str(input("Enter the name of the work to-do task..."))
            time = str(input("Enter how long this will take you..."))
            due = str(input("Enter the date it is due..."))
            myarray.append(["Item name:", name, "Rough time it will take to complete task:", time, "Date due:", due])
            print(myarray)
            itinerary(myarray)



def main():
    choice = int(input("Press 1 for salary calculator, press 2 to exit, and press 3 for itinerary."))
    if choice == 1:
        calculator()
    elif choice == 2:
        sys.exit("Thank you!")
    elif choice == 3:
        itinerary(it)
        
main()