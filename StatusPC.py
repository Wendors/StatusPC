# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import time
from re import T

# import winreg
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(379, 476)
        self.disctop = QtWidgets.QApplication.desktop()
        Form.move(int(self.disctop.width() - 376), 0)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(
            QtCore.Qt.Tool
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnBottomHint
        )
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, -20, 351, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label.setPalette(palette)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(2)
        self.shadow.setColor(QtGui.QColor(0, 0, 0))
        self.shadow.setOffset(5)
        self.label.setGraphicsEffect(self.shadow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 351, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.shadow_2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_2.setBlurRadius(2)
        self.shadow_2.setOffset(4)
        self.shadow_2.setColor(QtGui.QColor(0, 0, 0))
        self.label_2.setGraphicsEffect(self.shadow_2)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 61, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        self.shadow_3 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_3.setBlurRadius(2)
        self.shadow_3.setOffset(3)
        self.shadow_3.setColor(QtGui.QColor(0, 0, 0))
        self.label_3.setGraphicsEffect(self.shadow_3)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        self.shadow_4 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_4.setBlurRadius(2)
        self.shadow_4.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_4.setOffset(3)
        self.label_4.setGraphicsEffect(self.shadow_4)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 150, 261, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 130, 281, 31))
        self.shadow_7 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_7.setBlurRadius(2)
        self.shadow_7.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_7.setOffset(3)
        self.label_7.setGraphicsEffect(self.shadow_7)
        self.label_7.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 130, 0, 31))
        self.label_8.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(80, 170, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        self.shadow_9 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_9.setBlurRadius(2)
        self.shadow_9.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_9.setOffset(3)
        self.label_9.setGraphicsEffect(self.shadow_9)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(220, 170, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        self.shadow_10 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_10.setBlurRadius(2)
        self.shadow_10.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_10.setOffset(3)
        self.label_10.setGraphicsEffect(self.shadow_10)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(80, 200, 281, 31))
        self.shadow_12 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_12.setBlurRadius(2)
        self.shadow_12.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_12.setOffset(3)
        self.label_12.setGraphicsEffect(self.shadow_12)
        self.label_12.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(80, 200, 0, 31))
        self.label_13.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(80, 240, 47, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_14.setPalette(palette)
        self.shadow_14 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_14.setBlurRadius(2)
        self.shadow_14.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_14.setOffset(3)
        self.label_14.setGraphicsEffect(self.shadow_14)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(220, 240, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_15.setPalette(palette)
        self.shadow_15 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_15.setBlurRadius(2)
        self.shadow_15.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_15.setOffset(3)
        self.label_15.setGraphicsEffect(self.shadow_15)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(80, 270, 281, 31))
        self.shadow_17 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_17.setBlurRadius(2)
        self.shadow_17.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_17.setOffset(3)
        self.label_17.setGraphicsEffect(self.shadow_17)
        self.label_17.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(80, 270, 0, 31))
        self.label_18.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(80, 310, 87, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_19.setPalette(palette)
        self.shadow_19 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_19.setBlurRadius(2)
        self.shadow_19.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_19.setOffset(3)
        self.label_19.setGraphicsEffect(self.shadow_19)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(220, 310, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_20.setPalette(palette)
        self.shadow_20 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_20.setBlurRadius(2)
        self.shadow_20.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_20.setOffset(3)
        self.label_20.setGraphicsEffect(self.shadow_20)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(80, 340, 281, 31))
        self.shadow_22 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_22.setBlurRadius(2)
        self.shadow_22.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_22.setOffset(3)
        self.label_22.setGraphicsEffect(self.shadow_22)
        self.label_22.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(80, 340, 0, 31))
        self.label_23.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(80, 270, 281, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_24.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(80, 340, 281, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_25.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(80, 380, 47, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_21.setPalette(palette)
        self.shadow_21 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_21.setBlurRadius(2)
        self.shadow_21.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_21.setOffset(3)
        self.label_21.setGraphicsEffect(self.shadow_21)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(220, 380, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_29.setPalette(palette)
        self.shadow_29 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_29.setBlurRadius(2)
        self.shadow_29.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_29.setOffset(3)
        self.label_29.setGraphicsEffect(self.shadow_29)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_29.setObjectName("label_29")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(80, 410, 281, 31))
        self.shadow_26 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_26.setBlurRadius(2)
        self.shadow_26.setColor(QtGui.QColor(0, 0, 0))
        self.shadow_26.setOffset(3)
        self.label_26.setGraphicsEffect(self.shadow_26)
        self.label_26.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(80, 410, 0, 31))
        self.label_27.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(80, 410, 281, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_28.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "StatusPC"))
        self.label.setText(_translate("Form", "{0}".format(time.strftime("%H:%M:%S"))))
        self.mons = [
            "січеня",
            "лютого",
            "березеня",
            "квітеня",
            "травеня",
            "червеня",
            "липеня",
            "серпеня",
            "вересеня",
            "жовтеня",
            "листопада",
            "груденя",
        ]
        self.dey = time.strftime("%d")
        self.muns = time.strftime("%m")
        self.year = time.strftime("%Y")
        if int(self.dey[0:1]) == 0:
            self.dey = self.dey[1]
        else:
            self.dey = self.dey
        if int(self.muns[0:1]) == 0:
            self.muns = self.muns[1]
        else:
            self.muns = self.muns
        self.label_2.setText(
            _translate(
                "Form",
                "{0} {1} {2}".format(
                    self.dey, self.mons[int(self.muns) - 1], self.year
                ),
            )
        )
        self.label_3.setText(_translate("Form", "CPU"))
        self.label_4.setText(_translate("Form", "0 %"))
        self.label_9.setText(_translate("Form", "RAM"))
        self.label_10.setText(_translate("Form", ""))
        if sys.platform == "linux":
            self.label_14.setText(_translate("Form", "/"))
            self.label_19.setText(_translate("Form", "/home"))
            self.label_21.hide()
            self.label_29.hide()
            self.label_26.hide()
            self.label_27.hide()
            self.label_28.hide()
            self.label_19.hide()
            self.label_20.hide()
            self.label_22.hide()
            self.label_23.hide()
            self.label_25.hide()
        else:
            self.label_14.setText(_translate("Form", "C:\\"))
            self.label_19.setText(_translate("Form", "D:\\"))
            self.label_21.setText(_translate("Form", "E:\\"))
            self.label_15.setText(_translate("Form", ""))
            self.label_20.setText(_translate("Form", ""))
            self.label_24.setText(_translate("Form", ""))
            self.label_25.setText(_translate("Form", ""))
            self.label_29.setText(_translate("Form", ""))
            self.label_28.setText(_translate("Form", ""))

    def Taime_(self):
        self.time = time.strftime("%H:%M:%S")
        self.label.setText(self.time)
        self.mons = [
            "січня",
            "лютого",
            "березня",
            "квітня",
            "травня",
            "червня",
            "липня",
            "серпня",
            "вересня",
            "жовтня",
            "листопада",
            "грудня",
        ]
        self.dey = time.strftime("%d")
        self.muns = time.strftime("%m")
        self.year = time.strftime("%Y")
        if int(self.dey[0:1]) == 0:
            self.dey = self.dey[1]
        else:
            self.dey = self.dey
        if int(self.muns[0:1]) == 0:
            self.muns = self.muns[1]
        else:
            self.muns = self.muns
        self.label_2.setText(
            "{0} {1} {2}".format(self.dey, self.mons[int(self.muns) - 1], self.year)
        )

    def Cpu_(self):
        self.cpu = int(psutil.cpu_percent())
        self.label_4.setText("{0} %".format(self.cpu))
        self.cx = self.cpu
        self.cx = int(self.cx * 281 / 100)
        self.label_8.setGeometry(QtCore.QRect(80, 130, self.cx, 31))

    def Ram_(self):
        self.ram = psutil.virtual_memory()
        self.ramu = self.ram.used
        self.label_10.setText("{0} Gb".format(str(self.ramu)[0:4]))
        self.ramc = int(int(self.ram.percent) * 291 / 100)
        self.label_13.setGeometry(QtCore.QRect(80, 200, self.ramc, 31))

    def Disk_(self):
        self.disks = psutil.disk_partitions()
        self.listdisk = []
        if sys.platform == "linux":
            self.driv_ = "/"
            self.driv_H = str(os.environ["HOME"])
            self.listdisk = [self.driv_, self.driv_H]
            for i in self.listdisk:
                if i == self.driv_:
                    self.disk_c = psutil.disk_usage(i)
                    self.label_15.setText(
                        "{0} Gb".format(round(float(self.disk_c.used) / 1000000000, 1))
                    )
                    self.label_24.setText(
                        "{0} Gb".format(int(self.disk_c.total / 1000000000))
                    )
                    self.cpro = int(self.disk_c.percent) * 291 / 100
                    self.label_18.setGeometry(QtCore.QRect(80, 270, int(self.cpro), 31))

        else:
            self.driv_ = str(os.environ["SYSTEMDRIVE"])
            self.driv_H = "D:\\"
            for i in self.disks:
                if i.opts == "rw,fixed":
                    self.listdisk.append(i.device)
                for i in self.listdisk:
                    if (
                        i == self.driv_
                    ):  #  str(os.environ["SYSTEMDRIVE"]) + "\\" --для WINDOWS
                        self.disk_c = psutil.disk_usage(i)
                        self.label_15.setText(
                            "{0} Gb".format(
                                round(float(self.disk_c.used) / 1000000000, 1)
                            )
                        )
                        self.label_24.setText(
                            "{0} Gb".format(int(self.disk_c.total / 1000000000))
                        )
                        self.cpro = int(self.disk_c.percent) * 291 / 100
                        self.label_18.setGeometry(
                            QtCore.QRect(80, 270, int(self.cpro), 31)
                        )
                    if i == self.driv_H:
                        self.disk_d = psutil.disk_usage(i)
                        self.label_20.setText(
                            "{0} Gb".format(
                                round(float(self.disk_d.used) / 1000000000, 1)
                            )
                        )
                        self.label_25.setText(
                            "{0} Gb".format(int(self.disk_d.total / 1000000000))
                        )
                        self.dpro = int(self.disk_d.percent) * 291 / 100
                        self.label_23.setGeometry(
                            QtCore.QRect(80, 340, int(self.dpro), 31)
                        )
                    if i == "E:\\":
                        self.disk_e = psutil.disk_usage(i)
                        self.label_29.setText(
                            "{0} Gb".format(
                                round(float(self.disk_e.used) / 1000000000, 1)
                            )
                        )
                        self.label_28.setText(
                            "{0} Gb".format(int(self.disk_e.total / 1000000000))
                        )
                        self.epro = int(self.disk_e.percent) * 291 / 100
                        self.label_27.setGeometry(QtCore.QRect(80, 410, self.epro, 31))

    def _Udate(self):
        # Переопридиления  Time
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.Taime_)
        self.timer.start()
        # Переопридиления  CPU
        self.timer_2 = QtCore.QTimer()
        self.timer_2.setInterval(500)
        self.timer_2.setSingleShot(False)
        self.timer_2.timeout.connect(self.Cpu_)
        self.timer_2.start()
        # Переопридиления RAM
        self.timer_3 = QtCore.QTimer()
        self.timer_3.setInterval(1000)
        self.timer_2.setSingleShot(False)
        self.timer_3.timeout.connect(self.Ram_)
        self.timer_3.start()
        # Переопридиления Disk
        self.timer_4 = QtCore.QTimer()
        self.timer_4.setInterval(1000)
        self.timer_4.setSingleShot(False)
        self.timer_4.timeout.connect(self.Disk_)
        self.timer_4.start()


if __name__ == "__main__":
    import sys

    """
    try:
        regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(mykeys, 'StatisPC')
        winreg.CloseKey(self.mykeys)
    except:
        pass
    regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(mykeys, 'StatisPC', 0, winreg.REG_SZ, '"' + sys.argv[0].replace('\\', '\\\\') + '"' + " Minimum")
    winreg.CloseKey(mykeys)
    """

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui._Udate()
    Form.show()
    sys.exit(app.exec_())
