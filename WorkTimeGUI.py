from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("WorkTime")

salary_var = tk.StringVar()
starttime_var = tk.StringVar()
endtime_var = tk.StringVar()

def calculator():

    salary = salary_var.get()
    starttime = starttime_var.get()
    endtime = endtime_var.get()

    salary = float(salary)
    starttime = int(starttime)
    endtime = int(endtime)

    formula1 = endtime-starttime
    formula2 = formula1/100
    formula3 = formula2*salary
    rounded = round(formula3,2)
    rounded = str(rounded)
    rounded_label = tk.Label(root, text = "Your salary is $" + rounded).grid(row=4,column=0)

salary_label = tk.Label(root, text = "Per Hour Salary without money sign")
salary_entry = tk.Entry(root, textvariable=salary_var)

starttime_label = tk.Label(root, text = "Start Time for work in military time without colons")
starttime_entry = tk.Entry(root,textvariable=starttime_var)

endtime_label = tk.Label(root,text = "End Time for work in military time without colons")
endtime_entry = tk.Entry(root, textvariable=endtime_var)

btn = tk.Button(root, text="Submit", command = calculator)

salary_label.grid(row = 0, column = 0)
salary_entry.grid(row = 0, column = 1)
starttime_label.grid(row = 1, column = 0)
starttime_entry.grid(row=1,column=1)
endtime_label.grid(row=2,column=0)
endtime_entry.grid(row=2,column=1)
btn.grid(row=3,column=0)

root.mainloop()
