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

        self.T_label = QtWidgets.QLabel(self.centralwidget)
        self.T_label.setGeometry(QtCore.QRect(30, 130, 150, 31))
        self.T_label.setFont(font)
        self.T_label.setObjectName("T_label")
        self.T_input = QtWidgets.QLineEdit(self.centralwidget)
        self.T_input.setGeometry(QtCore.QRect(190, 130, 100, 31))
        self.T_input.setToolTip("")
        self.T_input.setToolTipDuration(1)
        self.T_input.setStatusTip("")
        self.T_input.setWhatsThis("")
        self.T_input.setObjectName("T_input")

        self.max_x_label = QtWidgets.QLabel(self.centralwidget)
        self.max_x_label.setGeometry(QtCore.QRect(30, 180, 150, 31))
        self.max_x_label.setFont(font)
        self.max_x_label.setObjectName("max_x")
        self.max_x_input = QtWidgets.QLineEdit(self.centralwidget)
        self.max_x_input.setGeometry(QtCore.QRect(190, 180, 100, 31))
        self.max_x_input.setToolTip("")
        self.max_x_input.setToolTipDuration(1)
        self.max_x_input.setStatusTip("")
        self.max_x_input.setWhatsThis("")
        self.max_x_input.setObjectName("max_x_input")

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

    def full(self, u):
        t = float(self.T_input.text())
        max_x = float(self.max_x_input.text())
        n_points = int(max_x / t)
        B = np.array(
            list(map(float, self.b_input.text().split(" ")))).reshape(-1, 1)
        A = np.array(
            list(map(float, self.a_input.text().split(" ")))).reshape(-1, 1)
        n = len(A)
        X = np.zeros((n, n_points))  # check
        X_0 = np.zeros((n, 1))
        I = np.identity(n)
        C = np.zeros(n)
        C[-1] = 0
        C = C.reshape(1, -1)
        D = B[-1]
        X_ = np.zeros((n, 1))

        for i in range(n_points):
            if i:
                X_ = X[:, i-1]
                X_ = X_.reshape(-1, 1)
            else:
                X_ = np.zeros((n, 1))
                X_ = X_.reshape(-1, 1)
            X[:, i] = np.dot(I + t*A, X_).reshape(-1)
            X[:, i] = X[:, i] + t*B.reshape(-1)

        Y = C.dot(X) + D*u

        plt.plot(np.arange(0, max_x, t), Y.reshape(-1, 1))
        plt.show()

    def calc_step(self):
        self.full("step")

    def calc_impulse(self):
        self.full("impulse")

    def retranslateUi(self, solver):
        _translate = QtCore.QCoreApplication.translate
        solver.setWindowTitle(_translate("solver", "LTI Solver 1.0"))
        self.a_label.setText(_translate("solver", "Vector a"))
        self.b_label.setText(_translate("solver", "Vector b"))
        self.T_label.setText(_translate("solver", "Time Step"))
        self.max_x_label.setText(_translate("solver", "Max X"))
        self.unit_pulse.setText(_translate("solver", "Unit Impulse"))
        self.unit_step.setText(_translate("solver", "Unit Step"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    ui = Ui_solver()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec_())
