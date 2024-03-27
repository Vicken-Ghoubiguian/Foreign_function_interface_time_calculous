# Importation of all useful libraries
from tkinter import *
from tkinter import ttk

#
root = Tk()

# Definition of the window's title
root.title("Time calculous")

#
root.iconbitmap('logo.ico')

# Definition of the window's size
root.geometry("1000x700")

# Make the window not resizable
root.resizable(False, False)

#
tabs = ttk.Notebook(root)

#
tabl = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

#
tabs.add(tabl, text="Wished weekday in a choosen month")
tabs.add(tab2, text="Calculations on date and time")
tabs.add(tab3, text="Number of weeks in a year according to the iso norm")

# Later for 'tab1'
l1=ttk.Label(tabl,text="I am tab-1",width=10)
l1.place(relx=0.4,rely=0.2)

# Later for 'tab2'
l2=ttk.Label(tab2,text="I am tab-2",width=10)
l2.place(relx=0.4,rely=0.2)

# Later for 'tab3'
l3=ttk.Label(tab3,text="I am tab-3",width=10)
l3.place(relx=0.4,rely=0.2)

#
tabs.pack(expand=1, fill='both')

#
root.mainloop()
