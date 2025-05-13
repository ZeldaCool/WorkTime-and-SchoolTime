import tkinter as tk
from tkinter import ttk
import re
global ittt, classname,gradetitle,grade
ittt = []
root = tk.Tk()
root.title("SchoolTime")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Grade Calculator')
tabControl.add(tab2, text='Itinerary Maker')
tabControl.pack(expand=1, fill="both")

classname_var = tk.StringVar()
gradetitle_var = tk.StringVar()
grade_var = tk.StringVar()

classname_label=tk.Label(tab1, text = "Enter the name of your class here:")
classname_entry=tk.Entry(tab1, textvariable=classname_var)

gradetitle_label=tk.Label(tab1, text = "Enter the name of your grade's standard/assignment here:")
gradetitle_entry=tk.Entry(tab1, textvariable=gradetitle_var)

grade_label=tk.Label(tab1, text = "Enter your grade on a 4 point scale:")
grade_entry=tk.Entry(tab1, textvariable=grade_var)
def gradecalculator(array, cn, gt, g):
    #Avg out grades, create a new button to avg
    array.append(["Class Name: ", cn, "Grade Standard/Name: ", gt, "Grade: ", g])
    y = len(array)
    r = 6
    c = 0
    n = 0
    while y != 0:
        printer = tk.Label(tab1,text="Class Name: "+array[n][1]+" Grade Standard/Name: "+array[n][3]+" Grade:"+array[n][5]).grid(row = r, column = c)
        r += 1
        y -= 1
        n+=1
def gradecalculator_starter():
    classname = classname_var.get()
    gradetitle = gradetitle_var.get()
    grade = grade_var.get()
    gradecalculator(ittt,classname,gradetitle,grade)

btnn = tk.Button(tab1,text = "Submit", command = gradecalculator_starter)

classname_label.grid(row=1,column=0)
classname_entry.grid(row=1,column=1)

gradetitle_label.grid(row=2,column=0)
gradetitle_entry.grid(row=2,column=1)

grade_label.grid(row=3,column=0)
grade_entry.grid(row=3,column=1)

btnn.grid(row=4,column=0)


root.mainloop()