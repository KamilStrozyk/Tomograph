import ttkthemes
import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import pygubu


class App:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Interface.ui')

        self.window = builder.get_object('main_window')
        self.window.title("Tomograph")
        self.window.geometry('700x740')

        self.style = ThemedStyle(self.window)
        self.style.set_theme("winnative")
        self.window.mainloop()

    def addFile(self):
        print("XD")
        pass


if __name__ == '__main__':
    app = App()
