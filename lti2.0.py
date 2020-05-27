# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lti2.0.ui'
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
        self.unit_pulse.setGeometry(QtCore.QRect(30, 260, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unit_pulse.setFont(font)
        self.unit_pulse.setObjectName("unit_pulse")
        self.unit_step = QtWidgets.QPushButton(self.centralwidget)
        self.unit_step.setGeometry(QtCore.QRect(560, 260, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unit_step.setFont(font)
        self.unit_step.setObjectName("unit_step")
        self.T_label = QtWidgets.QLabel(self.centralwidget)
        self.T_label.setGeometry(QtCore.QRect(30, 150, 101, 16))
        self.T_label.setObjectName("T_label")
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setGeometry(QtCore.QRect(30, 190, 111, 16))
        self.p_label.setObjectName("p_label")
        self.n_label = QtWidgets.QLabel(self.centralwidget)
        self.n_label.setGeometry(QtCore.QRect(30, 230, 111, 16))
        self.n_label.setObjectName("n_label")
        self.T_input = QtWidgets.QLineEdit(self.centralwidget)
        self.T_input.setGeometry(QtCore.QRect(160, 150, 113, 23))
        self.T_input.setObjectName("T_input")
        self.p_input = QtWidgets.QLineEdit(self.centralwidget)
        self.p_input.setGeometry(QtCore.QRect(160, 190, 113, 23))
        self.p_input.setObjectName("p_input")
        self.n_input = QtWidgets.QLineEdit(self.centralwidget)
        self.n_input.setGeometry(QtCore.QRect(160, 230, 113, 23))
        self.n_input.setObjectName("n_input")
        solver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(solver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 20))
        self.menubar.setObjectName("menubar")
        solver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(solver)
        self.statusbar.setObjectName("statusbar")
        solver.setStatusBar(self.statusbar)

        self.retranslateUi(solver)
        QtCore.QMetaObject.connectSlotsByName(solver)

        self.unit_pulse.clicked.connect(self.calc_impulse)
        self.unit_step.clicked.connect(self.calc_step)

    def calc_step(self):
        T = float(self.T_input.text())
        max_x = float(self.n_input.text())
        n_points = int(self.p_input.text())

        y = np.zeros(n_points)
        b = np.array(list(map(float, self.b_input.text().split(" "))))
        a = np.array(list(map(float, self.a_input.text().split(" "))))
        u = np.array([float(x >= len(a)) for x in np.arange(-2*T, max_x, T)])
        for i in range(len(a), len(y)):
            b_window = u[i-len(b):i]
            grad = np.array([self.history_diff(y[i:i+x])
                             for x in range(1, len(a))])
            print(grad)
            y[i] = a[1:].dot(grad)
            y[i] = y[i] + b_window.dot(b)

        xs = np.arange(0, max_x, T)
        plt.plot(xs[:n_points], y)
        plt.show()

    def calc_impulse(self):
        T = float(self.T_input.text())
        max_x = float(self.n_input.text())
        n_points = int(self.p_input.text())
        y = np.zeros(int(max_x / T))
        b = np.array(list(map(float, self.b_input.text().split(" "))))
        a = np.array(list(map(float, self.a_input.text().split(" "))))
        u = np.array([float(x == 0) for x in np.arange(-2*T, max_x, T)])
        for i in range(len(a), len(y)):
            b_window = u[i-len(b):i]
            grad = np.array([self.history_diff(y[i:i+x])
                             for x in range(1, len(a))])
            print(i)
            y[i] = a[1:].dot(grad)
            y[i] = y[i] + b_window.dot(b)

        xs = np.arange(0, max_x, T)
        plt.plot(xs[:n_points], y[:n_points])
        plt.show()

    def history_diff(self, inp):
        T = float(self.T_input.text())
        if len(inp) == 1:
            return inp[0]

        out = np.zeros(len(inp)-1)
        for i in range(len(out)):
            out[i] = (inp[i+1] - inp[i]) / T

        return self.history_diff(out)

    def retranslateUi(self, solver):
        _translate = QtCore.QCoreApplication.translate
        solver.setWindowTitle(_translate("solver", "LTI Solver 2.0"))
        self.a_label.setText(_translate("solver", "Vector a"))
        self.b_label.setText(_translate("solver", "Vector b"))
        self.unit_pulse.setText(_translate("solver", "Unit Impulse"))
        self.unit_step.setText(_translate("solver", "Unit Step"))
        self.T_label.setText(_translate("solver", "Time Step T"))
        self.p_label.setText(_translate("solver", "Number of points"))
        self.n_label.setText(_translate("solver", "Max x value"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    ui = Ui_solver()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec_())
