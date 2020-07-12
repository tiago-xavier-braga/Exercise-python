from tkinter import*
home_menu = Tk()
home_menu['bg']= '#2D2F31'
home_menu.geometry("600x400")
label_one = Label(home_menu, 
text="I'm label",
font = "Arial 20",
width = "20",
height = "4",
anchor = CENTER, # S = sul, N = norte, E = leste, W = oeste 
bd = 2,
relief = SOLID
).pack()

home_menu.mainloop()