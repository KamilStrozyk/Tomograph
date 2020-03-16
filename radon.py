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
import cv2
import numpy as np
from math import *


class Radon:
    def __init__(self):
        pass

    def radon_transform(self, image: np.ndarray, alpha=0.5, emmiters_count=10, theta=5):
        self.image = image
        row, col = image.shape
        center = {"x": row//2, "y": col//2}
        corner = {"x": row, "y": col}
        r = sqrt((center["x"] - corner["x"])**2 +
                 (center["y"] - corner["y"])**2)

        E = [int(r * cos(alpha)), int(r*sin(alpha))]
        D = []

        for i in range(emmiters_count):
            if i == 0:
                x = r*cos(alpha + pi - theta/2)
                y = r*sin(alpha + pi - theta/2)
            elif i == emmiters_count-1:
                x = r*cos(alpha + pi + theta/2)
                y = r*sin(alpha + pi + theta/2)
            else:
                x = r*cos(alpha + pi - theta/2 + i * theta/(emmiters_count-1))
                y = r*sin(alpha + pi - theta/2 + i * theta/(emmiters_count-1))
            D.append([row//2 + int(x), col//2 + int(y)])

        res = []
        for d in D:
            res.append(self.bresenham_line(E[0], E[1], d[0], d[1]))
        return image

    def bresenham_line(self, x1, y1, x2, y2):
        coords = []
        x = x1
        y = y1
        if (x1 < x2):
            xi = 1
            dx = x2 - x1
        else:
            xi = -1
            dx = x1 - x2
        if (y1 < y2):
            yi = 1
            dy = y2 - y1
        else:
            yi = -1
            dy = y1 - y2
        # pierwszy piksel
        coords.append(self.pixel_value_if_exist(x, y))

        if (dx > dy):
            ai = (dy - dx) * 2
            bi = dy * 2
            d = bi - dx
            while (x != x2):
                if (d >= 0):
                    x += xi
                    y += yi
                    d += ai
                else:
                    d += bi
                    x += xi
                coords.append(
                    self.pixel_value_if_exist(x, y))

        else:

            ai = (dx - dy) * 2
            bi = dx * 2
            d = bi - dy
            while (y != y2):

                if (d >= 0):
                    x += xi
                    y += yi
                    d += ai

                else:

                    d += bi
                    y += yi
                coords.append(
                    self.pixel_value_if_exist(x, y))
        print(coords)
        return coords

    def pixel_value_if_exist(self, x, y):
        try:
            res = self.image[x, y]
        except:
            res = 0
        return res

    def inverse_radon_transform(sinogram):
        pass
