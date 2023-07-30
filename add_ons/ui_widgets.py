import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy, QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys

from add_ons.style import Style
from add_ons.base_signals import *


class PlotCanvas(FigureCanvasQTAgg):
    """
    class inheriting from FigureCanvas, the plot will be drawn on the canvas,
    wich can be embedded in a QWidget.

    Usage:
    chart = PlotCanvas(self)
    chart.set_plot(x, y)
    """
    def __init__(self, parent, size=(10, 2)):
        self.fig, self.ax = plt.subplots(figsize=size, dpi=96)
        super().__init__(self.fig)
        self.setParent(parent)

        self.w = 3
        self.h = 3
        self.title = ''
        self.x_label = ''
        self.y_label = 'y'
        self.dpi = 96

    def set_plot(self, x=None, y=None, color='b'):

        self.ax.clear()

        if len(np.shape(y)) == 1:
            if x is not None:
                self.ax.plot(x, y, lw=2, ls='-', marker='', color=color, alpha=1.0)
            else:
                self.ax.plot(y, lw=2, ls='-', marker='', color=color, alpha=1.0)

            self.ax.grid(which='both', color='k', alpha=0.75, ls='-', lw=0.5)

            if self.x_label != '':
                self.ax.set_xlabel(self.x_label, FontSize=11)

            if self.y_label != '':
                self.ax.set_ylabel(self.y_label, FontSize=11)

            if self.title != '':
                self.ax.set_title(self.title, FontSize=12, FontWeight='bold')

            self.fig.tight_layout()
            self.fig.canvas.draw_idle()
            self.fig.canvas.flush_events()

        else:
            pass
            # print('Dimension von y nicht korrekt')

    def add_plot(self, x, y=None, color='b'):

        if len(np.shape(y)) == 1:
            if x is not None:
                self.ax.plot(x, y, lw=2, ls='-', marker='', color=color, alpha=1.0)
            else:
                self.ax.plot(y, lw=2, ls='-', marker='', color=color, alpha=1.0)

            self.fig.tight_layout()
            self.fig.canvas.draw_idle()
            self.fig.canvas.flush_events()

        else:
            pass
            # print('Dimension von y nicht korrekt')

    def save_plot(self, fname='default.png'):
        """method for saving the plot as png to given path"""
        self.fig.savefig(fname)


class PlotWidget(QWidget):
    """class to create widgets with embedded matplotlib plots"""
    def __init__(self, x=None, y=None, width=1600, height=800):
        super().__init__()
        self.resize(width, height)

        chart = PlotCanvas(self)
        chart.set_plot(x, y)
