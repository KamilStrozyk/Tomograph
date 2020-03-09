from tkinter import *


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tomograph")
        self.window.geometry('1280x720')
        
        self.lbl = Label(self.window, text="Hello")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self.window,width=10)
        self.txt.grid(column=1, row=0)
        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.window.mainloop()

    def clicked(self):
        self.lbl.configure(text="Button was clicked !!")

if __name__ == '__main__':
    app = App()


