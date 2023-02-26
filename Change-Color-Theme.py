from tkinter import *
from tkinter import colorchooser

root = Tk()
root.resizable(False,False)
root.geometry("500x400+380+160")
root.title("Change Color Theme")
root.configure(bg="slate grey")

def bgcolor():
    bg_color = colorchooser.askcolor(title="Select Background color to change")
    root.configure(bg=bg_color[1])
    l1.config(bg=bg_color[1])
    background.config(bg=bg_color[1],activebackground=bg_color[1])
    foreground.config(bg=bg_color[1],activebackground=bg_color[1])

def fgcolor():
    fg_color = colorchooser.askcolor(title="Select Foreground color to change")
    l1.config(fg=fg_color[1])
    background.config(fg=fg_color[1],activeforeground=fg_color[1])
    foreground.config(fg=fg_color[1],activeforeground=fg_color[1])

l1 = Label(root,text="Change Color Theme",fg="white",bg="slate grey",font="Monospace 20 bold")
l1.pack(pady=40)

background = Button(root,text="Change Background Color",font="Monospace 15 bold",
                    fg="white",bg="slate grey",bd=4,activebackground="slate grey",
                    activeforeground="white",command=lambda: bgcolor())
background.pack(pady=20)

foreground = Button(root,text="Change Foreground Color",font="Monospace 15 bold",
                    fg="white",bg="slate grey",bd=4,activebackground="slate grey",
                    activeforeground="white",command=lambda: fgcolor())
foreground.pack(pady=20)
root.mainloop() 
