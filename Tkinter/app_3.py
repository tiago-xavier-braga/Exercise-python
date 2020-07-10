from tkinter import *

home_menu = Tk()

home_menu.geometry("600x400+200+200")
home_menu.minsize(600,400) # Defines width and height minimus..
#home_menu.maxsize(700,500) Defines width and height max..

home_menu.state("zoomed")#Open in full screen

home_menu.iconbitmap("icone_3.ico")#Defines icone
home_menu.mainloop()