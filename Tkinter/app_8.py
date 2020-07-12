from tkinter import *
home_menu = Tk()
home_menu['bg']= '#2D2F31'
label_1 = Label(home_menu, text="I'm label !", font="Arial 40",width = 20)
label_1.pack()
home_menu.iconbitmap = "icone_3.ico"
home_menu.mainloop()