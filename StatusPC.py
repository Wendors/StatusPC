# -*- coding: utf-8 -*-

import os
import time
import sys
from datetime import datetime
from pathlib import Path

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class SystemMonitor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setup_timers()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(379, 476)
        
        # Центрування вікна
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        Form.move(screen_geometry.width() - 376, 0)
        
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(
            QtCore.Qt.Tool |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint
        )
        
        # Константи для спрощення розміщення
        self.LABEL_WIDTH = 351
        self.START_X = 10
        self.BAR_START_X = 80
        self.BAR_WIDTH = 281
        
        self._create_time_labels(Form)
        self._create_cpu_labels(Form)
        self._create_ram_labels(Form)
        self._create_disk_labels(Form)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def _create_time_labels(self, Form):
        # Мітка часу
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(self.START_X, -20, self.LABEL_WIDTH, 101))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        
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
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        # Мітка дати
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(self.START_X, 60, self.LABEL_WIDTH, 51))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        
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
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

    def _create_cpu_labels(self, Form):
        # CPU label
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(self.BAR_START_X, 100, 61, 31))
        self._setup_common_label_style(self.label_3, "CPU")
        
        # CPU value
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 141, 31))
        self._setup_common_label_style(self.label_4, "0 %")
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # CPU progress background
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(self.BAR_START_X, 130, self.BAR_WIDTH, 31))
        self._setup_progress_background(self.label_7)
        
        # CPU progress bar
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(self.BAR_START_X, 130, 0, 31))
        self._setup_progress_bar(self.label_8)

    def _create_ram_labels(self, Form):
        # RAM label
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(self.BAR_START_X, 170, 81, 31))
        self._setup_common_label_style(self.label_9, "RAM")
        
        # RAM value
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(220, 170, 141, 31))
        self._setup_common_label_style(self.label_10, "")
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # RAM progress background
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(self.BAR_START_X, 200, self.BAR_WIDTH, 31))
        self._setup_progress_background(self.label_12)
        
        # RAM progress bar
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(self.BAR_START_X, 200, 0, 31))
        self._setup_progress_bar(self.label_13)

    def _create_disk_labels(self, Form):
        # Disk C label
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(self.BAR_START_X, 240, 47, 31))
        
        # Disk C value
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(220, 240, 141, 31))
        self._setup_common_label_style(self.label_15, "")
        self.label_15.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # Disk C total
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(self.BAR_START_X, 270, self.BAR_WIDTH, 31))
        self._setup_disk_total_style(self.label_24)
        
        # Disk C progress background
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(self.BAR_START_X, 270, self.BAR_WIDTH, 31))
        self._setup_progress_background(self.label_17)
        
        # Disk C progress bar
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(self.BAR_START_X, 270, 0, 31))
        self._setup_progress_bar(self.label_18)
        
        # Disk D label
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(self.BAR_START_X, 310, 87, 31))
        
        # Disk D value
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(220, 310, 141, 31))
        self._setup_common_label_style(self.label_20, "")
        self.label_20.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # Disk D total
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(self.BAR_START_X, 340, self.BAR_WIDTH, 31))
        self._setup_disk_total_style(self.label_25)
        
        # Disk D progress background
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(self.BAR_START_X, 340, self.BAR_WIDTH, 31))
        self._setup_progress_background(self.label_22)
        
        # Disk D progress bar
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(self.BAR_START_X, 340, 0, 31))
        self._setup_progress_bar(self.label_23)
        
        # Disk E label (тільки для Windows)
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(self.BAR_START_X, 380, 47, 31))
        
        # Disk E value
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(220, 380, 141, 31))
        self._setup_common_label_style(self.label_29, "")
        self.label_29.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # Disk E total
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(self.BAR_START_X, 410, self.BAR_WIDTH, 31))
        self._setup_disk_total_style(self.label_28)
        
        # Disk E progress background
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(self.BAR_START_X, 410, self.BAR_WIDTH, 31))
        self._setup_progress_background(self.label_26)
        
        # Disk E progress bar
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(self.BAR_START_X, 410, 0, 31))
        self._setup_progress_bar(self.label_27)

    def _setup_common_label_style(self, label, text):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        label.setPalette(palette)
        
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QtGui.QColor(0, 0, 0))
        shadow.setOffset(3)
        label.setGraphicsEffect(shadow)
        
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(True)
        label.setFont(font)
        label.setText(text)

    def _setup_progress_background(self, label):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QtGui.QColor(0, 0, 0))
        shadow.setOffset(3)
        label.setGraphicsEffect(shadow)
        label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, "
            "stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(255, 255, 255, 255), "
            "stop:0.948864 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));"
        )

    def _setup_progress_bar(self, label):
        label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, "
            "stop:0.0511364 rgba(0, 0, 255, 255), stop:0.289773 rgba(85, 255, 255, 255), "
            "stop:0.4375 rgba(255, 255, 255, 255), stop:0.556818 rgba(255, 255, 255, 255), "
            "stop:0.727273 rgba(85, 255, 255, 255), stop:0.943182 rgba(0, 0, 255, 255));"
        )

    def _setup_disk_total_style(self, label):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        label.setPalette(palette)
        
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "System Monitor"))
        
        self.update_time()
        
        if sys.platform == "linux":
            self.label_14.setText(_translate("Form", "/"))
            self.label_19.setText(_translate("Form", "/home"))
            self.label_21.hide()
            self.label_29.hide()
            self.label_26.hide()
            self.label_27.hide()
            self.label_28.hide()
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

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)
        
        months_uk = [
            "січня", "лютого", "березня", "квітня", "травня", "червня",
            "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"
        ]
        
        current_date = datetime.now()
        day = current_date.day
        month_name = months_uk[current_date.month - 1]
        year = current_date.year
        
        self.label_2.setText(f"{day} {month_name} {year}")

    def update_cpu(self):
        cpu_usage = int(psutil.cpu_percent())
        self.label_4.setText(f"{cpu_usage} %")
        
        bar_width = int(cpu_usage * self.BAR_WIDTH / 100)
        self.label_8.setGeometry(QtCore.QRect(self.BAR_START_X, 130, bar_width, 31))

    def update_ram(self):
        ram = psutil.virtual_memory()
        ram_used_gb = ram.used / (1024 ** 3)
        self.label_10.setText(f"{ram_used_gb:.1f} Gb")
        
        bar_width = int(ram.percent * self.BAR_WIDTH / 100)
        self.label_13.setGeometry(QtCore.QRect(self.BAR_START_X, 200, bar_width, 31))

    def update_disk(self):
        GB = 1024 ** 3  # Константа для конвертації в GB
        
        if sys.platform == "linux":
            # Диск /
            try:
                disk_root = psutil.disk_usage('/')
                self.label_15.setText(f"{disk_root.used / GB:.1f} Gb")
                self.label_24.setText(f"{int(disk_root.total / GB)} Gb")
                
                bar_width = int(disk_root.percent * self.BAR_WIDTH / 100)
                self.label_18.setGeometry(QtCore.QRect(self.BAR_START_X, 270, bar_width, 31))
            except Exception as e:
                print(f"Помилка читання диска /: {e}")
            
            # Домашня директорія
            try:
                home_path = os.path.expanduser('~')
                disk_home = psutil.disk_usage(home_path)
                self.label_20.setText(f"{disk_home.used / GB:.1f} Gb")
                self.label_25.setText(f"{int(disk_home.total / GB)} Gb")
                
                bar_width = int(disk_home.percent * self.BAR_WIDTH / 100)
                self.label_23.setGeometry(QtCore.QRect(self.BAR_START_X, 340, bar_width, 31))
            except Exception as e:
                print(f"Помилка читання домашньої директорії: {e}")
                
        else:
            # Windows disks
            disks = psutil.disk_partitions()
            drive_mappings = {'C:\\': None, 'D:\\': None, 'E:\\': None}
            
            for disk in disks:
                if disk.device in drive_mappings:
                    try:
                        usage = psutil.disk_usage(disk.device)
                        drive_mappings[disk.device] = usage
                    except Exception as e:
                        print(f"Помилка читання диска {disk.device}: {e}")
            
            # Disk C
            if drive_mappings['C:\\']:
                disk_c = drive_mappings['C:\\']
                self.label_15.setText(f"{disk_c.used / GB:.1f} Gb")
                self.label_24.setText(f"{int(disk_c.total / GB)} Gb")
                bar_width = int(disk_c.percent * self.BAR_WIDTH / 100)
                self.label_18.setGeometry(QtCore.QRect(self.BAR_START_X, 270, bar_width, 31))
            
            # Disk D
            if drive_mappings['D:\\']:
                disk_d = drive_mappings['D:\\']
                self.label_20.setText(f"{disk_d.used / GB:.1f} Gb")
                self.label_25.setText(f"{int(disk_d.total / GB)} Gb")
                bar_width = int(disk_d.percent * self.BAR_WIDTH / 100)
                self.label_23.setGeometry(QtCore.QRect(self.BAR_START_X, 340, bar_width, 31))
            
            # Disk E
            if drive_mappings['E:\\']:
                disk_e = drive_mappings['E:\\']
                self.label_29.setText(f"{disk_e.used / GB:.1f} Gb")
                self.label_28.setText(f"{int(disk_e.total / GB)} Gb")
                bar_width = int(disk_e.percent * self.BAR_WIDTH / 100)
                self.label_27.setGeometry(QtCore.QRect(self.BAR_START_X, 410, bar_width, 31))

    def _setup_timers(self):
        # Таймер для оновлення часу
        self.timer_time = QtCore.QTimer()
        self.timer_time.setInterval(1000)
        self.timer_time.timeout.connect(self.update_time)
        self.timer_time.start()
        
        # Таймер для оновлення CPU
        self.timer_cpu = QtCore.QTimer()
        self.timer_cpu.setInterval(500)
        self.timer_cpu.timeout.connect(self.update_cpu)
        self.timer_cpu.start()
        
        # Таймер для оновлення RAM
        self.timer_ram = QtCore.QTimer()
        self.timer_ram.setInterval(1000)
        self.timer_ram.timeout.connect(self.update_ram)
        self.timer_ram.start()
        
        # Таймер для оновлення дисків
        self.timer_disk = QtCore.QTimer()
        self.timer_disk.setInterval(2000)
        self.timer_disk.timeout.connect(self.update_disk)
        self.timer_disk.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    monitor = SystemMonitor()
    monitor.show()
    
    sys.exit(app.exec_())
