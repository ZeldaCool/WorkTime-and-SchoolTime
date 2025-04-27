from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

global it,task,timetaken,due, Itinerary

class Itinerary:
    def __init__(self,taskname,timetaken,duedate,timetostart):
        self.taskname = taskname
        self.timetakenname = timetaken
        self.duedate = duedate
        self.timetostart= timetostart
root = tk.Tk()
root.title("WorkTime Salary Calculator")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Salary Calculator')
tabControl.add(tab2, text='Itinerary Maker')
tabControl.pack(expand=1, fill="both")


salary_var = tk.StringVar()
starttime_var = tk.StringVar()
endtime_var = tk.StringVar()

def calculator():

    salary = salary_var.get()
    starttime = starttime_var.get()
    endtime = endtime_var.get()

    split1 = re.split(":", starttime, 1)
    starttime = split1[0] + split1[1]
    split2 = re.split(":", endtime, 1)
    endtime = split2[0] + split2[1]

    salary = float(salary)
    starttime = int(starttime)
    endtime = int(endtime)
    formula1 = endtime-starttime
    formula2 = formula1/100
    formula3 = formula2*salary
    rounded = round(formula3,2)
    rounded = str(rounded)
    rounded_label = tk.Label(tab1, text = "Your salary is about $" + rounded).grid(row=4,column=0)

salary_label = tk.Label(tab1, text = "Per Hour Salary without money sign")
salary_entry = tk.Entry(tab1, textvariable=salary_var)

starttime_label = tk.Label(tab1, text = "Start Time for work in military time")
starttime_entry = tk.Entry(tab1,textvariable=starttime_var)

endtime_label = tk.Label(tab1,text = "End Time for work in military time")
endtime_entry = tk.Entry(tab1, textvariable=endtime_var)

btn = tk.Button(tab1, text="Submit", command = calculator)

salary_label.grid(row = 0, column = 0)
salary_entry.grid(row = 0, column = 1)
starttime_label.grid(row = 1, column = 0)
starttime_entry.grid(row=1,column=1)
endtime_label.grid(row=2,column=0)
endtime_entry.grid(row=2,column=1)
btn.grid(row=3,column=0)

task_var = tk.StringVar()
timetaken_var = tk.StringVar()
due_var = tk.StringVar()
timestart_var = tk.StringVar()
def itinerary(myArray,task,timetaken,due,timestart):
    myArray.extend([Itinerary(task, timetaken, due,timestart)])
    r=5
    c=0
    for obj in myArray:
        printer = tk.Label(tab2, text ="Task "+obj.taskname+" How Long It Will Take "+obj.timetakenname+" Due: "+obj.duedate+" What Time To Begin "+obj.timetostart).grid(row = r, column = c)
        r+=1


it = []
def itinerary_starter():
    firstUse = True
    global it
    task = task_var.get()
    timetaken = timetaken_var.get()
    due = due_var.get()
    timestart = timestart_var.get()
    itinerary(it,task,timetaken,due,timestart)
task_label = tk.Label(tab2, text = "Name of task to complete")
task_entry = tk.Entry(tab2, textvariable=task_var)

timetaken_label = tk.Label(tab2, text = "How long will this take you?")
timetaken_entry = tk.Entry(tab2, textvariable=timetaken_var)

due_label = tk.Label(tab2, text = "When is it due?")
due_entry = tk.Entry(tab2, textvariable=due_var)

timestart_label = tk.Label(tab2, text = "What time do you need to start?")
timestart_entry = tk.Entry(tab2, textvariable=timestart_var)

task = task_var.get()
timetaken = timetaken_var.get()
due = due_var.get()
timestart = timestart_var.get()
btnii = tk.Button(tab2, text = "Submit", command = itinerary_starter)

task_label.grid(row = 0, column = 0)
task_entry.grid(row = 0, column = 1)
timetaken_label.grid(row = 1, column = 0)
timetaken_entry.grid(row=1,column=1)
due_label.grid(row=2,column=0)
due_entry.grid(row=2,column=1)
timestart_label.grid(row=3,column=0)
timestart_entry.grid(row=3,column=1)
btnii.grid(row=4,column=0)
root.mainloop()
