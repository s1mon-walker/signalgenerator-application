# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\entwurf_ui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1276, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 258, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.radioButton_t = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_t.setObjectName("radioButton_t")
        self.verticalLayout_5.addWidget(self.radioButton_t)
        self.radioButton_n = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_n.setObjectName("radioButton_n")
        self.verticalLayout_5.addWidget(self.radioButton_n)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_n_samp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_n_samp.setObjectName("lineEdit_n_samp")
        self.verticalLayout.addWidget(self.lineEdit_n_samp)
        self.lineEdit_t_mess = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_t_mess.setObjectName("lineEdit_t_mess")
        self.verticalLayout.addWidget(self.lineEdit_t_mess)
        self.lineEdit_n_periods = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_n_periods.setObjectName("lineEdit_n_periods")
        self.verticalLayout.addWidget(self.lineEdit_n_periods)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.verticalLayout.addWidget(self.lineEdit_offset)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.checkBox_anteile = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_anteile.setObjectName("checkBox_anteile")
        self.verticalLayout_2.addWidget(self.checkBox_anteile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_sig = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add_sig.setObjectName("btn_add_sig")
        self.horizontalLayout.addWidget(self.btn_add_sig)
        self.btn_del_sig = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_del_sig.setObjectName("btn_del_sig")
        self.horizontalLayout.addWidget(self.btn_del_sig)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_make_sig = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_make_sig.setObjectName("btn_make_sig")
        self.verticalLayout_2.addWidget(self.btn_make_sig)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setEnabled(True)
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
        self.btn_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_2.addWidget(self.btn_start)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(284, 19, 981, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 951, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_11 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget_11.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget_12.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget_13.setStyleSheet("background-color: rgb(148, 148, 148);")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3.addWidget(self.widget_13)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_21 = QtWidgets.QWidget(self.tab_2)
        self.widget_21.setGeometry(QtCore.QRect(10, 10, 961, 381))
        self.widget_21.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.widget_21.setObjectName("widget_21")
        self.widget_22 = QtWidgets.QWidget(self.tab_2)
        self.widget_22.setGeometry(QtCore.QRect(10, 400, 961, 191))
        self.widget_22.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.widget_22.setObjectName("widget_22")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.action_ffne_Konfiguration = QtWidgets.QAction(MainWindow)
        self.action_ffne_Konfiguration.setObjectName("action_ffne_Konfiguration")
        self.actionKonfiguration_speichern = QtWidgets.QAction(MainWindow)
        self.actionKonfiguration_speichern.setObjectName("actionKonfiguration_speichern")
        self.actionAlle_Signale_l_schen = QtWidgets.QAction(MainWindow)
        self.actionAlle_Signale_l_schen.setObjectName("actionAlle_Signale_l_schen")
        self.menuFile.addAction(self.action_ffne_Konfiguration)
        self.menuFile.addAction(self.actionKonfiguration_speichern)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionAlle_Signale_l_schen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Anzahl Samples:"))
        self.radioButton_t.setText(_translate("MainWindow", "Messzeit"))
        self.radioButton_n.setText(_translate("MainWindow", "Anzahl Perioden"))
        self.label_2.setText(_translate("MainWindow", "Offset:"))
        self.checkBox_anteile.setText(_translate("MainWindow", "Anteile sichtbar"))
        self.btn_add_sig.setText(_translate("MainWindow", "Signal hinzufügen"))
        self.btn_del_sig.setText(_translate("MainWindow", "Signal löschen"))
        self.btn_make_sig.setText(_translate("MainWindow", "Erzeuge Signal"))
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
        self.btn_start.setText(_translate("MainWindow", "Starte Messung"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plots einzeln"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Plots kombiniert"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.action_ffne_Konfiguration.setText(_translate("MainWindow", "Öffne Konfiguration"))
        self.actionKonfiguration_speichern.setText(_translate("MainWindow", "Konfiguration speichern"))
        self.actionAlle_Signale_l_schen.setText(_translate("MainWindow", "Alle Signale löschen"))
