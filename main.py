import ttkthemes
import tkinter as tk
import matplotlib
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
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
        self.prepareCanvas()

        self.style = ThemedStyle(self.window)
        self.style.set_theme("winnative")
        self.window.mainloop()

    def prepareCanvas(self):
        self.image_canvas_container = self.builder.get_object('image_canvas')
        self.figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.image_canvas = image_canvas = FigureCanvasTkAgg(
            fig, master=self.image_canvas_container)
        image_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.sinogram_canvas_container = self.builder.get_object('sinogram_canvas')
        self.figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.sinogram_canvas = sinogram_canvas = FigureCanvasTkAgg(
            fig, master=self.sinogram_canvas_container)
        sinogram_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.recon_canvas_container = self.builder.get_object('recon_canvas')
        self.figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.recon_canvas = recon_canvas = FigureCanvasTkAgg(
            fig, master=self.recon_canvas_container)
        recon_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def addFile(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
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
