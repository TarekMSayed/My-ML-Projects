# Simple enough, just import everything from tkinter.
from tkinter import *


#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


    def showImg(self):
        path = filedialog.askopenfilename()
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()



# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")
btn = Button(root, text="Select an image", command=showImg)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
