# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Asset_Traking.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 211, 91))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.Asset1 = QtWidgets.QPushButton(self.centralwidget)
        self.Asset1.setGeometry(QtCore.QRect(310, 110, 181, 71))
        self.Asset1.setObjectName("Asset1")
        self.Asset2 = QtWidgets.QPushButton(self.centralwidget)
        self.Asset2.setGeometry(QtCore.QRect(310, 230, 181, 81))
        self.Asset2.setObjectName("Asset2")
        self.Asset3 = QtWidgets.QPushButton(self.centralwidget)
        self.Asset3.setGeometry(QtCore.QRect(310, 360, 181, 81))
        self.Asset3.setObjectName("Asset3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 490, 55, 16))
        self.label.setObjectName("label")
        self.Output_lable = QtWidgets.QLabel(self.centralwidget)
        self.Output_lable.setGeometry(QtCore.QRect(320, 480, 181, 31))
        self.Output_lable.setObjectName("Output_lable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Asset1.clicked.connect(self.Output_lable.clear)
        self.Asset2.clicked.connect(self.Output_lable.clear)
        self.Asset3.clicked.connect(self.Output_lable.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asset Tracking System"))
        self.label_2.setText(_translate("MainWindow", "Asset Tracking System"))
        self.Asset1.setText(_translate("MainWindow", "Click Here for Asset 1"))
        self.Asset2.setText(_translate("MainWindow", "Click Here for Asset 2"))
        self.Asset3.setText(_translate("MainWindow", "Click Here for Asset 3"))
        self.label.setText(_translate("MainWindow", "Status"))
        self.Output_lable.setText(_translate("MainWindow", "Please Click above buttons !!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
