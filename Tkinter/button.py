from tkinter import *
home_menu = Tk()
home_menu.geometry("600x400")
#background color
home_menu['bg']= '#2D2F31'
#button
btn = Button(home_menu, text="click me")
#background button 
btn['bg'] = '#645B5C'
#Put the button on the screen
btn.pack()

home_menu.iconbitmap('icone_3.ico')
home_menu.mainloop()