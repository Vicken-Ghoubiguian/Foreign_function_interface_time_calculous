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
root.geometry("500x500")

#
tabs = ttk.Notebook(root)

#
tabl = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)
tab4 = ttk.Frame(tabs)
tab5 = ttk.Frame(tabs)

#
tabs.add(tabl, text="....1....")
tabs.add(tab2, text="....2....")
tabs.add(tab3, text="....3....")
tabs.add(tab4, text="....4....")
tabs.add(tab5, text="....5....")

#
tabs.pack(expand=1, fill='both')

#
root.mainloop()
