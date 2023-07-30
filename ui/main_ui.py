# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.radioButton_t = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_t.setObjectName("radioButton_t")
        self.verticalLayout_5.addWidget(self.radioButton_t)
        self.radioButton_n = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_n.setObjectName("radioButton_n")
        self.verticalLayout_5.addWidget(self.radioButton_n)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_n_samp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n_samp.setObjectName("lineEdit_n_samp")
        self.verticalLayout.addWidget(self.lineEdit_n_samp)
        self.lineEdit_t_mess = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_t_mess.setObjectName("lineEdit_t_mess")
        self.verticalLayout.addWidget(self.lineEdit_t_mess)
        self.lineEdit_n_periods = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n_periods.setText("")
        self.lineEdit_n_periods.setObjectName("lineEdit_n_periods")
        self.verticalLayout.addWidget(self.lineEdit_n_periods)
        self.lineEdit_faktor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_faktor.setObjectName("lineEdit_faktor")
        self.verticalLayout.addWidget(self.lineEdit_faktor)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.verticalLayout.addWidget(self.lineEdit_offset)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.checkBox_anteile = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_anteile.setObjectName("checkBox_anteile")
        self.verticalLayout_2.addWidget(self.checkBox_anteile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_sig = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_sig.setObjectName("btn_add_sig")
        self.horizontalLayout.addWidget(self.btn_add_sig)
        self.btn_del_sig = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_sig.setObjectName("btn_del_sig")
        self.horizontalLayout.addWidget(self.btn_del_sig)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_make_sig = QtWidgets.QPushButton(self.centralwidget)
        self.btn_make_sig.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_make_sig.setObjectName("btn_make_sig")
        self.verticalLayout_2.addWidget(self.btn_make_sig)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("func")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_2.addWidget(self.btn_start)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_verstaerkung = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_verstaerkung.setObjectName("lineEdit_verstaerkung")
        self.horizontalLayout_2.addWidget(self.lineEdit_verstaerkung)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_phase = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phase.setObjectName("lineEdit_phase")
        self.horizontalLayout_2.addWidget(self.lineEdit_phase)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_7.addLayout(self.verticalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.tab_1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.horizontalLayout_4.addWidget(self.horizontalSlider_1)
        self.label_12 = QtWidgets.QLabel(self.tab_1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_6.addLayout(self.verticalLayout_21)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_5.addWidget(self.horizontalSlider_2)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuBearbeiten = QtWidgets.QMenu(self.menubar)
        self.menuBearbeiten.setObjectName("menuBearbeiten")
        self.menuEinstellungen = QtWidgets.QMenu(self.menubar)
        self.menuEinstellungen.setObjectName("menuEinstellungen")
        self.menuKanal_w_hlen = QtWidgets.QMenu(self.menuEinstellungen)
        self.menuKanal_w_hlen.setObjectName("menuKanal_w_hlen")
        self.menuAnsicht = QtWidgets.QMenu(self.menubar)
        self.menuAnsicht.setObjectName("menuAnsicht")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAlle_Signale_del = QtWidgets.QAction(MainWindow)
        self.actionAlle_Signale_del.setObjectName("actionAlle_Signale_del")
        self.actionConfig_speichern = QtWidgets.QAction(MainWindow)
        self.actionConfig_speichern.setObjectName("actionConfig_speichern")
        self.actionConfig_laden = QtWidgets.QAction(MainWindow)
        self.actionConfig_laden.setObjectName("actionConfig_laden")
        self.actionSchliessen = QtWidgets.QAction(MainWindow)
        self.actionSchliessen.setObjectName("actionSchliessen")
        self.actionExport_als_csv = QtWidgets.QAction(MainWindow)
        self.actionExport_als_csv.setObjectName("actionExport_als_csv")
        self.actionExport_als_png = QtWidgets.QAction(MainWindow)
        self.actionExport_als_png.setObjectName("actionExport_als_png")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionAD_verbinden = QtWidgets.QAction(MainWindow)
        self.actionAD_verbinden.setObjectName("actionAD_verbinden")
        self.actionErweiterte_Fourierreihe = QtWidgets.QAction(MainWindow)
        self.actionErweiterte_Fourierreihe.setObjectName("actionErweiterte_Fourierreihe")
        self.actionKannal_1 = QtWidgets.QAction(MainWindow)
        self.actionKannal_1.setCheckable(True)
        self.actionKannal_1.setChecked(True)
        self.actionKannal_1.setObjectName("actionKannal_1")
        self.actionKannal_2 = QtWidgets.QAction(MainWindow)
        self.actionKannal_2.setCheckable(True)
        self.actionKannal_2.setObjectName("actionKannal_2")
        self.actionNeu = QtWidgets.QAction(MainWindow)
        self.actionNeu.setObjectName("actionNeu")
        self.actionAnzahl_Samples_nur_2er_Potenzen = QtWidgets.QAction(MainWindow)
        self.actionAnzahl_Samples_nur_2er_Potenzen.setCheckable(True)
        self.actionAnzahl_Samples_nur_2er_Potenzen.setChecked(True)
        self.actionAnzahl_Samples_nur_2er_Potenzen.setObjectName("actionAnzahl_Samples_nur_2er_Potenzen")
        self.actionPlot_Ordinate_beschriften = QtWidgets.QAction(MainWindow)
        self.actionPlot_Ordinate_beschriften.setCheckable(True)
        self.actionPlot_Ordinate_beschriften.setChecked(True)
        self.actionPlot_Ordinate_beschriften.setObjectName("actionPlot_Ordinate_beschriften")
        self.actionPlot_Abszisse_beschriften = QtWidgets.QAction(MainWindow)
        self.actionPlot_Abszisse_beschriften.setCheckable(True)
        self.actionPlot_Abszisse_beschriften.setObjectName("actionPlot_Abszisse_beschriften")
        self.menuDatei.addAction(self.actionNeu)
        self.menuDatei.addAction(self.actionConfig_speichern)
        self.menuDatei.addAction(self.actionConfig_laden)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionExport_als_png)
        self.menuDatei.addAction(self.actionExport_als_csv)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionSchliessen)
        self.menuBearbeiten.addAction(self.actionAlle_Signale_del)
        self.menuBearbeiten.addAction(self.actionErweiterte_Fourierreihe)
        self.menuKanal_w_hlen.addAction(self.actionKannal_1)
        self.menuKanal_w_hlen.addAction(self.actionKannal_2)
        self.menuEinstellungen.addAction(self.actionAD_verbinden)
        self.menuEinstellungen.addAction(self.menuKanal_w_hlen.menuAction())
        self.menuEinstellungen.addAction(self.actionAnzahl_Samples_nur_2er_Potenzen)
        self.menuEinstellungen.addSeparator()
        self.menuEinstellungen.addAction(self.actionPlot_Ordinate_beschriften)
        self.menuEinstellungen.addAction(self.actionPlot_Abszisse_beschriften)
        self.menuAnsicht.addAction(self.actionDark_Mode)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuBearbeiten.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())
        self.menubar.addAction(self.menuEinstellungen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Anzahl Samples:"))
        self.radioButton_t.setText(_translate("MainWindow", "Messzeit:"))
        self.radioButton_n.setText(_translate("MainWindow", "Anzahl Perioden:"))
        self.label_3.setText(_translate("MainWindow", "Faktor:"))
        self.label_2.setText(_translate("MainWindow", "Offset:"))
        self.lineEdit_n_samp.setToolTip(_translate("MainWindow", "Anzahl Samples des Signalgenerator in 2er Pozenten"))
        self.lineEdit_t_mess.setToolTip(_translate("MainWindow", "Messzeit des gesammten Signals"))
        self.lineEdit_n_periods.setToolTip(_translate("MainWindow", "Anzahl Perioden des ersten Signals"))
        self.lineEdit_faktor.setToolTip(_translate("MainWindow", "Faktor über das gesammte Signal"))
        self.lineEdit_offset.setToolTip(_translate("MainWindow", "Offset des Signals in Volt"))
        self.checkBox_anteile.setToolTip(_translate("MainWindow", "Zeigt die Anteile der Fourierreihe als Einzelplots"))
        self.checkBox_anteile.setText(_translate("MainWindow", "Anteile sichtbar"))
        self.btn_add_sig.setToolTip(_translate("MainWindow", "Neues Signal zur Liste hinzufügen"))
        self.btn_add_sig.setText(_translate("MainWindow", "Signal hinzufügen"))
        self.btn_del_sig.setToolTip(_translate("MainWindow", "Letztes Signal aus der Liste löschen"))
        self.btn_del_sig.setText(_translate("MainWindow", "Signal löschen"))
        self.btn_make_sig.setToolTip(_translate("MainWindow", "Fourierreihe erstellen und Signalsgenerator konfigurieren"))
        self.btn_make_sig.setText(_translate("MainWindow", "Erzeuge Signal"))
        self.tableWidget.setToolTip(_translate("MainWindow", "Funktionen in der Tabelle werden zur Fourierreihe addiert"))
        self.tableWidget.setStatusTip(_translate("MainWindow", "Mögliche Signale: sin, cos, square, triangle, rampup, rampdown"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "sin"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "0"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_start.setToolTip(_translate("MainWindow", "Signalgenerator und Osziloskop starten"))
        self.btn_start.setText(_translate("MainWindow", "Starte Messung"))
        self.label_4.setText(_translate("MainWindow", "Verstärkung:"))
        self.label_5.setText(_translate("MainWindow", "dB     Phasenversatz:"))
        self.label_6.setText(_translate("MainWindow", "°"))
        self.label_11.setText(_translate("MainWindow", "F min"))
        self.label_12.setText(_translate("MainWindow", "F max"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Plots einzeln"))
        self.label_21.setText(_translate("MainWindow", "F min"))
        self.label_22.setText(_translate("MainWindow", "F max"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Plots kombiniert"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuBearbeiten.setTitle(_translate("MainWindow", "Bearbeiten"))
        self.menuEinstellungen.setTitle(_translate("MainWindow", "Einstellungen"))
        self.menuKanal_w_hlen.setTitle(_translate("MainWindow", "Signalgenerator Kanal wählen"))
        self.menuAnsicht.setTitle(_translate("MainWindow", "Ansicht"))
        self.actionAlle_Signale_del.setText(_translate("MainWindow", "Alle Signale löschen"))
        self.actionConfig_speichern.setText(_translate("MainWindow", "Konfiguration speichern"))
        self.actionConfig_laden.setText(_translate("MainWindow", "Konfiguration laden"))
        self.actionSchliessen.setText(_translate("MainWindow", "Schliessen"))
        self.actionExport_als_csv.setText(_translate("MainWindow", "Export als .csv"))
        self.actionExport_als_png.setText(_translate("MainWindow", "Export als .png"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionDark_Mode.setToolTip(_translate("MainWindow", "Stil der Anwendung"))
        self.actionDark_Mode.setStatusTip(_translate("MainWindow", "Wird nach abspeichern der Konfiguration und neustart der Applikation übernommen"))
        self.actionAD_verbinden.setText(_translate("MainWindow", "Analog Discovery verbinden"))
        self.actionErweiterte_Fourierreihe.setText(_translate("MainWindow", "Konvertiere zu Sinusreihe"))
        self.actionKannal_1.setText(_translate("MainWindow", "Kannal 1"))
        self.actionKannal_2.setText(_translate("MainWindow", "Kannal 2"))
        self.actionNeu.setText(_translate("MainWindow", "Neu"))
        self.actionAnzahl_Samples_nur_2er_Potenzen.setText(_translate("MainWindow", "Anzahl Samples nur 2er Potenzen"))
        self.actionPlot_Ordinate_beschriften.setText(_translate("MainWindow", "Plot Ordinate beschriften"))
        self.actionPlot_Abszisse_beschriften.setText(_translate("MainWindow", "Plot Abszisse beschriften"))