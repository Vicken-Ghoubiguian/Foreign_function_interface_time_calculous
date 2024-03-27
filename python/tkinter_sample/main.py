#
from tkinter import *
from tkinter import ttk

#
root = Tk()

#
root.title("Time calculous")

#
root.iconbitmap('logo.ico')

#
root.geometry("1000x700")

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

#
tabs.pack(expand=1, fill='both')

#
root.mainloop()
