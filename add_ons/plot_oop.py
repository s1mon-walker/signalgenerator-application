import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np

import add_ons.plot_toolbox
import add_ons.base_signals
from add_ons import plot_toolbox


class PlotBase:
    """
    Basisklasse für die Darstellung von Plots in 2D und 3D
    """

    def __init__(self, width=8, height=3, dpi=140):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.fig = None
        self.ax = None

        self.title = ''
        self.x_label = ''
        self.y_label = ''

    def save_figure(self, url='img/plot.png', dpi=300):
        """
        Speichere die Figure in einem Bildformat (jpg, png...) mit der entsprechenden
        dpi Auflösung ab.
        """
        self.fig.savefig(url, dpi=dpi)

    @staticmethod
    def show_plot(show):
        """
        Wird das Skript nicht in der Jupyterumgebung aufgerufen, ist der Aufruf der
        Methode plt.show() für die Anzeige notwendig.
        """
        plt.tight_layout()

        if show:
            if not plot_toolbox.run_from_ipython():
                plot_toolbox.move_figure(plt)
                plt.show()


class PlotSimple1(PlotBase):
    """
    Klasse für die einfache Darstellung von Linienplots
    """

    def __init__(self, width=8, height=3, dpi=140):
        """
        Initialisierung
        """
        super().__init__(width, height, dpi)

    def plot(self, x=None, y=None, show=True):

        self.fig, self.ax = plt.subplots(1, 1, figsize=(self.width, self.height), dpi=self.dpi)

        if len(np.shape(y)) == 1:
            if x is not None:
                self.ax.plot(x, y, lw=2, ls='-', marker='', color='b', alpha=1.0)
            else:
                self.ax.plot(y, lw=2, ls='-', marker='', color='b', alpha=1.0)

            self.ax.grid(which='both', color='k', alpha=0.75, ls='-', lw=0.5)

            self.ax.set_xlabel(self.x_label, FontSize=11)

            if self.x_label != '':
                self.ax.set_xlabel(self.x_label, FontSize=11)

            if self.y_label != '':
                self.ax.set_ylabel(self.y_label, FontSize=11)

            if self.title != '':
                self.ax.set_title(self.title, FontSize=12, FontWeight='bold')

            PlotBase.show_plot(show)
        else:
            print('Dimension von y nicht korrekt')


class PlotSimple2(PlotBase):
    """
    Klasse für die einfache Darstellung von Linienplots
    """

    def __init__(self, width=8, height=3, dpi=140):
        """
        Initialisierung
        """
        super().__init__(width, height, dpi)

    def plot(self, x=None, y=[], marker='',show=True):

        self.fig, self.ax = plt.subplots(1, 1, figsize=(self.width, self.height), dpi=self.dpi)

        if len(np.shape(y)) == 1:
            if x is not None:
                self.ax.plot(x, y, lw=2, ls='-', marker='', color='b', alpha=1.0)
            else:
                self.ax.plot(y, lw=2, ls='-', marker='', color='b', alpha=1.0)
        elif len(np.shape(y)) == 2:
            for i in range(0, np.shape(y)[0], 1):
                if x is not None:
                    self.ax.plot(x, y[i], lw=2, ls='-', marker=marker, color='b', alpha=1.0)
                else:
                    self.ax.plot(y[i], lw=2, ls='-', marker='', color='b', alpha=1.0)

        self.ax.grid(which='both', color='k', alpha=0.75, ls='-', lw=0.5)

        if self.x_label != '':
            self.ax.set_xlabel(self.x_label, FontSize=11)

        if self.y_label != '':
            self.ax.set_ylabel(self.y_label, FontSize=11)

        if self.title != '':
            self.ax.set_title(self.title, FontSize=12, FontWeight='bold')

        PlotBase.show_plot(show)


if __name__ == '__main__':
    x = np.linspace(-10, 10, num=100, endpoint=True)
    y = x**2
    z = x**3

    n = 900
    n = base_signals.n_to_pow2(n)
    print(n)

    signal = base_signals.Tangent(10, 4098, 1, 2, 0, 0)
    plot_signal = PlotSimple2()
    plot_signal.plot(signal.t_ms, signal.signal)

    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure