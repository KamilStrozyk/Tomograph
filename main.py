import ttkthemes
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
import pygubu

def addFile(self):
    print("XD")
    pass

class App(pygubu.TkApplication):
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Interface.ui')

        self.window = builder.get_object('main_window')
        self.window.title("Tomograph")
        self.window.geometry('700x740')
        self._create_ui()

        self.style = ThemedStyle(self.window)
        self.style.set_theme("winnative")
        self.window.mainloop()

    def addFile(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        pass

    def run(self):
        pass

    def _create_ui(self):
        callbacks = {
            'addFile': self.addFile,
            'run': self.run,
            }
        self.builder.connect_callbacks(callbacks)
        


if __name__ == '__main__':
    app = App()
