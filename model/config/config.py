#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
from add_ons.base_signals import *


class Config:
    """Konfigurationsklasse für den remanenten Datenzugriff von Parametern."""
    def __init__(self, file_path=None):
        if file_path is None:
            absolute_path = (os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
            self._file_path = absolute_path + '/config.ini'
        else:
            self._file_path = file_path

        self._config = ConfigParser()

        # [style]
        self.style_dark = False

        # [parameter]
        self.n_samples = 0
        self.t_mess = 0
        self.n_periods = 0
        self.faktor = 0
        self.offset = 0
        self.anteile_sichtbar = False

        # [signals]
        self.signals = []

        self.read()

    def read(self):
        """Lesen der Parameter aus der Konfigurationsdatei."""
        try:
            f = open(self._file_path, 'r')
            self._config.read_file(f)
            f.close()

            # [style]
            self.style_dark = self._config.getboolean('style', 'dark')

            # [parameter]
            self.n_samples = self._config.getint('parameter', 'n_samples')
            self.t_mess = self._config.getfloat('parameter', 't_mess')
            self.n_periods = self._config.getfloat('parameter', 'n_periods')
            self.faktor = self._config.getfloat('parameter', 'faktor')
            self.offset = self._config.getfloat('parameter', 'offset')
            self.anteile_sichtbar = self._config.getboolean('parameter', 'anteile_sichtbar')

            # [signals]
            self._signalstring = self._config.get('signals', 'signals')
            self.unpack_signalstring()

            print('[CONFIG] config file read')

        except Exception as e:
            print('[CONFIG] Error _config read:' + str(e))

        finally:
            f.close()

    def write(self):
        """Schreiben der Parameter in die Konfigurationsdatei."""
        try:
            f = open(self._file_path, 'w')

            # [style]
            self._config.set('style', 'dark', Config.bool_to_string(self.style_dark))

            # [parameter]
            self._config.set('parameter', 'n_samples', '{:d}'.format(self.n_samples))
            self._config.set('parameter', 't_mess', '{:f}'.format(self.t_mess))
            self._config.set('parameter', 'n_periods', '{:f}'.format(self.n_periods))
            self._config.set('parameter', 'faktor', '{:f}'.format(self.faktor))
            self._config.set('parameter', 'offset', '{:f}'.format(self.offset))
            self._config.set('parameter', 'anteile_sichtbar', Config.bool_to_string(self.anteile_sichtbar))

            # self._config.set('demo', 'demo_int', '{:d}'.format(self.demo_int))
            # self._config.set('demo', 'demo_float', '{:f}'.format(self.demo_float))
            # self._config.set('demo', 'demo_string', '{:s}'.format(self.demo_string))

            # [signals]
            self.build_signalstring()
            print(self._signalstring)
            self._config.set('signals', 'signals', '{:s}'.format(self._signalstring))

            self._config.write(f)
            print('[CONFIG] config file written')

        except Exception as e:
            print('[CONFIG] Error _config write:', str(e))
            f.write('[style]')

        finally:
            f.close()

    @staticmethod
    def bool_to_string(value):
        """Hilfsmethode zur Speicherung von boolschen Datentypen. In Konfigurationsdateien
        sind die Werte True und False in true und false zu konvertieren."""
        if value:
            string = 'true'
        else:
            string = 'false'
        return string

    def build_signalstring(self):
        self._signalstring = ''
        for signal in self.signals:
            self._signalstring += str(signal)
            self._signalstring += ';'
        self._signalstring = self._signalstring[0:-3]
        print('[CONFIG] signalstring built')

    def unpack_signalstring(self):
        self.signals = []
        string = self._signalstring
        index = string.find('=')
        string = string[index+1:]
        strings = string.split(';')
        for element in strings:
            index = element.find('(')
            args = element[index+1:-2]
            args = args.split(',')
            amp = args[0]
            freq = args[1]
            phase = args[2]

            if 'SignalBase' in element:
                self.signals.append(['base', amp, freq, phase])
            elif 'Sinus' in element:
                self.signals.append(['sin', amp, freq, phase])
            elif 'Cosinus' in element:
                self.signals.append(['cos', amp, freq, phase])
            elif 'Tangent' in element:
                self.signals.append(['tan', amp, freq, phase])
            elif 'Square' in element:
                self.signals.append(['square', amp, freq, phase])
            elif 'Triangle' in element:
                self.signals.append(['tringle', amp, freq, phase])
            elif 'RampUp' in element:
                self.signals.append(['rampup', amp, freq, phase])
            elif 'RampDown' in element:
                self.signals.append(['rampdown', amp, freq, phase])
            elif 'PWM' in element:
                self.signals.append(['pwm', amp, freq, phase])
            else:
                print('[CONFIG] error unpacking signalstring: unknown signaltype')


if __name__ == '__main__':
    config = Config()
    config.read()

    print('[style]')
    print('dark =', config.style_dark)

    config.write()
