# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lti.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import matplotlib.pyplot as plt


class Ui_solver(object):
    def setupUi(self, solver):
        self.T = 0.01
        solver.setObjectName("solver")
        solver.resize(808, 390)
        self.centralwidget = QtWidgets.QWidget(solver)
        self.centralwidget.setObjectName("centralwidget")
        self.a_label = QtWidgets.QLabel(self.centralwidget)
        self.a_label.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.a_label.setFont(font)
        self.a_label.setObjectName("a_label")
        self.a_input = QtWidgets.QLineEdit(self.centralwidget)
        self.a_input.setGeometry(QtCore.QRect(150, 22, 631, 31))
        self.a_input.setToolTip("")
        self.a_input.setToolTipDuration(1)
        self.a_input.setStatusTip("")
        self.a_input.setWhatsThis("")
        self.a_input.setObjectName("a_input")
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(30, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_label.setFont(font)
        self.b_label.setObjectName("b_label")
        self.b_input = QtWidgets.QLineEdit(self.centralwidget)
        self.b_input.setGeometry(QtCore.QRect(150, 84, 631, 31))
        self.b_input.setToolTip("")
        self.b_input.setToolTipDuration(1)
        self.b_input.setStatusTip("")
        self.b_input.setWhatsThis("")
        self.b_input.setObjectName("b_input")
        self.unit_pulse = QtWidgets.QPushButton(self.centralwidget)
        self.unit_pulse.setGeometry(QtCore.QRect(30, 230, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unit_pulse.setFont(font)
        self.unit_pulse.setObjectName("unit_pulse")
        self.unit_step = QtWidgets.QPushButton(self.centralwidget)
        self.unit_step.setGeometry(QtCore.QRect(560, 230, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unit_step.setFont(font)
        self.unit_step.setObjectName("unit_step")
        solver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(solver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 20))
        self.menubar.setObjectName("menubar")
        solver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(solver)
        self.statusbar.setObjectName("statusbar")
        solver.setStatusBar(self.statusbar)

        self.unit_pulse.clicked.connect(self.calc_impulse)
        self.unit_step.clicked.connect(self.calc_step)

        self.retranslateUi(solver)
        QtCore.QMetaObject.connectSlotsByName(solver)

    def calc_step(self):
        y = np.zeros(self.n)
        b = np.array(list(map(float, self.b_input.text().split(" "))))
        a = np.array(list(map(float, self.a_input.text().split(" "))))
        u = np.array([x >= len(a) for x in range(self.n)])
        for i in range(len(a), len(y)):
            b_window = u[i-len(b):i]
            grad = np.array([self.history_diff(y[i-x:i])
                             for x in range(1, len(a))])
            y[i] = a[1:].dot(grad)
            y[i] = y[i] + b_window.dot(b)

        plt.plot([x for x in range(self.n)], y)
        plt.show()

    def calc_impulse(self):
        y = np.zeros(self.n)
        b = np.array(list(map(float, self.b_input.text().split(" "))))
        a = np.array(list(map(float, self.a_input.text().split(" "))))
        print(a.shape)
        u = np.array([x == len(a) for x in range(self.n)])
        for i in range(len(a), len(y)):
            b_window = u[i-len(b):i]
            grad = np.array([self.history_diff(y[i-x:i])
                             for x in range(1, len(a))])
            y[i] = a[1:].dot(grad)
            y[i] = y[i] + b_window.dot(b)

        plt.plot([x for x in range(self.n)], y)
        plt.show()

    def history_diff(self, inp):
        if len(inp) == 1:
            return inp[0]

        out = np.zeros(len(inp)-1)
        for i in range(len(out)):
            out[i] = (inp[i+1] - inp[i]) / self.T

        return self.history_diff(out)

    def retranslateUi(self, solver):
        _translate = QtCore.QCoreApplication.translate
        solver.setWindowTitle(_translate("solver", "LTI Solver 1.0"))
        self.a_label.setText(_translate("solver", "Vector a"))
        self.b_label.setText(_translate("solver", "Vector b"))
        self.unit_pulse.setText(_translate("solver", "Unit Impulse"))
        self.unit_step.setText(_translate("solver", "Unit Step"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    ui = Ui_solver()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec_())
