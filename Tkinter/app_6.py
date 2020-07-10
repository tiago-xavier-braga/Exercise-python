from tkinter import *

home_menu = Tk()
home_menu['bg'] = '#2D2F31'
width = 600
height = 400

width_screen = home_menu.winfo_screenwidth()
heigth_screen = home_menu.winfo_screenheight()

centerW = width_screen/2  - width/2
centerH = heigth_screen/2 - height/2
home_menu.geometry("%dx%d+%d+%d"% (width, height,centerW, centerH))
print(width_screen, heigth_screen)
home_menu.iconbitmap("icone_3.ico")
home_menu.mainloop()