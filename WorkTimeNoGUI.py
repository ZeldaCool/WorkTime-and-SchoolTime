import sys
import re
from os.path import split

global it, stop, firstuse, prename, pretime, predue,ib, amstart, amend


firstuse = True
amstart = False
amend = False

def calculator():
    salary = float(input('Hello! Please enter your per hour salary here...'))
    startTime = str(input('Enter your starting time in standard 12 hour time! Make sure to add AM or PM!'))
    split1 = re.split(":",startTime,1)
    group1 = split1[0] + split1[1]
    if group1 <= 0:
        print("Values out of scope!")
        calculator()
    elif group1 >= 1300:
        print("Values out of scope!")
        calculator()
    search1 = re.search("AM", startTime)
    if search1.group() == "AM":
        amstart = True
    else:
        amstart = False
    endTime = str(input('Enter your ending time in standard 12 hour time! Make sure to add AM or PM!'))
    split2 = re.split(":",endTime,1)
    search2 = re.search("AM", endTime)
    if search2.group() == "AM":
        amend = True
    else:
        amend = False
    group2 = split2[0] + split1[1]
    if group2 <= 0:
        print("Values out of scope!")
        calculator()
    elif group2 >= 1300:
        print("Values out of scope!")
        calculator()

    if amstart == False:
        group1 = 1200 + group1
    elif amend == False:
        group2 = 1200 + group2
    time1 = group2 - group1
    time2 = time1/100
    time3 = time2*salary
    rounded = round(time3,2)
    print(rounded)
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