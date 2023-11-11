from tkinter import *
from PIL import ImageTk, Image
import time



loop = 1


while loop == 1:
    win = Tk()
    win.geometry("100x150")
    win.title("BEANS")
    
#varibles 
    
    beans_num = Entry(win).grid(row=3)


#beans image
    beans = Image.open("images/beans.png").resize((200,200))
    beans_pic = ImageTk.PhotoImage(beans)
    
    
#labels
    beans_lbl = Label(win, image=beans_pic, width=100, height=100).grid(row=4)
    
  
   
#functions
    
    def delete_beans():
       top2 = Toplevel(win,)
       del_beans_lbl = Label(top2, text="MORE BEANS FOR YOU!!!", padx=10, pady=10, font=15, bg="#fff", fg="#f00").pack()
       more_beans()
       top2.mainloop()

      
    #opens 10k windows of beans
    def more_beans():
       for i in range():
         top = Toplevel(height=200, width=200)
         top.title("BEANS")
         lbl = Label(top, image=beans_pic).pack()
         


#create buttons
    b1 = Button(win, text="Delete Beans", command=delete_beans).grid(row=2)
    b2 = Button(win, text="CLICK FOR BEANS", command=more_beans).grid(row=1)
    
    
    print(beans_num)
    
    win.mainloop()



    
    