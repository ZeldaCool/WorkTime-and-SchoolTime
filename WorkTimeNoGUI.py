import sys
import re
#Use Class Instead of Array for Itinerary

global it, stop, firstuse, prename, pretime, predue,ib, amstart, amend, Itinerary



firstuse = True
amstart = False
amend = False

class Itinerary:
    def __init__(self,taskname,timetaken,duedate):
        self.taskname = taskname
        self.timetaken = timetaken
        self.duedate = duedate
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
    global firstuse
    while True:
        stop = int(input('Press 1 to continue, press 2 to quit.'))
        while stop != 2:
            name = str(input("Enter the name of the work to-do task..."))
            time = str(input("Enter how long this will take you..."))
            due = str(input("Enter the date it is due..."))
            myarray.extend([Itinerary(name, time, due)])

            for obj in myarray:
                print("Task", obj.taskname, "How Long It Will Take", obj.timetaken, "Due:", obj.duedate, sep=', ')
            itinerary(myarray)
        for obj in myarray:
            print("Task:", obj.taskname, "How Long It Will Take:", obj.timetaken, "Due:", obj.duedate, sep=' ')



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