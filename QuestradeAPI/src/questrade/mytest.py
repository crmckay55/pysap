'''
Created on Jan 12, 2017

@author: Chris
'''
from Tkinter import *
from ttk import Treeview


def callback():
    print("called the callback!")



root = Tk()


tree = Treeview(root)
root.wm_state('zoomed')

print(root.maxsize())



# Inserted at the root, program chooses id:
tree["columns"] = ("one","two")
tree.column("one", width=100)
tree.heading("one", text="Column 1")
tree.column("two", width = 100)
tree.heading("two",text="Column 2")
tree.insert('', 'end', 'widgets',text="test item")
tree.insert('widgets','end','test',text='another test')


frame = Frame(width=768, height=576, bg="", colormap="new")
frame.pack()

tree.pack()

statuslabel = Label(root, bd=1, relief=SUNKEN, anchor=W)
statuslabel.config(text='test status bar')
statuslabel.pack(fill=X)


root.update()
mainloop()

