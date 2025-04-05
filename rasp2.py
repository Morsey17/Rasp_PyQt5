from base_class import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Расписание")
        MainWindow.resize(1800, 980)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_clas = []
        self.label_clas = []
        self.groupBox_clas_urok = []
        self.label_clas_urok = []
        self.groupBox_teach = []
        self.label_teach = []
        self.groupBox_teach_urok = []
        self.label_teach_urok = []
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """
    def addWidget(self):
        for i in range(3):
            self.groupBox_clas.append(QtWidgets.QGroupBox(self.centralwidget))
            self.groupBox_clas[i].setGeometry(QtCore.QRect(100, i * 180 + (i + 1) * 20, 180, 180))
            self.groupBox_clas[i].setObjectName("groupBox_clas" + str(i))
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
