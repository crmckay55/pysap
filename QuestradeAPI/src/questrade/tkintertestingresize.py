'''
Created on Jan 21, 2017

@author: Chris
'''

from Tkinter import *



class IntroScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        #self.title('Intro Screen')
        self.create_widgets()
        self.focus_force()

    def create_widgets(self):
        label = Label(self, text='Hello World!')
        label.grid()

        button = Button(self, text='Open Window', command=self.newWindow)
        button.grid()

    def newWindow(self):
        self.toplevel = InfoWindow()

#Like the frame, or any widget, this inherited from the parent widget
class InfoWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.grid()
        self.create_widgets()
        self.focus_force()

    def create_widgets(self):
        label = Label(self, text='This is a window!')
        label.grid()

root = Tk()
app = IntroScreen(root)
root.mainloop()