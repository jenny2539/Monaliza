# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.Circle_button = QtGui.QPushButton(self.tab)
        self.Circle_button.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.Circle_button.setObjectName(_fromUtf8("Circle_button"))
        self.Line_button = QtGui.QPushButton(self.tab)
        self.Line_button.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.Line_button.setObjectName(_fromUtf8("Line_button"))
        self.Go_to_position_button = QtGui.QPushButton(self.tab)
        self.Go_to_position_button.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.Go_to_position_button.setObjectName(_fromUtf8("Go_to_position_button"))
        self.Grap_pen_button = QtGui.QPushButton(self.tab)
        self.Grap_pen_button.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.Grap_pen_button.setObjectName(_fromUtf8("Grap_pen_button"))
        self.Get_position_button = QtGui.QPushButton(self.tab)
        self.Get_position_button.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.Get_position_button.setObjectName(_fromUtf8("Get_position_button"))
        self.Reset_button = QtGui.QPushButton(self.tab)
        self.Reset_button.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.Reset_button.setObjectName(_fromUtf8("Reset_button"))
        self.Circle_X = QtGui.QSpinBox(self.tab)
        self.Circle_X.setGeometry(QtCore.QRect(140, 20, 42, 22))
        self.Circle_X.setMaximum(65535)
        self.Circle_X.setObjectName(_fromUtf8("Circle_X"))
        self.Circle_Y = QtGui.QSpinBox(self.tab)
        self.Circle_Y.setGeometry(QtCore.QRect(220, 20, 42, 22))
        self.Circle_Y.setMaximum(65535)
        self.Circle_Y.setObjectName(_fromUtf8("Circle_Y"))
        self.Line_X1 = QtGui.QSpinBox(self.tab)
        self.Line_X1.setGeometry(QtCore.QRect(140, 80, 42, 22))
        self.Line_X1.setMaximum(65535)
        self.Line_X1.setObjectName(_fromUtf8("Line_X1"))
        self.Line_Y1 = QtGui.QSpinBox(self.tab)
        self.Line_Y1.setGeometry(QtCore.QRect(220, 80, 42, 22))
        self.Line_Y1.setMaximum(65535)
        self.Line_Y1.setObjectName(_fromUtf8("Line_Y1"))
        self.Circle_radius = QtGui.QSpinBox(self.tab)
        self.Circle_radius.setGeometry(QtCore.QRect(300, 20, 42, 22))
        self.Circle_radius.setMaximum(65535)
        self.Circle_radius.setObjectName(_fromUtf8("Circle_radius"))
        self.Position_X = QtGui.QSpinBox(self.tab)
        self.Position_X.setGeometry(QtCore.QRect(140, 140, 42, 22))
        self.Position_X.setMaximum(65535)
        self.Position_X.setObjectName(_fromUtf8("Position_X"))
        self.Position_Y = QtGui.QSpinBox(self.tab)
        self.Position_Y.setGeometry(QtCore.QRect(220, 140, 42, 22))
        self.Position_Y.setMaximum(65535)
        self.Position_Y.setObjectName(_fromUtf8("Position_Y"))
        self.Grap_pen_X = QtGui.QSpinBox(self.tab)
        self.Grap_pen_X.setGeometry(QtCore.QRect(140, 200, 42, 22))
        self.Grap_pen_X.setMaximum(65535)
        self.Grap_pen_X.setObjectName(_fromUtf8("Grap_pen_X"))
        self.Grap_pen_Y = QtGui.QSpinBox(self.tab)
        self.Grap_pen_Y.setGeometry(QtCore.QRect(220, 200, 42, 22))
        self.Grap_pen_Y.setMaximum(65535)
        self.Grap_pen_Y.setObjectName(_fromUtf8("Grap_pen_Y"))
        self.Get_position_display_X = QtGui.QLCDNumber(self.tab)
        self.Get_position_display_X.setGeometry(QtCore.QRect(140, 260, 91, 23))
        self.Get_position_display_X.setObjectName(_fromUtf8("Get_position_display_X"))
        self.Go_to_position_free = QtGui.QPushButton(self.tab)
        self.Go_to_position_free.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.Go_to_position_free.setObjectName(_fromUtf8("Go_to_position_free"))
        self.Grap_pen_free = QtGui.QPushButton(self.tab)
        self.Grap_pen_free.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.Grap_pen_free.setObjectName(_fromUtf8("Grap_pen_free"))
        self.Byte1 = QtGui.QSpinBox(self.tab)
        self.Byte1.setGeometry(QtCore.QRect(20, 400, 42, 22))
        self.Byte1.setMinimum(-1)
        self.Byte1.setMaximum(255)
        self.Byte1.setProperty("value", -1)
        self.Byte1.setObjectName(_fromUtf8("Byte1"))
        self.Byte2 = QtGui.QSpinBox(self.tab)
        self.Byte2.setGeometry(QtCore.QRect(70, 400, 42, 22))
        self.Byte2.setMinimum(-1)
        self.Byte2.setMaximum(255)
        self.Byte2.setSingleStep(1)
        self.Byte2.setProperty("value", -1)
        self.Byte2.setObjectName(_fromUtf8("Byte2"))
        self.Byte4 = QtGui.QSpinBox(self.tab)
        self.Byte4.setGeometry(QtCore.QRect(170, 400, 42, 22))
        self.Byte4.setMinimum(-1)
        self.Byte4.setMaximum(255)
        self.Byte4.setProperty("value", -1)
        self.Byte4.setObjectName(_fromUtf8("Byte4"))
        self.Byte3 = QtGui.QSpinBox(self.tab)
        self.Byte3.setGeometry(QtCore.QRect(120, 400, 42, 22))
        self.Byte3.setMinimum(-1)
        self.Byte3.setMaximum(255)
        self.Byte3.setProperty("value", -1)
        self.Byte3.setObjectName(_fromUtf8("Byte3"))
        self.Byte7 = QtGui.QSpinBox(self.tab)
        self.Byte7.setGeometry(QtCore.QRect(320, 400, 42, 22))
        self.Byte7.setMinimum(-1)
        self.Byte7.setMaximum(255)
        self.Byte7.setProperty("value", -1)
        self.Byte7.setObjectName(_fromUtf8("Byte7"))
        self.Byte8 = QtGui.QSpinBox(self.tab)
        self.Byte8.setGeometry(QtCore.QRect(370, 400, 42, 22))
        self.Byte8.setMinimum(-1)
        self.Byte8.setMaximum(255)
        self.Byte8.setProperty("value", -1)
        self.Byte8.setObjectName(_fromUtf8("Byte8"))
        self.Byte6 = QtGui.QSpinBox(self.tab)
        self.Byte6.setGeometry(QtCore.QRect(270, 400, 42, 22))
        self.Byte6.setMinimum(-1)
        self.Byte6.setMaximum(255)
        self.Byte6.setProperty("value", -1)
        self.Byte6.setObjectName(_fromUtf8("Byte6"))
        self.Byte5 = QtGui.QSpinBox(self.tab)
        self.Byte5.setGeometry(QtCore.QRect(220, 400, 42, 22))
        self.Byte5.setMinimum(-1)
        self.Byte5.setMaximum(255)
        self.Byte5.setProperty("value", -1)
        self.Byte5.setObjectName(_fromUtf8("Byte5"))
        self.Byte11 = QtGui.QSpinBox(self.tab)
        self.Byte11.setGeometry(QtCore.QRect(520, 400, 42, 22))
        self.Byte11.setMinimum(-1)
        self.Byte11.setMaximum(255)
        self.Byte11.setProperty("value", -1)
        self.Byte11.setObjectName(_fromUtf8("Byte11"))
        self.Byte12 = QtGui.QSpinBox(self.tab)
        self.Byte12.setGeometry(QtCore.QRect(570, 400, 42, 22))
        self.Byte12.setMinimum(-1)
        self.Byte12.setMaximum(255)
        self.Byte12.setProperty("value", -1)
        self.Byte12.setObjectName(_fromUtf8("Byte12"))
        self.Byte10 = QtGui.QSpinBox(self.tab)
        self.Byte10.setGeometry(QtCore.QRect(470, 400, 42, 22))
        self.Byte10.setMinimum(-1)
        self.Byte10.setMaximum(255)
        self.Byte10.setProperty("value", -1)
        self.Byte10.setObjectName(_fromUtf8("Byte10"))
        self.Byte9 = QtGui.QSpinBox(self.tab)
        self.Byte9.setGeometry(QtCore.QRect(420, 400, 42, 22))
        self.Byte9.setMinimum(-1)
        self.Byte9.setMaximum(255)
        self.Byte9.setProperty("value", -1)
        self.Byte9.setObjectName(_fromUtf8("Byte9"))
        self.Error_lebel = QtGui.QLabel(self.tab)
        self.Error_lebel.setGeometry(QtCore.QRect(500, 210, 191, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 130, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 85, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 26, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 147, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 130, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 85, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 26, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 147, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 130, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 85, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 26, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 20, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 40, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Error_lebel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Error_lebel.setFont(font)
        self.Error_lebel.setObjectName(_fromUtf8("Error_lebel"))
        self.Send_Package_button = QtGui.QPushButton(self.tab)
        self.Send_Package_button.setGeometry(QtCore.QRect(630, 400, 75, 23))
        self.Send_Package_button.setObjectName(_fromUtf8("Send_Package_button"))
        self.Error_message_lebel = QtGui.QLabel(self.tab)
        self.Error_message_lebel.setGeometry(QtCore.QRect(500, 300, 231, 31))
        self.Error_message_lebel.setObjectName(_fromUtf8("Error_message_lebel"))
        self.Serial_port_combo = QtGui.QComboBox(self.tab)
        self.Serial_port_combo.setGeometry(QtCore.QRect(520, 20, 131, 22))
        self.Serial_port_combo.setObjectName(_fromUtf8("Serial_port_combo"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(460, 20, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Connect_button = QtGui.QPushButton(self.tab)
        self.Connect_button.setGeometry(QtCore.QRect(670, 20, 75, 23))
        self.Connect_button.setObjectName(_fromUtf8("Connect_button"))
        self.Line_X2 = QtGui.QSpinBox(self.tab)
        self.Line_X2.setGeometry(QtCore.QRect(300, 80, 42, 22))
        self.Line_X2.setMaximum(65535)
        self.Line_X2.setObjectName(_fromUtf8("Line_X2"))
        self.Line_Y2 = QtGui.QSpinBox(self.tab)
        self.Line_Y2.setGeometry(QtCore.QRect(380, 80, 42, 22))
        self.Line_Y2.setMaximum(65535)
        self.Line_Y2.setObjectName(_fromUtf8("Line_Y2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(150, 50, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(310, 50, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(150, 110, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(230, 110, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(310, 110, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(390, 110, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(150, 170, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(230, 170, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(230, 230, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(150, 230, 46, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.Get_position_display_Y = QtGui.QLCDNumber(self.tab)
        self.Get_position_display_Y.setGeometry(QtCore.QRect(250, 260, 91, 23))
        self.Get_position_display_Y.setObjectName(_fromUtf8("Get_position_display_Y"))
        self.Get_position_display_SW = QtGui.QLCDNumber(self.tab)
        self.Get_position_display_SW.setGeometry(QtCore.QRect(360, 260, 64, 23))
        self.Get_position_display_SW.setObjectName(_fromUtf8("Get_position_display_SW"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Circle_button.setText(_translate("MainWindow", "Circle >>", None))
        self.Line_button.setText(_translate("MainWindow", "Line >>", None))
        self.Go_to_position_button.setText(_translate("MainWindow", "Go to >>", None))
        self.Grap_pen_button.setText(_translate("MainWindow", "Grap pen >>", None))
        self.Get_position_button.setText(_translate("MainWindow", "Get Pos >>", None))
        self.Reset_button.setText(_translate("MainWindow", "Reset >>", None))
        self.Go_to_position_free.setText(_translate("MainWindow", "Free Move", None))
        self.Grap_pen_free.setText(_translate("MainWindow", "Free Move", None))
        self.Error_lebel.setText(_translate("MainWindow", "No error", None))
        self.Send_Package_button.setText(_translate("MainWindow", "send>>", None))
        self.Error_message_lebel.setText(_translate("MainWindow", "No error message", None))
        self.label_3.setText(_translate("MainWindow", "Serial port", None))
        self.Connect_button.setText(_translate("MainWindow", "Connect", None))
        self.label.setText(_translate("MainWindow", "x", None))
        self.label_2.setText(_translate("MainWindow", "y", None))
        self.label_4.setText(_translate("MainWindow", "radius", None))
        self.label_5.setText(_translate("MainWindow", "x1", None))
        self.label_6.setText(_translate("MainWindow", "y1", None))
        self.label_7.setText(_translate("MainWindow", "x2", None))
        self.label_8.setText(_translate("MainWindow", "y2", None))
        self.label_9.setText(_translate("MainWindow", "x", None))
        self.label_10.setText(_translate("MainWindow", "y", None))
        self.label_11.setText(_translate("MainWindow", "y", None))
        self.label_12.setText(_translate("MainWindow", "x", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

