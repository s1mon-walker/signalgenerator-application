# -*- coding: utf-8 -*-
# =========================================================
# ===== EWS Applikation Analog Discovery     18-02-21 =====
# ===== Projekt der ABB Technikerschule               =====
# ===== Simon Walker, Philipp Eberle, Husein Mazlagic =====
# =========================================================

import getpass
import sys
import time
import math as m

from PyQt5.QtCore import QSize, QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QInputDialog, QFileDialog, QMessageBox

import add_ons.style
from add_ons.ad_control import AnalogDiscoveryController
from add_ons.fft import FFT
from add_ons.ui_widgets import *
from add_ons.base_signals import *
from model.config import config
from ui.main_ui import Ui_MainWindow

# ===== shadow builtin print function to write logger file =====
from model.logger import logger
print = logger.debug
# ==============================================================
# from widget_custom.list_item.list_item import ListItem, ListItemWidget

# 4k Display mit hoher DPI-Auflösung
# if hasattr(Qt, 'AA_EnableHighDpiScaling'):
#     QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
# if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
#     QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self, parent=None):
        # Instantiation of the base class
        QMainWindow.__init__(self, parent)

        # Instance of the visual description from QT Creator
        self.ui = Ui_MainWindow()
        # making the visualisation structure
        self.ui.setupUi(self)
        self.setWindowTitle('EWS Projekt Analog Discovery')
        self.setMinimumSize(QSize(100, 50))
        # self.resize(500, 1000)
        self.move(-5, 0)

        # Creating instance Analog Discovery Controller class
        self.ad = AnalogDiscoveryController()
        if self.ad.cdevices.value == 1:
            self.ad_available = True
        else:
            self.ad_available = False
        self.setWindowTitle('EWS Projekt Analog Discovery - ' + self.ad.version_str)

        self.fft = None

        # setting icons for actions
        self.ui.actionSchliessen.setIcon(QIcon('assets/icon/exit.ico'))
        self.ui.actionExport_als_csv.setIcon(QIcon('assets/icon/excel.ico'))
        self.ui.actionConfig_speichern.setIcon(QIcon('assets/icon/save.ico'))
        self.ui.actionAlle_Signale_del.setIcon(QIcon('assets/icon/clear.ico'))
        self.ui.actionAD_verbinden.setIcon(QIcon('assets/icon/connected.ico'))
        self.ui.actionConfig_laden.setIcon(QIcon('assets/icon/folder.ico'))
        self.ui.actionNeu.setIcon(QIcon('assets/icon/new.ico'))
        self.ui.actionExport_als_png.setIcon(QIcon('assets/icon/png.ico'))
        self.ui.actionErweiterte_Fourierreihe.setIcon(QIcon('assets/icon/equal.ico'))

        # Creating the base Variables
        self.ad_ready = False
        self.factor = 1
        self.offset = 0
        self.n_periods = 0
        self.t_mess = 0.1
        self.ad.n_sp = 4096
        self.fft_sig = None
        self.fft_ch1 = None
        self.fft_ch2 = None
        self.amplification = None
        self.phase = None
        self.new_data = False
        self.ui.lineEdit_n_samp.setText(str(self.ad.n_sp))
        self.ui.lineEdit_faktor.setText(str(self.factor))
        self.ui.lineEdit_t_mess.setText(str(self.t_mess))
        self.ui.lineEdit_offset.setText(str(self.offset))
        self.ui.lineEdit_n_periods.setText('1')
        self.ui.lineEdit_verstaerkung.setReadOnly(True)
        self.ui.lineEdit_phase.setReadOnly(True)

        # Verlinkung der Events aus dem PyQt Framework mit den Eventhandler.
        self.ui.actionNeu.triggered.connect(self.on_new)
        self.ui.actionConfig_speichern.triggered.connect(self.on_write_config)
        self.ui.actionConfig_laden.triggered.connect(self.on_read_config)
        self.ui.actionSchliessen.triggered.connect(self.close)
        self.ui.actionAlle_Signale_del.triggered.connect(self.on_del_all_sig)
        self.ui.actionExport_als_csv.triggered.connect(self.on_export_csv)
        self.ui.actionExport_als_png.triggered.connect(self.on_export_png)
        self.ui.actionErweiterte_Fourierreihe.triggered.connect(self.on_advanced_fourier)
        self.ui.actionAD_verbinden.triggered.connect(self.on_reconnect_ad)
        self.ui.actionKannal_1.triggered.connect(self.on_choose_ch1)
        self.ui.actionKannal_2.triggered.connect(self.on_choose_ch2)
        self.ui.actionPlot_Ordinate_beschriften.triggered.connect(self.update_plots)
        self.ui.actionPlot_Abszisse_beschriften.triggered.connect(self.update_plots)

        self.ui.lineEdit_n_samp.editingFinished.connect(self.on_changed_n_samples)
        self.ui.lineEdit_n_samp.setValidator(QIntValidator())
        self.ui.lineEdit_offset.editingFinished.connect(self.on_changed_offset)
        self.ui.lineEdit_offset.setValidator(QDoubleValidator())
        self.ui.lineEdit_faktor.editingFinished.connect(self.on_changed_factor)
        self.ui.lineEdit_faktor.setValidator(QDoubleValidator())
        self.ui.lineEdit_n_periods.editingFinished.connect(self.on_changed_n_periods)
        self.ui.lineEdit_n_periods.setValidator(QDoubleValidator())
        self.ui.lineEdit_t_mess.editingFinished.connect(self.on_changed_t_mess)
        self.ui.lineEdit_t_mess.setValidator(QDoubleValidator())

        self.palette_lineedit = self.ui.lineEdit_t_mess.palette()
        # print('Palette base: ', self.palette_lineedit.base().color().getRgb())
        self.palette_readonly = self.ui.lineEdit_t_mess.palette()
        if config.style_dark:
            self.palette_readonly.setColor(QPalette.Base, QColor(40, 40, 100))
        else:
            self.palette_readonly.setColor(QPalette.Base, QColor(220, 220, 220))

        self.ui.btn_add_sig.clicked.connect(self.on_add_sig)
        self.ui.btn_del_sig.clicked.connect(self.on_del_sig)
        self.ui.btn_make_sig.clicked.connect(self.on_make_sig)
        self.ui.btn_start.clicked.connect(self.on_start)

        self.ui.radioButton_t.toggled.connect(self.on_changed_t_mess)
        self.ui.radioButton_n.toggled.connect(self.on_changed_n_periods)
        self.ui.checkBox_anteile.toggled.connect(self.update_plots)
        self.ui.radioButton_n.click()

        self.ui.progressBar.setValue(0)
        self.ui.horizontalSlider_1.valueChanged.connect(self.on_slider_1_changed)
        self.ui.horizontalSlider_2.valueChanged.connect(self.on_slider_2_changed)

        # Zuweisen der Widgets
        self.plot_1 = PlotCanvas(self.ui.tabWidget)
        self.ui.verticalLayout_11.addWidget(self.plot_1)
        self.plot_1.y_label = 'Amplitude [V]'
        self.plot_1.set_plot()
        self.plot_2 = PlotCanvas(self.ui.tabWidget)
        self.ui.verticalLayout_11.addWidget(self.plot_2)
        self.plot_2.y_label = 'Amplitude [V]'
        self.plot_2.set_plot()
        self.plot_3 = PlotCanvas(self.ui.tabWidget)
        self.ui.verticalLayout_11.addWidget(self.plot_3)
        self.plot_3.y_label = 'Amplitude [V]'
        self.plot_3.x_label = 'Frequenz [Hz]'
        self.plot_3.set_plot()
        self.plot_4 = PlotCanvas(self.ui.tabWidget, (10, 4))
        self.ui.verticalLayout_21.addWidget(self.plot_4)
        self.plot_4.y_label = 'Amplitude [V]'
        self.plot_4.x_label = 'Zeit [s]'
        self.plot_4.set_plot()
        self.plot_5 = PlotCanvas(self.ui.tabWidget)
        self.ui.verticalLayout_21.addWidget(self.plot_5)
        self.plot_5.y_label = 'Amplitude [V]'
        self.plot_5.x_label = 'Frequenz [Hz]'
        self.plot_5.set_plot()

    def on_new(self):
        """Creates new blank workspace"""
        print('[MAIN] new workspace...')
        self.ad_ready = False
        self.factor = 1
        self.offset = 0
        self.n_periods = 1
        self.t_mess = 0.1
        self.ad.n_sp = 4096
        self.ui.lineEdit_n_samp.setText(str(self.ad.n_sp))
        self.ui.lineEdit_faktor.setText(str(self.factor))
        self.ui.lineEdit_t_mess.setText(str(self.t_mess))
        self.ui.lineEdit_offset.setText(str(self.offset))
        self.ui.lineEdit_n_periods.setText(str(self.n_periods))

        self.on_del_all_sig()
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('sin'))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem('1'))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem('10'))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem('0'))

    def on_changed_n_samples(self):
        """handles changes to the samplecount by user"""
        value = int(self.ui.lineEdit_n_samp.text())
        if float(np.log2(value)).is_integer() or not self.ui.actionAnzahl_Samples_nur_2er_Potenzen.isChecked():
            pass
        else:
            value = n_to_pow2(value)
            self.ui.lineEdit_n_samp.setText(str(value))

    def on_changed_offset(self):
        """handles changes to the offset by user"""
        self.offset = float(self.ui.lineEdit_offset.text())

    def on_changed_factor(self):
        """handles changes to the signal amplification factor by user"""
        self.factor = float(self.ui.lineEdit_faktor.text())
        self.ad.factor = self.factor

    def on_changed_n_periods(self):
        """handles changes to the number of periods of the baser freqency in the first row"""
        self.n_periods = float(self.ui.lineEdit_n_periods.text())
        if self.ui.radioButton_n.isChecked():
            self.t_mess = self.n_periods * (1/float(self.ui.tableWidget.item(0, 2).text()))
            self.ui.lineEdit_n_periods.setReadOnly(False)
            self.ui.lineEdit_n_periods.setPalette(self.palette_lineedit)
            self.ui.lineEdit_t_mess.setReadOnly(True)
            self.ui.lineEdit_t_mess.setPalette(self.palette_readonly)
            self.ui.lineEdit_t_mess.setText(str(self.t_mess))

    def on_changed_t_mess(self):
        """handles changes to the signal time by calculating number of periods for base signal"""
        self.t_mess = float(self.ui.lineEdit_t_mess.text())
        if self.ui.radioButton_t.isChecked():
            self.n_periods = self.t_mess / (1/float(self.ui.tableWidget.item(0, 2).text()))
            self.ui.lineEdit_t_mess.setReadOnly(False)
            self.ui.lineEdit_t_mess.setPalette(self.palette_lineedit)
            self.ui.lineEdit_n_periods.setReadOnly(True)
            self.ui.lineEdit_n_periods.setPalette(self.palette_readonly)
            self.ui.lineEdit_n_periods.setText(str(self.n_periods))

    def on_slider_1_changed(self):
        """handles changes to the slider values and applys changes to fft plot on tab 1"""
        value = self.ui.horizontalSlider_1.value()
        end_plot_3 = int(len(self.fft_ch1.freq) / 100 * value)
        self.plot_3.set_plot(x=self.fft_ch1.freq[:end_plot_3], y=self.fft_ch1.fft[:end_plot_3])

    def on_slider_2_changed(self):
        """handles changes to the slider values and applys changes to fft plot on tab 2"""
        value = self.ui.horizontalSlider_2.value()
        end_plot_5 = int(len(self.fft_sig.freq) / 100 * value)
        self.plot_5.set_plot(x=self.fft_sig.freq[:end_plot_5], y=self.fft_sig.fft[:end_plot_5])
        self.plot_5.add_plot(x=self.fft_ch1.freq[:end_plot_5], y=self.fft_ch1.fft[:end_plot_5], color='r')
        self.plot_5.add_plot(x=self.fft_ch2.freq[:end_plot_5], y=self.fft_ch2.fft[:end_plot_5], color='magenta')

    def on_add_sig(self):
        """adds new row to the tableWidget"""
        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)

    def on_del_sig(self):
        """removes last row from tableWidget"""
        if self.ui.tableWidget.rowCount() >= 1:
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()-1)

    def on_del_all_sig(self):
        """set rowCount zo 0 and set all Items blank"""
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(4)
        for i in range(4):
            self.ui.tableWidget.setItem(0, i, QTableWidgetItem())

    def on_make_sig(self):
        """generating function from table contents"""
        print('[MAIN] making signal')
        ret = self.table_to_function()
        if ret == -1: return -1  # end function if table_to_functon() does not end successfully
        self.ad.n_sp = int(self.ui.lineEdit_n_samp.text())
        self.ad.set_function()
        if self.ad_available:
            self.ad_ready = True
        self.update_plots()

    def table_to_function(self):
        """making signal list from table contents and adding it up to one signal"""
        function_list = []
        freq_0 = 1
        n_signals = self.ui.tableWidget.rowCount()
        for i in range(n_signals):
            func = None
            try:
                function = self.ui.tableWidget.item(i, 0).text()
                amp = float(self.ui.tableWidget.item(i, 1).text())
                freq = float(self.ui.tableWidget.item(i, 2).text())
                phase = float(self.ui.tableWidget.item(i, 3).text())

                n_samples = self.ad.n_sp

                if i == 0:
                    n_periods = self.n_periods
                    freq_0 = freq
                else:
                    n_periods = self.n_periods * (freq / freq_0)
                    print('{} = {} * ({} / {})'.format(n_periods, self.n_periods, freq, freq_0))

            except ValueError:
                function = 'error'

            if function == 'sin':
                func = Sinus(freq, n_samples, amp, n_periods, phase)
            elif function == 'cos':
                func = Cosinus(freq, n_samples, amp, n_periods, phase)
            elif function == 'square':
                func = Square(freq, n_samples, amp, n_periods, phase)
            elif function == 'triang' or function == 'triangle':
                func = Triangle(freq, n_samples, amp, n_periods, phase)
            elif function == 'rampup':
                func = RampUp(freq, n_samples, amp, n_periods, phase)
            elif function == 'rampdown':
                func = RampDown(freq, n_samples, amp, n_periods, phase)
            elif function == 'pwm':
                func = PWM(freq, n_samples, amp, n_periods, phase, offset=0, duty_cycle=0.5)
            else:
                print('[MAIN] not filled table correctly')
                msg_box = QMessageBox(self)  # QIcon('assets/icon/clear.ico')
                msg_box.setWindowTitle('Fehler')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText('Tabelleninhalt ungültig:\nFehler in Zeile ' + str(i+1))
                msg_box.show()
                return -1

            if func is not None:
                function_list.append(func)
                print('[MAIN] made ' + str(func))

        function_list.append(self.offset)
        self.ad.n_signals = n_signals
        self.ad.signal_list = function_list

    def on_start(self):
        """starts a measuring thread for the AD if it is connected and ready"""
        if self.ad_ready and self.ad_available:
            print('[MAIN] starting ad')
            self.update_progress_bar(10)
            ad_thread = ADThread(self, lambda: self.ad.start(self, self.callback_after_ad_start))
            ad_thread.start_thread()
            self.ad_ready = False

    def update_progress_bar(self, status):
        """updates the progressbar to state between 0 and 100"""
        status = min(100, max(0, status))
        self.ui.progressBar.setValue(int(status))

    def update_plots(self):
        """updates all plots according to the state of the application"""
        time = self.ad.time
        signal = self.ad.signal * self.ad.amplitude
        ch1_data = self.ad.ch1
        ch2_data = self.ad.ch2

        if self.ui.actionPlot_Ordinate_beschriften.isChecked():
            self.plot_1.y_label = 'Amplitude [V]'
            self.plot_2.y_label = 'Amplitude [V]'
            self.plot_3.y_label = 'Amplitude [V]'
            self.plot_4.y_label = 'Amplitude [V]'
            self.plot_5.y_label = 'Amplitude [V]'
        else:
            self.plot_1.y_label = ''
            self.plot_2.y_label = ''
            self.plot_3.y_label = ''
            self.plot_4.y_label = ''
            self.plot_5.y_label = ''

        if self.ui.actionPlot_Abszisse_beschriften.isChecked():
            self.plot_1.x_label = 'Zeit [s]'
            self.plot_2.x_label = 'Zeit [s]'
            self.plot_3.x_label = 'Frequenz [Hz]'
            self.plot_4.x_label = 'Zeit [s]'
            self.plot_5.x_label = 'Frequenz [Hz]'
        else:
            self.plot_1.x_label = ''
            self.plot_2.x_label = ''
            self.plot_3.x_label = ''
            self.plot_4.x_label = ''
            self.plot_5.x_label = ''

        if self.ui.checkBox_anteile.isChecked():
            self.plot_1.set_plot(time, self.ad.signal_list[0].signal)
            if self.ad.n_signals > 1:
                for i in range(1, self.ad.n_signals):
                    self.plot_1.add_plot(time, self.ad.signal_list[i].signal)
        else:
            self.plot_1.set_plot(time, signal)

        self.plot_2.set_plot(time, ch1_data, 'r')
        self.plot_2.add_plot(time, ch2_data, 'magenta')

        if self.ad_ready and ch1_data:
            self.fft_sig = FFT([time, signal])
            self.fft_ch1 = FFT([time, ch1_data])
            self.fft_ch2 = FFT([time, ch2_data])
            if self.new_data:
                print('[MAIN] got new data')
                end_plot_3 = self.fft_ch1.auto_plot_window(len(self.ad.signal_list))
                end_plot_5 = self.fft_sig.auto_plot_window(len(self.ad.signal_list))
                value_slider_1 = int(100 / len(self.fft_ch1.freq) * end_plot_3)
                value_slider_2 = int(100 / len(self.fft_sig.freq) * end_plot_3)
                self.ui.horizontalSlider_1.setValue(value_slider_1)
                self.ui.horizontalSlider_2.setValue(value_slider_2)
                self.new_data = False
            else:
                end_plot_3 = len(self.fft_ch1.freq)
                end_plot_5 = len(self.fft_sig.freq)
            self.plot_3.set_plot(x=self.fft_ch1.freq[:end_plot_3], y=self.fft_ch1.fft[:end_plot_3])
            self.plot_5.set_plot(x=self.fft_sig.freq[:end_plot_5], y=self.fft_sig.fft[:end_plot_5])
            self.plot_5.add_plot(x=self.fft_ch1.freq[:end_plot_5], y=self.fft_ch1.fft[:end_plot_5], color='r')
            self.plot_5.add_plot(x=self.fft_ch2.freq[:end_plot_5], y=self.fft_ch2.fft[:end_plot_5], color='magenta')

        self.plot_4.set_plot(time, signal)
        self.plot_4.add_plot(time, ch1_data, 'r')
        self.plot_4.add_plot(time, ch2_data, 'magenta')

    def on_advanced_fourier(self):
        """prototype method: converts the genrated signal to pure sine signal"""
        num, ok = QInputDialog.getInt(self, 'Anzahl Sinussignale', 'Anzahl Sinussignale wählen:',
                                      5, 1, 100, 2)

        if ok:
            fft = FFT([self.ad.time, self.ad.signal])
            sigs = fft.generate_fourier_series(num)
            self.ui.tableWidget.setRowCount(len(sigs[0]))

            for i in range(len(sigs[0])):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem('sin'))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(sigs[0][i])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(sigs[1][i])))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem('0'))

            self.on_make_sig()

    def on_export_csv(self):
        """saves the data to csv file at user defined path"""
        file_name, ok = QFileDialog.getSaveFileUrl()
        file_name = file_name.toString()
        file_name = file_name[8:]
        file_name += '.csv' if file_name[-4:] != '.csv' else ''

        if ok:
            try:
                data_list = []
                data_list.append(self.ad.signal)
                data_list.append(self.ad.ch1)
                data_list.append(self.ad.ch2)
                data_list.append(self.fft_sig.freq)
                data_list.append(self.fft_sig.fft)
                data_list.append(self.fft_ch1.freq)
                data_list.append(self.fft_ch1.fft)
                data_list.append(self.fft_ch2.freq)
                data_list.append(self.fft_ch2.fft)

                data = np.asarray(self.ad.time)
                for element in data_list:
                    add_data = np.zeros(len(self.ad.time))
                    for i in range(len(element)):
                        add_data[i] = element[i]
                    data = np.vstack((data, add_data))
                data = data.swapaxes(0, 1)
                np.savetxt(file_name, data)
            except AttributeError:
                print('[MAIN] error: no data')

    def on_export_png(self):
        """lets user chose plot to export as png and shows dialog for configuring save path"""
        items = ['Fourierreihe', 'Messresultat', 'kombiniert', 'FFT von ch1', 'FFT von allen Signalen']
        item, ok = QInputDialog.getItem(self, 'Plot wählen',
                                        'Welcher Plot soll gespeichert werden?', items, 0, False)

        if ok:
            file_name, ok = QFileDialog.getSaveFileUrl()
            file_name = file_name.toString()
            file_name = file_name[8:]
            file_name += '.png' if file_name[-4:] != '.png' else ''

            if ok and item == 'Fourierreihe':
                self.plot_1.save_plot(file_name)
            elif ok and item == 'Messresultat':
                self.plot_2.save_plot(file_name)
            elif ok and item == 'FFT von ch1':
                self.plot_3.save_plot(file_name)
            elif ok and item == 'kombiniert':
                self.plot_4.save_plot(file_name)
            elif ok and item == 'FFT von allen Signalen':
                self.plot_5.save_plot(file_name)
            else:
                return -1

    def on_reconnect_ad(self):
        """Reconnecting the AD or building new connection if not connected"""
        self.ad.close()
        self.ad = AnalogDiscoveryController()
        if self.ad.cdevices.value == 1:
            self.ad_available = True
        else:
            self.ad_available = False
        self.ad.n_sp = int(self.ui.lineEdit_n_samp.text())

    def on_choose_ch1(self):
        """setting AD output channel to 1"""
        self.ad.set_channel(1)
        self.ui.actionKannal_2.setChecked(False)

    def on_choose_ch2(self):
        """setting AD output channel to 2"""
        self.ad.set_channel(2)
        self.ui.actionKannal_1.setChecked(False)

    @staticmethod
    def get_value_as_float(ui_line_edit):
        if ui_line_edit.text() == '':
            value = 0.0
        else:
            value = float(ui_line_edit.text())
        return value

    def on_write_config(self, filename=None):
        """Method to write the config file"""
        print('[MAIN] writing config file')
        config.style_dark = self.ui.actionDark_Mode.isChecked()
        config.n_samples = int(self.ui.lineEdit_n_samp.text())
        config.t_mess = self.t_mess
        config.n_periods = self.n_periods
        config.faktor = Main.get_value_as_float(self.ui.lineEdit_faktor)
        config.offset = Main.get_value_as_float(self.ui.lineEdit_offset)
        config.anteile_sichtbar = self.ui.checkBox_anteile.isChecked()
        config.signals = self.ad.signal_list
        config.write()

    def on_read_config(self, filename=None):
        """Method to read the config file"""
        print('[MAIN] reading config file')
        config.read()
        self.ui.actionDark_Mode.setChecked(config.style_dark)
        self.ui.lineEdit_n_samp.setText(str(config.n_samples))
        self.ui.lineEdit_t_mess.setText(str(config.t_mess))
        self.ui.lineEdit_n_periods.setText(str(config.n_periods))
        self.ui.lineEdit_faktor.setText(str(config.faktor))
        self.ui.lineEdit_offset.setText(str(config.offset))
        self.ui.checkBox_anteile.setChecked(config.anteile_sichtbar)

        self.ui.tableWidget.setRowCount(len(config.signals))
        for i in range(len(config.signals)):
            for j in range(len(config.signals[0])):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(config.signals[i][j]))

        self.on_make_sig()

    def callback_after_ad_start(self):
        """This method handles everything that needs to be done after AD is done"""
        self.ad_ready = True
        self.new_data = True
        self.update_plots()
        time = np.asarray(self.ad.time)
        ch1 = np.asarray(self.ad.ch1)
        ch2 = np.asarray(self.ad.ch2)
        freq = float(self.ui.tableWidget.item(0, 2).text())
        amplification, phase = auswertung(time, ch1, ch2, freq)
        phase *= -1 if dir else 1
        amplification = 20 * m.log10(max(amplification, 0.0000000001))
        self.update_progress_bar(100)
        self.ui.lineEdit_verstaerkung.setText('{:.2f}'.format(amplification))
        self.ui.lineEdit_phase.setText('{:.2f}'.format(phase))
        print('[MAIN] callback done')

    def keyPressEvent(self, event):
        """Event Erfassung und Auswertung der gedrückten Tasten."""
        super().keyPressEvent(event)
        Key_Enter = 16777220
        # print(event.key())
        if event.key() == Qt.Key_Q:
            self.close()
        elif event.key() == Key_Enter:
            self.on_make_sig()


def auswertung(zeitvektor, ch1, ch2, frequenz):
    '''
    Diese Funktion wertet 2 Signale auf Verstärkung und Phasenversatz aus, die Verstärkung wird aus dem Effektivwert der
    Signale errechnet. Die Phasenlage wird durch schieben des Signal ch2 auf der x-Achse und dem Vergleich mit ch1 errechnet.

     zeitvektor = Gemeinsame Zeitachse beider Signale
      ch1 = Messwerte auf Kanal 1
      ch2 = Messwerte auf Kanal 2
      frequenz = Frequenz der beiden Siganle zum bestimmen der Periodendauer

      return: verstärkung, phase
    '''

    ch1_delta = max(ch1) - min(ch1)
    ch2_delta = max(ch2) - min(ch2)
    ch1_offset = ch1_delta / 2 - max(ch1)  # Koorektur eines möglichen Offsets
    ch2_offset = ch2_delta / 2 - max(ch2)  # Koorektur eines möglichen Offsets
    ch1 = ch1 + ch1_offset
    ch2 = ch2 + ch2_offset

    ch1_RMS = np.sqrt(np.square(ch1)/2)
    ch2_RMS = np.sqrt(np.square(ch2)/2)
    ch1_RMS = np.median(ch1_RMS)
    ch2_RMS = np.median(ch2_RMS)
    verstaerkung = ch2_RMS / max(ch1_RMS, 0.001)  # Verstärkung aus dem Effektivwert der Spannung errechnen

    ch2 = ch2 * verstaerkung    # strecken von ch2 auf die Amplitude von ch1

    t_sample = zeitvektor[1]-zeitvektor[0]
    t_period = 1/frequenz
    index_period = t_period / t_sample
    index_span = int(index_period/2) - 1    # anzahl Indexe indenen die Phase liegen kann: +-180° - 1 Index

    delta_index = shift_signal(ch1, ch2, index_span)
    phase_t = delta_index * t_sample
    phase = phase_t / t_period * 360

    return verstaerkung, phase


def shift_signal(y1, y2, max_i, return_index=True):
    """
    Diese Funktion schiebt den Datensatz 1 auf der x-Achse um eine möglichst gute Übereinstimmung mit Datensatz 2 zu erhalten
     y1 = amplitude Signal 1, dieses wird geschoben     (Numpy Array)
     y2 = amplitude Signal 2, schablone                 (Numpy Array)
     max_i = maximale anzahl Indexe um die geschoben werden soll
     return_index = Auswahl ob die anzahl Indexe oder der neue Datensatz ausgegeben wird

     return: y1_best oder delta_index
    """

    if not len(y1) == len(y2):
        print('===== Fehler: Arrays haben nicht die gleiche Länge! =====')
        return 0

    delta_y = np.sum(np.absolute(y2 - y1))  # Summe mit Totaler abweichung aller Punkte errechen
    delta_index = 0
    for i in range(1, max_i):               # Signal 1 auf der x-Achse schieben bis zum maximalen delta Index
        y1_new = np.roll(y1,i)
        delta_y_new = np.sum(np.absolute(y2 - y1_new))
        if delta_y_new < delta_y:           # Jedes mal die Totale abweichung vergleichen
            delta_y = delta_y_new
            delta_index = -i
            y1_best = y1_new

    for i in range(1, max_i):               # Signal 1 in die andere richtung schieben auf der x-Achse
        y1_new = np.roll(y1,-i)
        delta_y_new = np.sum(np.absolute(y2 - y1_new))
        if delta_y_new < delta_y:
            delta_y = delta_y_new
            delta_index = i
            y1_best = y1_new                # Am Ende steht in "delta_index" die Position mit der greingsten Abweichung

    if return_index:                        # Es kann nur die Differenz von Indexen herausgegeben werden oder das ganze neue Array
        return delta_index
    else:
        return y1_best


class ADThread(QThread):  # http://doc.qt.io/qt-5/qthread.html
    signal_counter = pyqtSignal(int)  # define new Signal

    def __init__(self, parent=None, function=None):
        super().__init__(parent)
        self.function = function

    def run(self):
        """Wird automatisch durch den Thread aufgerufen."""
        self.function()
        print('[MAIN] terminateing thread...')

    def start_thread(self):
        print('[MAIN] starting thread...')
        self.start(QThread.NormalPriority)

    def stop(self):
        print('[MAIN] stopping thread...')
        self.terminate()


def except_hook(cls, exception, trace_back):
    """Fehlerausgabe in der Python-Konsole anstelle des Terminals."""
    print('[MAIN] Fehler auf Mainebene:')
    print('[MAIN] ' + str(cls) + ' ' + str(exception))
    sys.__excepthook__(cls, exception, trace_back)


if __name__ == '__main__':
    print('[MAIN] shadow builtin print() test')
    print('[MAIN] application started by ' + getpass.getuser())
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('assets/icon/abbts.ico'))
    add_ons.style.set_style(app)
    main = Main()
    main.show()
    sys.exit(app.exec_())
