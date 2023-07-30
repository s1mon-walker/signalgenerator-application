import numpy as np
import copy

# ===== shadow builtin print function to write logger file =====
from model.logger import logger
print = logger.debug
# ==============================================================


class SignalBase():
    """
    Basisklasse mit den Gemeinsamkeiten der Signale.

    Sinn der Signalklasse:
    Die Funktionen sind objekte, welche anschliessend einem Funktionsgenrator übergebn werden können
    """

    def __init__(self, f=100,
                       n_sp = 2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0):

        self.f = f  # Signalfrequenz
        self.n_sp = n_sp  # Anzahl Sampling Points

        self.amplitude = amplitude  # Amplitude des Signals
        self.n = n  # Anzahl Perioden in der betrachteten Zeitspanne t_sp
        self.t_sp = 1/f * n  # s Betrachtete Zeitspanne
        self.phase = phase  # Phasenverschiebung (im Bogenmass)
        self.offset = offset  # Offset des Signals

        self.sp = None  # NumPy Array der Grösse n_sp
        self.dt_sp = None  # s Zeit zwischen zwei Sampling Points
        self.t = None  # Zeitvektor
        self.t_ms = None # Zeitvektor in Millisekunden
        self.wt = None  # Produkt aus Kreisfrequenz, Anzahl Perioden und Zeitvektor
        self.sampling_rate = None  # Taktrate bei der Ausgabe auf einem Signalgenerator

        self.signal = np.zeros(n_sp)  # Signalvektor
        self.normalised = False

    def calc(self):
        self.sp = np.arange(0, self.n_sp, 1)  # NumPy Array der Grösse n_sp
        self.dt_sp = self.t_sp / (self.n_sp - 1)  # s Zeit zwischen zwei Sampling Points
        self.t = self.dt_sp * self.sp  # Zeitvektor
        self.t_ms = self.t * 1000
        self.wt = 2 * np.pi * self.f * self.t  # Produkt aus Kreisfrequenz, Anzahl Perioden und Zeitvektor
        self.sampling_rate = self.n_sp / self.t_sp  # Taktrate bei der Ausgabe auf einem Signalgenerator
        if self.normalised:
            self.signal = self.signal * self.amplitude + self.offset
            self.normalised = False

    def normalise(self):
        if not self.normalised:
            self.signal = self.signal - self.offset
            self.signal = self.signal / self.amplitude
            self.normalised = True

    def __add__(self, other):
        # ToDo: Function still alters self
        if type(other) == int or type(other) == float:
            signal_sum = SignalBase(self.f, self.n_sp, self.amplitude, self.n, self.phase, self.offset)
            signal_sum.calc()
            signal_sum.signal = self.signal
            if self.normalised:
                signal_sum.offset += other
            else:
                signal_sum.signal += other
        else:
            if self.n_sp != other.n_sp:
                print('[SIGNALS] error adding signals n_sp not equal')
                return 1
            elif self.dt_sp != other.dt_sp:
                print('[SIGNALS] error adding signals dt_sp not equal')
                return 1

            signal_sum = SignalBase(self.f, self.n_sp, self.amplitude, self.n, self.phase, self.offset)
            signal_sum.signal = self.signal
            signal_sum.calc()
            other.calc()
            signal_sum.signal = signal_sum.signal + other.signal
            signal_sum.offset = np.mean(signal_sum.signal)
            signal_sum.amplitude = (np.max(signal_sum.signal) - np.min(signal_sum.signal)) / 2

        return signal_sum

    def __radd__(self, other):  # sum(signal_list)
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            signal_prod = copy.copy(self)
            if self.normalised:
                signal_prod.amplitude *= other
            else:
                signal_prod.signal *= other
        else:
            if self.n_sp != other.n_sp:
                return 1
            elif self.dt_sp != other.dt_sp:
                return 1
            signal_prod = SignalBase(self.f, self.n_sp, self.amplitude, self.n, self.phase, self.offset)
            signal_prod.signal = self.signal
            signal_prod.calc()
            other.calc()
            signal_prod.signal = signal_prod.signal * other.signal
            signal_prod.offset = np.mean(signal_prod.signal)
            signal_prod.amplitude = (np.max(signal_prod.signal) - np.min(signal_prod.signal)) / 2

        return signal_prod

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return 'SignalBase({},{},{})'.format(self.amplitude, self.f, self.phase)


class Sinus(SignalBase):
    def __init__(self, f=100,
                       n_sp=2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0):

        if f == 0:
            f = 1
            amplitude = 0
        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        self.signal = self.amplitude * np.sin(self.wt + self.phase) + self.offset

    def __str__(self):
        return 'Sinus({},{},{})'.format(self.amplitude, self.f, self.phase)


class Cosinus(SignalBase):
    def __init__(self, f=100,
                       n_sp=2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        self.signal = self.amplitude * np.cos(self.wt + self.phase) + self.offset

    def __str__(self):
        return 'Cosinus({},{},{})'.format(self.amplitude, self.f, self.phase)


class Tangent(SignalBase):
    def __init__(self, f=100,
                 n_sp=2**12,
                 amplitude=1.0,
                 n=2.0,
                 phase=0.0,
                 offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        self.signal = self.amplitude * np.tan(self.wt + self.phase) + self.offset

    def __str__(self):
        return 'Tangent({},{},{})'.format(self.amplitude, self.f, self.phase)


class Square(SignalBase):
    def __init__(self, f=100,
                       n_sp=2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        sin_sp = self.amplitude * np.sin(self.wt + self.phase)
        for i in range(0, self.n_sp, 1):
            if sin_sp[i] >= 0.0:
                self.signal[i] = self.amplitude + self.offset
            else:
                self.signal[i] = (-1) * self.amplitude + self.offset

    def __str__(self):
        return 'Square({},{},{})'.format(self.amplitude, self.f, self.phase)


class Triangle(SignalBase):
    def __init__(self, f=100,
                       n_sp=2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        sin_sp = 1 * np.sin(self.wt + self.phase)
        arcsin = np.arcsin(sin_sp) * 2 / np.pi
        self.signal = arcsin * self.amplitude + self.offset

    def __str__(self):
        return 'Triangle({},{},{})'.format(self.amplitude, self.f, self.phase)


class RampUp(SignalBase):
    def __init__(self, f=100,
                 n_sp=2**12,
                 amplitude=1.0,
                 n=2.0,
                 phase=0.0,
                 offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        self.signal = np.zeros(2 * self.n_sp)
        value = self.offset
        for i in range(0, 2*self.n_sp, 1):
            if i % int(self.n_sp / self.n) == 0:
                value = self.offset
            else:
                value += self.amplitude / self.n_sp * self.n
            self.signal[i] = value

        self.signal *= 2
        self.signal -= (np.max(self.signal) - np.min(self.signal)) / 2
        phase = int(self.n_sp * (self.phase / (2*np.pi) / self.n))
        self.signal = self.signal[phase:phase+self.n_sp]

    def __str__(self):
        return 'RampUp({},{},{})'.format(self.amplitude, self.f, self.phase)


class RampDown(SignalBase):
    def __init__(self, f=100,
                 n_sp=2**12,
                 amplitude=1.0,
                 n=2.0,
                 phase=0.0,
                 offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        self.signal = np.zeros(2 * self.n_sp)
        value = self.offset + self.amplitude
        for i in range(0, 2*self.n_sp, 1):
            if i % int(self.n_sp / self.n) == 0:
                value = self.offset + self.amplitude
            else:
                value -= self.amplitude / self.n_sp * self.n
            self.signal[i] = value

        self.signal *= 2
        self.signal -= (np.max(self.signal) - np.min(self.signal)) / 2
        phase = int(self.n_sp * (self.phase / (2*np.pi) / self.n))
        self.signal = self.signal[phase:phase+self.n_sp]

    def __str__(self):
        return 'RampDown({},{},{})'.format(self.amplitude, self.f, self.phase)


class Trapezium(SignalBase):
    def __init__(self, f=100,
                 n_sp=2**12,
                 amplitude=1.0,
                 n=2.0,
                 phase=0.0,
                 offset=0.0):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.calc()

    def calc(self):
        super().calc()
        print('to do')

    def __str__(self):
        return 'Trapezium({},{},{})'.format(self.amplitude, self.f, self.phase)


class PWM(SignalBase):
    def __init__(self, f=100,
                       n_sp=2**12,
                       amplitude=1.0,
                       n=2.0,
                       phase=0.0,
                       offset=0.0,
                       duty_cycle=0.75):

        super().__init__(f, n_sp, amplitude, n, phase, offset)
        self.duty_cycle = duty_cycle
        self.calc()

    def calc(self):
        super().calc()
        sin_sp = 1 * np.sin(self.wt + self.phase)
        triangle_sp = 1 * np.arcsin(sin_sp) / np.pi + 0.5
        for i in range(0, self.n_sp, 1):
            if triangle_sp[i] < self.duty_cycle:
                self.signal[i] = self.amplitude + self.offset
            else:
                self.signal[i] = 0.0 + self.offset

    def __str__(self):
        return 'PWM({},{},{})'.format(self.amplitude, self.f, self.phase)


def n_to_pow2(n):
    if n in [2**x for x in range(16)]:
        return n
    else:
        next_n = next_pow2(n)
        last_n = last_pow2(n)
        delta_n_next = abs(next_n - n)
        delta_n_last = abs(n - last_n)
        if delta_n_last < delta_n_next:
            return last_n
        else:
            return next_n


def last_pow2(n):
    return int(2**np.floor(np.log2(n)))


def next_pow2(n):
    return int(2**np.ceil(np.log2(n)))


if __name__ == '__main__':
    from plot_oop import *
    import numpy as np


    frequenz = 10
    n_samples = 2**12
    amplitude = 2
    n_perioden = 2
    phase = 0
    offset = 1

    # sin3 = 1 + sin2
    # self.__add__(sin1, sin2) => self.__add__(self, other)

    signaltest = RampUp(frequenz, n_samples, amplitude, n_perioden, phase, offset)
    signaltest2 = Sinus(100, 2**12, 1, 20, 0, 0)

    plot_signal = PlotSimple1(width=5, height=2, dpi=140)
    plot_signal.plot(x=signaltest.t, y=signaltest.signal)

    signals = []
    for i in range(1, 10):
        sig = Sinus(2*i-1, 2**12, (4/np.pi/(2*i-1)), 2*(2*i-1))
        signals.append(sig)
        plot_signal.plot(sig.t, sig.signal)

    square = sum(signals)

    plot_signal.plot(square.t, square.signal)
