from tkinter import*

home_menu = Tk()
home_menu['bg'] = '#2D2F31'
border = 15
label_one = Label(home_menu, 
            text ="I'm label one\nNot man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "solid").pack()
label_one = Label(home_menu, 
            text ="Not man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "groove").pack()
label_one = Label(home_menu, 
            text ="Not man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "flat").pack()
label_one = Label(home_menu, 
            text ="Not man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "raised").pack()
label_one = Label(home_menu, 
            text ="Not man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "sunken").pack()
label_one = Label(home_menu, 
            text ="Not man, I'm label one",
            font = "Arial 20",
            bd = border,
            relief = "ridge").pack()

home_menu.mainloop()