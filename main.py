import ttkthemes
import tkinter as tk
import matplotlib
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
import pygubu
from PIL import ImageTk, Image
import os
import radon
import cv2
import numpy as np
from threading import Thread
import time


def addFile(self):
    print("XD")
    pass


class App(pygubu.TkApplication):
    def __init__(self):
        self.radon = radon.Radon()
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Interface.ui')

        self.window = builder.get_object('main_window')
        self.window.title("Tomograph")
        self.window.geometry('700x740')
        self._create_ui()
        self.prepare_canvas()

        self.alpha = 0.5
        self.span = 90
        self.emmiters_count = 75

        self.style = ThemedStyle(self.window)
        self.style.set_theme("winnative")
        self.window.mainloop()

    def prepare_canvas(self):

        self.image_canvas_container = self.builder.get_object('image_canvas')
        self.image_figure = fig = Figure(
            figsize=(3, 3), dpi=100, facecolor='black')
        self.image_canvas = image_canvas = FigureCanvasTkAgg(
            fig, master=self.image_canvas_container)
        image_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.sinogram_canvas_container = self.builder.get_object(
            'sinogram_canvas')
        self.sinogram_figure = fig = Figure(
            figsize=(3, 3), dpi=100, facecolor='black')
        self.sinogram_canvas = sinogram_canvas = FigureCanvasTkAgg(
            fig, master=self.sinogram_canvas_container)
        sinogram_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.recon_canvas_container = self.builder.get_object('recon_canvas')
        self.recon_figure = fig = Figure(
            figsize=(3, 3), dpi=100, facecolor='black')
        self.recon_canvas = recon_canvas = FigureCanvasTkAgg(
            fig, master=self.recon_canvas_container)
        recon_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def add_file(self):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.image = cv2.imread(filename, 0)
        axim = self.image_figure.add_axes([0, 0, 1, 1], anchor='SW')
        axim.imshow(self.image, aspect='auto', cmap='gray')
        axim.axis('off')
        self.image_canvas.draw()
        pass

    def run(self):
        self.generate_sinogram()
        self.generate_recon()
        pass

    def generate_sinogram(self):
        self.sinogram = np.zeros((int(360/self.alpha), self.emmiters_count))
        axim = self.sinogram_figure.add_axes([0, 0, 1, 1], anchor='SW')
        self.sin_thread = Thread(target=lambda: self.sinogram_thread())
        self.sin_thread.start()
        self.update_sinogram(axim)
        axim.imshow(self.sinogram, aspect='auto',
                     cmap='gray')
        axim.axis('off')
        self.sinogram_canvas.draw()
        pass

    def sinogram_thread(self):
        self.radon.radon_transform(
            image=self.image, sinogram=self.sinogram, alpha=self.alpha, theta=self.span, emmiters_count=self.emmiters_count)
    pass

    def update_sinogram(self, axim):
        if self.sin_thread.is_alive() is True:
            axim.imshow(self.sinogram, aspect='auto', cmap='gray')
            axim.axis('off')
            self.sinogram_canvas.draw()
            self.window.after(50, self.update_sinogram(axim))

    def reconstruction_thread(self):
        self.radon.inverse_radon_transform(
            recon=self.recon, sinogram=self.sinogram, alpha=self.alpha, theta=self.span, emmiters_count=self.emmiters_count)
    pass

    def update_recon(self, axim):
        if self.recon_thread.is_alive() is True:
            axim.imshow(self.recon, aspect='auto', cmap='gray')
            axim.axis('off')
            self.recon_canvas.draw()
            self.window.after(50, self.update_recon(axim))

    def generate_recon(self):
        row, col = self.image.shape
        self.recon = np.zeros((row, col))
        axim = self.recon_figure.add_axes([0, 0, 1, 1], anchor='SW')
        self.recon_thread = Thread(target=lambda: self.reconstruction_thread())
        self.recon_thread.start()

        self.update_recon(axim)
        # time.sleep(10)
        axim.imshow(self.recon, aspect='auto', cmap='gray')
        axim.axis('off')
        self.recon_canvas.draw()
        pass

    def _create_ui(self):
        callbacks = {
            'addFile': self.add_file,
            'run': self.run,
        }
        self.builder.connect_callbacks(callbacks)


if __name__ == '__main__':
    app = App()
