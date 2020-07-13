from tkinter import *

root = Tk()
root.geometry("500x300")
root.maxsize(500,300)
root['bg']= '#2D2F31'
Label(root, text='User:', font="Arial 20", fg = "#ffffff", bg="#2D2F31").grid(row = 0, sticky=W)
Label(root, text='Password: ', font="Arial 20", fg = "#ffffff", bg="#2D2F31",height = "2").grid(row = 1)
text_name = Entry(root,font="Arial 20", fg = "#ffffff", bg="#56595d", border =0).grid(row = 0, column=1,sticky=W)
text_pass = Entry(root,font="Arial 20", fg = "#ffffff", bg="#56595d", border =0).grid(row = 1, column=1,sticky=W)
button = Button(root, text='Login ', font="Arial 20", fg = "#ffffff", bg="#56595d", border = 0).grid(row = 2, column = 1)
root.mainloop()