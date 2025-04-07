import sys
import re

global it, stop, firstuse, prename, pretime, predue,ib, amstart, amend


firstuse = True
amstart = False
amend = False

def calculator():
    salary = float(input('Hello! Please enter your per hour salary here...'))
    startTime = str(input('Enter your starting time in standard 12 hour time without AM or PM.'))
    starting = int(input("Is this AM? 1 for yes, 2 for no."))
    if starting == 1:
        amstart = True
    else:
        amstart = False
    split1 = re.split(":", startTime, 1)
    group1 = split1[0] + split1[1]
    group1 = int(group1)
    if group1 <= 0:
        print("Values out of scope!")
        calculator()
    elif group1 >= 1300:
        print("Values out of scope!")
        calculator()

    endTime = str(input('Enter your ending time in standard 12 hour time without AM or PM.'))
    ending = int(input("Is this AM? 1 for yes, 2 for no."))
    if ending == 1:
        amend = True
    else:
        amend = False
    split2 = re.split(":",endTime,1)
    group2 = split2[0] + split1[1]
    group2 = int(group2)
    if group2 <= 0:
        print("Values out of scope!")
        calculator()
    elif group2 >= 1300:
        print("Values out of scope!")
        calculator()

    if not amstart:
        group1 = 1200 + group1
    elif not amend:
        group2 = 1200 + group2
    time1 = group2 - group1
    time2 = time1/100
    time3 = time2*salary
    rounded = round(time3,2)
    rounded = str(rounded)
    print("Your salary is about " + rounded + " Dollars!")
    main()






def itinerary(myarray):
    global stop,prename,pretime,firstuse, predue, it, ib
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
        print(myarray)
        main()



def main():
    choice = int(input("Press 1 for salary calculator, press 2 to exit, and press 3 for itinerary."))
    if choice == 1:
        calculator()
    elif choice == 2:
        sys.exit("Thank you!")
    elif choice == 3:
        it = []
        itinerary(it)

main()