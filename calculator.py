from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "c":
         scvalue.set("")
         screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("420x800")
root.title("calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill= X , ipadx= 8, pady= 10, padx= 10)

f = Frame(root, bg= "grey")
b = Button(f , text="9", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="8", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="7", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

f = Frame(root, bg= "grey")
b = Button(f , text="6", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="5", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="4", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

f = Frame(root, bg= "grey")
b = Button(f , text="3", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="2", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="1", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

f = Frame(root, bg= "grey")
b = Button(f , text="0", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="+", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="-", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

f = Frame(root, bg= "grey")
b = Button(f , text="*", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="/", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="%", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

f = Frame(root, bg= "grey")
b = Button(f , text="=", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18 , pady = 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="c", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side=LEFT, padx= 18 ,  pady= 5)
b.bind("<Button-1>" ,click)

b = Button(f , text="%", font= "lucida 35 bold" , padx= 20 , pady = 18)
b.pack(side = LEFT , padx= 18, pady = 5)
b.bind("<Button-1>" ,click)

f.pack()

root.mainloop()