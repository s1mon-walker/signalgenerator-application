import numpy as np
import scipy
from scipy import interpolate
from add_ons.csv_read_write import CsvReadWrite
from add_ons.plot_oop import PlotSimple2, PlotSimple1
from add_ons.base_signals import Sinus

# ===== shadow builtin print function to write logger file =====
from model.logger import logger
print = logger.debug
# ==============================================================


class FFT:
    """
    Class to handle the fast fourier transform of a signal
    """

    def __init__(self, param='daten.csv'):
        if type(param) == str:
            self.dateinamen = param
            self.header, self.values = self.read_data(csv=CsvReadWrite(self.dateinamen))
        elif type(param) == list or np.ndarray:
            self.header = None
            self.values = param
        else:
            print('[FFT] unsupported argument type')
            self.mode_csv = False

        self.anzahl_stellen_original = np.shape(self.values)[1] # diese Anzahl Stützstellen muss auf die nächsthöhere 2er-Potenz erweitert werden
        self.plot = PlotSimple2()
        self.t_neu = self.anzahl_stuetzstellen_anpassen()  # neuer Zeitvektor (Stützstellen)
        self.y_neu = self.resampling()  # neue Werte zum neuen Zeitvektor
        self.offset = self.offset_korrektur()
        self.fenster = self.fensterfunktionen_anwenden()
        self.y_neu += self.offset
        self.fft = scipy.fft(self.y_neu)
        self.fft = np.absolute(self.fft) * (2 / len(self.fft))
        self.fft[0] = 0.5 * self.fft[0]

        T = (len(self.fft) - 1) * self.t_neu[1]
        f_min = 1 / T
        f_max = 1 / self.t_neu[1]
        self.freq = np.arange(0, f_max, f_min)

        self.fft = self.fft[:int(len(self.fft)/2)]
        self.freq = self.freq[:len(self.fft)]

    def set_filename(self, filename='daten.csv'):
        self.dateinamen = filename
        self.header, self.values = self.read_data(csv=CsvReadWrite(self.dateinamen))
        self.anzahl_stellen_original = np.shape(self.values)[1]  # diese Anzahl Stützstellen muss auf die nächsthöhere 2er-Potenz erweitert werden

    def anzahl_stuetzstellen_anpassen(self):
        neue_anzahl = int(2 ** np.ceil(np.log2(self.anzahl_stellen_original)))  # neue Anzahl Stützstellen entspricht 2er-Potenz
        neuer_zeitvektor = np.linspace(0, self.values[0][-1], neue_anzahl)  # hier kann die Erstellung des neuen Zeitvektors implementiert werden -> linspace!
        return neuer_zeitvektor

    def resampling(self):
        # erzeugen der entsprechenden Funktion f für die Interpolation (linear)
        f = interpolate.interp1d(self.values[0], self.values[1], kind='linear')
        y_neu = f(self.t_neu)  # Auswerten dieser Funktion an den neuen Stützstellen
        return y_neu

    def offset_korrektur(self):
        offset = np.mean(self.y_neu)
        self.y_neu -= offset
        return offset

    def fensterfunktionen_anwenden(self):
        # Hier können die verschiedenen Fensterfunktionen angewendet werden
        y_window = np.hamming(self.anzahl_stellen_original)  # auf korrekte Anzahl Stützstellen anpassen!
        self.y_neu * y_window
        return y_window

    @staticmethod
    def read_data(csv=None):
        csv.read()
        return csv.header, csv.data_np

    def plot_data(self, n=None):
        if n == None:
            n = len(self.fft)
        self.plot.plot(self.values[0], [self.values[1], self.fenster])
        self.plot.plot(self.freq[:n], [self.fft[:n]])
        # Signal 1: Originalmessung
        # Signal 2: Hamming-Fenster entspricht Länge der Originalmessung

    def get_biggest_n_index(self, n=1):
        values = []
        fft = self.fft
        for i in range(n):
            biggest = np.argmax(fft)
            values.append(biggest)
            fft = np.delete(fft, biggest)
        return values

    def get_biggest_n_freq(self, n=1):
        values = []
        index = self.get_biggest_n_index(n)
        for i in index:
            values.append(self.freq[i])
        return values

    def get_biggest_n_amp(self, n=1):
        fft = np.sort(self.fft)
        fft = np.flip(fft)
        return fft[:n]

    def clean_data(self, factor=1):
        biggest2 = self.get_biggest_n_amp(2)
        delta = biggest2[0] - biggest2[1]
        threshold = biggest2[0] / 10 / delta * factor
        for i in range(len(self.fft)):
            if self.fft[i] < threshold:
                self.fft[i] = 0

    def auto_plot_window(self, n=10):
        indexs = self.get_biggest_n_index(n)
        indexs = sorted(indexs)
        end = int(indexs[-1] * 1.1 + len(self.fft) * 0.01)
        end = min(end, len(self.fft))
        return end

    def generate_fourier_series(self, n, n_periods=1):
        '''
        Prototyp einer Funktion zu automatischen konvertierung eines beliebigen Signals
        in eine Summe reiner Sinussignale.
        Funktioniert aktuell nur mit Square als Inputsignal
        Notiz: evtl. könnte noch eine ifft verwendet werden
        :param n:
        :param n_periods:
        :return:
        '''
        amplitudes = self.get_biggest_n_amp(n)
        print('[FFT] Amplitudes: ' + str(amplitudes))
        freqs = self.get_biggest_n_freq(n)
        print('[FFT] Freqs: ' + str(freqs))
        base_n_periods = n_periods
        self.signals = []
        n_periods = []

        for i in range(n):
            freqs[i] = np.ceil(freqs[i])
            n_periods.append(base_n_periods * (freqs[i] / freqs[0]))
            self.signals.append(Sinus(freqs[i], 2**12, amplitudes[i], n_periods[-1]))

        self.series_signal = sum(self.signals)

        return [amplitudes, freqs, n_periods]


if __name__ == '__main__':
    from add_ons.base_signals import *

    dateinamen = 'messung.csv'
    sin1 = Sinus(f=10, n_sp=2**12, amplitude=2, n=10)
    sin2 = Sinus(f=100, n_sp=2**12, amplitude=3, n=100)
    sin3 = Sinus(f=1000, n_sp=2**12, amplitude=3, n=1000)
    sig = sin1 + sin2 + sin3
    # sig = Square(f=1, n=100)

    fft = FFT(param=[sig.t, sig.signal])
    # fft.clean_data()
    i = fft.auto_plot_window(10)
    fft.plot_data(i)

    # series = fft.generate_fourier_series(10, 2)
    # plot = PlotSimple1()
    # plot.plot(series.t, series.signal)
