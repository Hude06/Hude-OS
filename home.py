# Write your code here :-)
# Write your code here :-)
import tkinter as tk
import os
from tkinter import *
def donothing():
    print("itwoooooorks")

def openclock():
    print("open clock")

def caulc():
     os.system('python3 /Users/hude/Desktop/"HUDE OS"/caulk.py')
def terminal():
     os.system('python3 /Users/hude/Desktop/"HUDE OS/terminal.py"')

root = Tk()
menubar = Menu(root)
clockmenu = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Edit", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)



filemenu.add_command(label="Game", command=openclock)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)

clockmenu = Menu(menubar, tearoff=0)
clockmenu.add_separator()
clockmenu.add_command(label="clock", command=root.quit)
clockmenu.add_command(label="calculater", command=caulc)
clockmenu.add_command(label="terminal", command=terminal)




menubar.add_cascade(label="App's", menu=clockmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

content= Label(root, font = ('calibri', 40, 'bold'),
			background = 'red',
			foreground = 'white',
            text = "WELCOME to Hude OS")
content.configure(width=500, height=300)
w = tk.Tk()
content.pack(anchor = 'center')








root.config(menu=menubar)
root.mainloop()

# Write your code here :-)


# By @Jude hill

# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to
# display time on the label
def time():
	string = strftime('%I:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive

lbl = Label(root, font = ('calibri', 40, 'bold'),
			background = 'purple',
			foreground = 'black')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()



root.config(menu=menubar)
root.mainloop()








# Write your code here :-)
