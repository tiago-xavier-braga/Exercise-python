from tkinter import*

home_menu = Tk()

home_menu.geometry("600x400")
home_menu['bg']= '#2D2F31'

def click():
    label_one['text'] = "I'm variable"
    for item in label_one.keys():
        print(item,":",label_one[item]) 
        
text = StringVar()
text.set("Click")
btn = Button(home_menu, 
textvariable =text, 
command= lambda:click(),
font = "Arial 20",
padx = 40,
pady = 40
).pack()

label_one= Label(home_menu,
font = "Arial 20",
padx = 40,
pady = 40,
justify = LEFT,
fg = "#ffffff",
bg = '#2D2F31',
text= "Click")
label_one.pack()

home_menu.mainloop()