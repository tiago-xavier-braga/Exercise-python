from tkinter import *

home_menu = Tk()
home_menu.geometry = ("600x400")
home_menu.minsize(600,400)
home_menu['bg'] = '#2D2F31'
def click_me(mensage):
    print(mensage)

btn = Button(home_menu, text ="Click me", command = lambda: print("UaU"))
btn.pack()

btn2 = Button(home_menu, text ="Click me", command = lambda: click_me("Hello Word!"))
btn2.pack()
home_menu.state("iconic")
home_menu.iconbitmap('icone_3.ico')
home_menu.mainloop()