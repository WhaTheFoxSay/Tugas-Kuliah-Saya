# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorInan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 181)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(52, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_1.clicked.connect(self.lineEdit_1.clear)
        self.pushButton_1.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_1.clicked.connect(self.lineEdit_3.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_2.setText(_translate("MainWindow", "------------ Ferdinan Rizky Budiarto [1002220005] ------------"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.comboBox.setItemText(4, _translate("MainWindow", "%"))
        self.comboBox.setItemText(5, _translate("MainWindow", "mod"))
        self.comboBox.setItemText(6, _translate("MainWindow", "^"))
        self.label.setText(_translate("MainWindow", "="))
        self.pushButton_1.setText(_translate("MainWindow", "Hapus"))
        self.pushButton_2.setText(_translate("MainWindow", "Itung"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
