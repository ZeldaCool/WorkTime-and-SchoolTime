import sys

global name,stop,grade,it,stopp, gradename

class Itinerary:
    def __init__(self,taskname,timetaken,duedate,timetostart):
        self.taskname = taskname
        self.timetaken = timetaken
        self.duedate = duedate
        self.timetostart= timetostart
def main():
    start = int(input("Press 1 for itinerary, 2 for grades, and 3 to exit."))
    if start == 1:
        itt = []
        itinerary(itt)
    elif start == 2:
        it = []
        gradecalculator(it)
    else:
        sys.exit("Thank You!")
def gradecalculator(array):
    #Add multiple grade entries for each class, avg it out
        while True:
            stop = int(input("Press one to continue, and two to quit."))
            if stop != 2:
                name = str(input("Enter the name of the class..."))
                gradename = str(input("Enter the name of your grade's standard/assignment here..."))
                grade = float(input("Enter the grade on a 4 point scale here..."))
                array.append(["Class name: ",name,"Grade name: ",gradename,"Grade: ",grade])
                print(array)
            if stop == 2:
                main()
def itinerary(myarray):
    global firstuse
    while True:
        stop = int(input('Press 1 to continue, press 2 to quit.'))
        while stop != 2:
            name = str(input("Enter the name of the work to-do task..."))
            time = str(input("Enter how long this will take you..."))
            due = str(input("Enter the date it is due..."))
            timestart = str(input("Enter the time you need to start the task..."))

            myarray.extend([Itinerary(name, time, due, timestart)])
            for obj in myarray:
                print("Task", obj.taskname, "How Long It Will Take", obj.timetaken, "Due", obj.duedate, "What Time To Begin", obj.timetostart, sep=', ')
            itinerary(myarray)
        for obj in myarray:
            print("Task", obj.taskname, "How Long It Will Take", obj.timetaken, "Due", obj.duedate,"What Time To Begin", obj.timetostart, sep=', ')

main()