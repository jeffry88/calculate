# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Jul 30 10:58:21 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setWhatsThis(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 130, 397, 361))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcd = QtGui.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd.setFont(font)
        self.lcd.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd.setDigitCount(10)
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.verticalLayout.addWidget(self.lcd)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.number9 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number9.setFont(font)
        self.number9.setObjectName(_fromUtf8("number9"))
        self.horizontalLayout.addWidget(self.number9)
        self.number8 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number8.setFont(font)
        self.number8.setObjectName(_fromUtf8("number8"))
        self.horizontalLayout.addWidget(self.number8)
        self.number7 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number7.setFont(font)
        self.number7.setObjectName(_fromUtf8("number7"))
        self.horizontalLayout.addWidget(self.number7)
        self.add = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.add.setFont(font)
        self.add.setObjectName(_fromUtf8("add"))
        self.horizontalLayout.addWidget(self.add)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.number6 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number6.setFont(font)
        self.number6.setObjectName(_fromUtf8("number6"))
        self.horizontalLayout_2.addWidget(self.number6)
        self.number5 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number5.setFont(font)
        self.number5.setObjectName(_fromUtf8("number5"))
        self.horizontalLayout_2.addWidget(self.number5)
        self.number4 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number4.setFont(font)
        self.number4.setObjectName(_fromUtf8("number4"))
        self.horizontalLayout_2.addWidget(self.number4)
        self.sub = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.sub.setFont(font)
        self.sub.setObjectName(_fromUtf8("sub"))
        self.horizontalLayout_2.addWidget(self.sub)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.number3 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number3.setFont(font)
        self.number3.setObjectName(_fromUtf8("number3"))
        self.horizontalLayout_3.addWidget(self.number3)
        self.number2 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number2.setFont(font)
        self.number2.setObjectName(_fromUtf8("number2"))
        self.horizontalLayout_3.addWidget(self.number2)
        self.number1 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number1.setFont(font)
        self.number1.setObjectName(_fromUtf8("number1"))
        self.horizontalLayout_3.addWidget(self.number1)
        self.mult = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.mult.setFont(font)
        self.mult.setObjectName(_fromUtf8("mult"))
        self.horizontalLayout_3.addWidget(self.mult)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.number0 = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.number0.setFont(font)
        self.number0.setObjectName(_fromUtf8("number0"))
        self.horizontalLayout_4.addWidget(self.number0)
        self.point = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.point.setFont(font)
        self.point.setObjectName(_fromUtf8("point"))
        self.horizontalLayout_4.addWidget(self.point)
        self.clear = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.clear.setFont(font)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.horizontalLayout_4.addWidget(self.clear)
        self.exc = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.exc.setFont(font)
        self.exc.setObjectName(_fromUtf8("exc"))
        self.horizontalLayout_4.addWidget(self.exc)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.result = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.result.setFont(font)
        self.result.setObjectName(_fromUtf8("result"))
        self.verticalLayout.addWidget(self.result)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "简易计算器", None))
        self.number9.setText(_translate("MainWindow", "9", None))
        self.number8.setText(_translate("MainWindow", "8", None))
        self.number7.setText(_translate("MainWindow", "7", None))
        self.add.setText(_translate("MainWindow", "+", None))
        self.number6.setText(_translate("MainWindow", "6", None))
        self.number5.setText(_translate("MainWindow", "5", None))
        self.number4.setText(_translate("MainWindow", "4", None))
        self.sub.setText(_translate("MainWindow", "-", None))
        self.number3.setText(_translate("MainWindow", "3", None))
        self.number2.setText(_translate("MainWindow", "2", None))
        self.number1.setText(_translate("MainWindow", "1", None))
        self.mult.setText(_translate("MainWindow", "*", None))
        self.number0.setText(_translate("MainWindow", "0", None))
        self.point.setText(_translate("MainWindow", ".", None))
        self.clear.setText(_translate("MainWindow", "C", None))
        self.exc.setText(_translate("MainWindow", "/", None))
        self.result.setText(_translate("MainWindow", "=", None))
