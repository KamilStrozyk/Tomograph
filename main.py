import ttkthemes
import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tomograph")
        self.window.config(bg='#FFFAFA')
        self.window.geometry('1280x720')

        self.style = ThemedStyle(self.window)
        self.style.set_theme("equilux")

        self.main_frame = ttk.Frame(self.window, width = 1280)
        self.main_frame.grid(column=0, row=0)
        self.main_frame.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----

        self.lbl = ttk.Label(self.main_frame, text="Hello")
        # self.lbl.grid(column=0, row=0)
        self.txt = ttk.Entry(self.main_frame,width=10)
        # self.txt.grid(column=1, row=0)
        self.btn = ttk.Button(self.main_frame, text="Click Me", command=self.clicked)
        # self.btn.grid(column=2, row=0)
        self.window.mainloop()

    def clicked(self):
        self.lbl.configure(text="Button was clicked !!")

if __name__ == '__main__':
    app = App()


