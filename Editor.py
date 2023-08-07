#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()
top=Frame(win)
top.pack(side=TOP)

#Set the geometry of Tkinter frame
win.geometry("550x550")

def display_text():
   global fColor, entry1
   string= fColor.get()
   string1=entry1.get()
   #label.configure(text=string, fg=string)
   text.configure( fg=string, bg=string1)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack(in_=top, side=TOP)


#Create an Entry widget to accept User Input
fColor= Entry(win, width= 10)
fColor.focus_set()
fColor.pack(in_=top, side=TOP )

#eXperiment 

#Initialize a Label to display the User Input
label1=Label(win, text="", font=("Courier 22 bold"))
label1.pack(in_=top, side=TOP)


#Create an Entry widget to accept User Input
entry1= Entry(win,fg="blue", width=10)
entry1.focus_set()
entry1.pack(in_=top, side=TOP)

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 10, command= display_text).pack()

#create teYt
text=Text(win, fg="red")
text.focus_set()
text.pack()


win.mainloop()
