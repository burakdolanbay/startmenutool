# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledv2.ui'
#
# Created: Sat Apr  9 00:09:36 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
import getpass

from PyQt4.QtCore import Qt, pyqtSlot, SIGNAL, SLOT, QRect
from PyQt4.QtGui import QMenu, QTableWidget
from orca.scripts import apps

import pencere
import sqlite3 as db

import pencereVson
from pencere import Ui_Dialog

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


class Ui_kilit_btn(object):
    ###########################




    #############################


    def firefox(self):
        os.system("firefox")
        quit()

    # kapatma...
    def kapatma(self):
        os.system("shutdown -h now")
        quit()

    # reset

    def resetle(self):
         os.system(" shutdown -r now")
         quit()

    def kilit(self):
        os.system("gnome-session-quit")
        quit()

    def libreoffice(self):
        os.system("libreoffice")
        quit()

    # Donatılar
    def hesapMakinesi(self):
        os.system("gnome-calculator")
        quit()

    # oyunlar
    def mayin(self):
        os.system("gnome-mines")
        quit()

    def pisti(self):
        os.system("gnome-mahjongg")
        quit()

    def sudoku(self):
        os.system("gnome-sudoku")
        quit()

        # ubuntuYazılımMerkezi

    def software(self):
        os.system("software-center")
        quit()

    def yardımMerkezi(self):
        os.system("gnome-help")
        quit()

        # terminal

    def terminal(self):
        os.system("gnome-terminal")
        quit()
        # terminal

    def calar(self):
        os.system("rhythmbox")
        quit()

        # DENETİM MASASI AÇMA

    def aygit(self):
        os.system("gnome-disks")
        quit()

    def ayarlar(self):
        os.system("unity-control-center")
        quit()

        # Bilgisayar

    def disk_ac(self):
        os.system("nautilus /")
        quit()

        # arama

    def arama(self):
        os.system("gnome-search-tool")
        quit()

    # text
    def text(self):
        os.system("gedit")
        quit()

        # Videolar

    def video_ac(self):
        os.system("nautilus /home/" + getpass.getuser() + "/Videolar")
        quit()

        # Muzik

    def muzik_ac(self):
        os.system("nautilus /home/" + getpass.getuser() + "/Müzik")
        quit()

    def Clicked(self, item):
        konum = self.vb.konumCek(item.text())
        os.system(konum)
        quit()


        # Resimler

    def resim_ac(self):
        os.system("nautilus /home/" + getpass.getuser() + "/Resimler")
        quit()

        # Belge

    def belge_ac(self):
        os.system("nautilus /home/" + getpass.getuser() + "/Belgeler")
        quit()

    def setupUi(self, kilit_btn):
        self.bilgi = getpass.getuser()
        kilit_btn.setObjectName(_fromUtf8("kilit_btn"))
        kilit_btn.resize(473, 658)
        kilit_btn.move(0, 400)
        kilit_btn.setAutoFillBackground(False)
        kilit_btn.setWindowIcon(QtGui.QIcon('windowsicon.png'))

        kilit_btn.setStyleSheet(_fromUtf8("background-color: rgba(0, 128, 255,70%);"))
        kilit_btn.setWindowFlags(kilit_btn.windowFlags() | QtCore.Qt.FramelessWindowHint)
        kilit_btn.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtGui.QWidget(kilit_btn)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(280, 590, 171, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(_fromUtf8("background-color: none"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.kapat_btn = QtGui.QCommandLinkButton(self.frame_2)
        self.kapat_btn.setGeometry(QtCore.QRect(80, 10, 71, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kapat_btn.sizePolicy().hasHeightForWidth())
        self.kapat_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kapat_btn.setFont(font)
        self.kapat_btn.setStyleSheet(_fromUtf8("image: url(\"/home/reo-ubuntu/Masasüstü/power.png\");\n"
                                               "subcontrol-origin: padding;\n"
                                               "    subcontrol-position: bottom right; background-color:none;"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("power.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kapat_btn.setIcon(icon)
        self.kapat_btn.setObjectName(_fromUtf8("kapat_btn"))

        self.restart_btn = QtGui.QCommandLinkButton(self.frame_2)
        self.restart_btn.setGeometry(QtCore.QRect(0, 10, 81, 41))
        self.restart_btn.setStyleSheet(_fromUtf8("background-color: none"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.restart_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("reboot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restart_btn.setIcon(icon1)
        self.restart_btn.setObjectName(_fromUtf8("restart_btn"))
        self.powers = QtGui.QCommandLinkButton(self.frame_2)
        self.powers.setGeometry(QtCore.QRect(150, 10, 185, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.powers.setFont(font)
        self.powers.setText(_fromUtf8(""))
        self.powers.setObjectName(_fromUtf8("powers"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 350, 260, 250))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))

        self.verticalLayoutWidget_2.setStyleSheet(_fromUtf8("background-color: rgba(0, 100, 255,30%);"))

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        #####


        self.toolBox = QtGui.QToolBox(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(_fromUtf8("    color:rgb(255, 255, 255)"))

        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 239, 179))
        self.toolBoxPage1.setObjectName(_fromUtf8("toolBoxPage1"))
        self.sudoku_btn = QtGui.QCommandLinkButton(self.toolBoxPage1)
        self.sudoku_btn.setGeometry(QtCore.QRect(0, 0, 231, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sudoku_btn.sizePolicy().hasHeightForWidth())
        self.sudoku_btn.setSizePolicy(sizePolicy)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("sudoku.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sudoku_btn.setIcon(icon8)
        self.sudoku_btn.setObjectName(_fromUtf8("sudoku_btn"))
        self.mayin_btn = QtGui.QCommandLinkButton(self.toolBoxPage1)
        self.mayin_btn.setGeometry(QtCore.QRect(0, 40, 231, 41))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("mayin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mayin_btn.setIcon(icon9)
        self.mayin_btn.setObjectName(_fromUtf8("mayin_btn"))
        self.mah_btn = QtGui.QCommandLinkButton(self.toolBoxPage1)
        self.mah_btn.setGeometry(QtCore.QRect(0, 80, 231, 41))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("pist.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mah_btn.setIcon(icon10)
        self.mah_btn.setObjectName(_fromUtf8("mah_btn"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("game.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.toolBoxPage1, icon11, _fromUtf8(""))
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 239, 179))
        self.toolBoxPage2.setObjectName(_fromUtf8("toolBoxPage2"))
        self.toolBox.addItem(self.toolBoxPage2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.toolBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 0, 16, 641))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line.setStyleSheet(_fromUtf8("background-color:none"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 10, 201, 581))
        self.verticalLayoutWidget.setStyleSheet(_fromUtf8("background-color:none"))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(128, 128))
        self.label.setMaximumSize(QtCore.QSize(128, 128))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("OS_Ubuntu.png")))

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.users_btn = QtGui.QLabel(self.verticalLayoutWidget)
        self.users_btn.setStyleSheet(_fromUtf8("text-align:center;"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.users_btn.setFont(font)
        self.users_btn.setObjectName(_fromUtf8("users_btn"))
        self.verticalLayout.addWidget(self.users_btn)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.belgeler_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.belgeler_btn.sizePolicy().hasHeightForWidth())
        self.belgeler_btn.setSizePolicy(sizePolicy)
        self.belgeler_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.belgeler_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.belgeler_btn.setSizeIncrement(QtCore.QSize(0, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.belgeler_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.belgeler_btn.setFont(font)
        self.belgeler_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.belgeler_btn.setAutoFillBackground(False)
        self.belgeler_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                                  "color:rgb(255, 255, 255);\n"
                                                  "text-align:left;\n"
                                                  "border:0px;\n"

                                                  "background-color: none;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover\n"
                                                  "{\n"
                                                  "    color:rgb(255, 255, 255);\n"
                                                  "    background-color:rgb(218, 218, 218);\n"
                                                  "\n"
                                                  "\n"
                                                  "}"))
        self.belgeler_btn.setIconSize(QtCore.QSize(0, 0))
        self.belgeler_btn.setObjectName(_fromUtf8("belgeler_btn"))
        self.verticalLayout.addWidget(self.belgeler_btn)
        self.resim_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resim_btn.sizePolicy().hasHeightForWidth())
        self.resim_btn.setSizePolicy(sizePolicy)
        self.resim_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.resim_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resim_btn.setFont(font)
        self.resim_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                               "color:rgb(255, 255, 255);\n"
                                               "text-align:left;\n"
                                               "border:0px;\n"
                                               "background-color: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    color:rgb(255, 255, 255);\n"
                                               "    background-color:rgb(218, 218, 218);\n"
                                               "\n"
                                               "\n"
                                               "}"))
        self.resim_btn.setAutoDefault(False)
        self.resim_btn.setDefault(False)
        self.resim_btn.setFlat(False)
        self.resim_btn.setObjectName(_fromUtf8("resim_btn"))
        self.verticalLayout.addWidget(self.resim_btn)
        self.muzik_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.muzik_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muzik_btn.setFont(font)
        self.muzik_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                               "color:rgb(255, 255, 255);\n"
                                               "text-align:left;\n"
                                               "border:0px;\n"
                                               "background-color: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    color:rgb(255, 255, 255);\n"
                                               "    background-color:rgb(218, 218, 218);\n"
                                               "\n"
                                               "\n"
                                               "}"))
        self.muzik_btn.setObjectName(_fromUtf8("muzik_btn"))
        self.verticalLayout.addWidget(self.muzik_btn)
        self.video_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.video_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.video_btn.setFont(font)
        self.video_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                               "color:rgb(255, 255, 255);\n"
                                               "text-align:left;\n"
                                               "border:0px;\n"
                                               "background-color: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    color:rgb(255, 255, 255);\n"
                                               "    background-color:rgb(218, 218, 218);\n"
                                               "\n"
                                               "\n"
                                               "}"))
        self.video_btn.setObjectName(_fromUtf8("video_btn"))
        self.verticalLayout.addWidget(self.video_btn)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.pc_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pc_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pc_btn.setFont(font)
        self.pc_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                            "color:rgb(255, 255, 255);\n"
                                            "text-align:left;\n"
                                            "border:0px;\n"
                                            "background-color: none;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    color:rgb(255, 255, 255);\n"
                                            "    background-color:rgb(218, 218, 218);\n"
                                            "\n"
                                            "\n"
                                            "}"))
        self.pc_btn.setObjectName(_fromUtf8("pc_btn"))
        self.verticalLayout.addWidget(self.pc_btn)
        self.denetim_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.denetim_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.denetim_btn.setFont(font)
        self.denetim_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                                 "color:rgb(255, 255, 255);\n"
                                                 "text-align:left;\n"
                                                 "border:0px;\n"
                                                 "background-color: none;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover\n"
                                                 "{\n"
                                                 "    color:rgb(255, 255, 255);\n"
                                                 "    background-color:rgb(218, 218, 218);\n"
                                                 "\n"
                                                 "\n"
                                                 "}"))
        self.denetim_btn.setObjectName(_fromUtf8("denetim_btn"))
        self.verticalLayout.addWidget(self.denetim_btn)
        self.aygit_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.aygit_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.aygit_btn.setFont(font)
        self.aygit_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                               "color:rgb(255, 255, 255);\n"
                                               "text-align:left;\n"
                                               "border:0px;\n"
                                               "background-color: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    color:rgb(255, 255, 255);\n"
                                               "    background-color:rgb(218, 218, 218);\n"
                                               "\n"
                                               "\n"
                                               "}"))
        self.aygit_btn.setObjectName(_fromUtf8("aygit_btn"))
        self.verticalLayout.addWidget(self.aygit_btn)
        self.terminal_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal_btn.sizePolicy().hasHeightForWidth())
        self.terminal_btn.setSizePolicy(sizePolicy)
        self.terminal_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.terminal_btn.setFont(font)
        self.terminal_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                                  "color:rgb(255, 255, 255);\n"
                                                  "text-align:left;\n"
                                                  "border:0px;\n"
                                                  "background-color: none;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover\n"
                                                  "{\n"
                                                  "    color:rgb(255, 255, 255);\n"
                                                  "    background-color:rgb(218, 218, 218);\n"
                                                  "\n"
                                                  "\n"
                                                  "}"))

        self.terminal_btn.setObjectName(_fromUtf8("terminal_btn"))
        self.verticalLayout.addWidget(self.terminal_btn)
        self.yardim_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yardim_btn.sizePolicy().hasHeightForWidth())
        self.yardim_btn.setSizePolicy(sizePolicy)
        self.yardim_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.yardim_btn.setFont(font)
        self.yardim_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
                                                "color:rgb(255, 255, 255);\n"
                                                "text-align:left;\n"
                                                "border:0px;\n"
                                                "background-color: none;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover\n"
                                                "{\n"
                                                "    color:rgb(255, 255, 255);\n"
                                                "    background-color:rgb(218, 218, 218);\n"
                                                "\n"
                                                "\n"
                                                "}"))
        self.yardim_btn.setObjectName(_fromUtf8("yardim_btn"))
        self.verticalLayout.addWidget(self.yardim_btn)
        self.arama_btn = QtGui.QCommandLinkButton(self.centralwidget)
        self.arama_btn.setGeometry(QtCore.QRect(210, 590, 40, 36))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arama_btn.sizePolicy().hasHeightForWidth())
        self.arama_btn.setSizePolicy(sizePolicy)
        self.arama_btn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.arama_btn.setFont(font)
        self.arama_btn.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arama_btn.setIcon(icon12)
        self.arama_btn.setObjectName(_fromUtf8("arama_btn"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 590, 200, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 0, 248, 341))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.setStyleSheet("""
                               QListWidget {
                                    show-decoration-selected: 1; /* make the selection span the entire width of the view */
                                    background-color: rgba(0, 100, 255,50%);
                                    border:0px;
                                    color:white;
                                    margin-top:10px;

                                    font-size:15px;
                                    font-weight: bold;


                                }
                                QListWidget::item {
                                    padding:5px;
                                }
                                QListView::item:alternate {

                                    background: #EEEEEE;

                                }

                                QListWidget::item:selected {
                                    border: 0px solid none;
                                }



                                QListWidget::item:hover {

                                    background-color:rgb(218, 218, 218);
                                }
                                """
                                      )
        kilit_btn.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(kilit_btn)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 473, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        kilit_btn.setMenuBar(self.menuBar)

        self.vb = Ui_Dialog()
        self.nesneler = self.vb.listele()
        for i in self.nesneler:
            nesne = QtGui.QListWidgetItem(i[2]);
            nesne.setIcon(QtGui.QIcon(r"" + i[1]));
            self.listWidget.addItem(nesne)

        self.listWidget.itemClicked.connect(self.Clicked)
        self.retranslateUi(kilit_btn)

        QtCore.QObject.connect(self.kapat_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.kapatma)
        QtCore.QObject.connect(self.restart_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.resetle)
        QtCore.QObject.connect(self.powers, QtCore.SIGNAL(_fromUtf8("clicked()")), self.kilit)
        QtCore.QObject.connect(self.arama_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.arama)
        QtCore.QObject.connect(self.aygit_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.aygit)
        QtCore.QObject.connect(self.belgeler_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.belge_ac)
        QtCore.QObject.connect(self.denetim_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ayarlar)

        QtCore.QObject.connect(self.video_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.video_ac)
        QtCore.QObject.connect(self.resim_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.resim_ac)
        QtCore.QObject.connect(self.terminal_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.terminal)
        QtCore.QObject.connect(self.yardim_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.yardımMerkezi)

        QtCore.QObject.connect(self.sudoku_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sudoku)
        QtCore.QObject.connect(self.mayin_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mayin)

        QtCore.QObject.connect(self.muzik_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.muzik_ac)
        QtCore.QObject.connect(self.pc_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.disk_ac)

        QtCore.QMetaObject.connectSlotsByName(kilit_btn)

    def retranslateUi(self, kilit_btn):
        kilit_btn.setWindowTitle(_translate("kilit_btn", "Başlat Menüsü", None))
        self.frame_2.setStyleSheet(_translate("kilit_btn", "    border-style: outset;\n"
                                                           "    text-align:left;\n"

                                                           "    background-color:none\n"

                                                           "", None))
        self.kapat_btn.setText(_translate("kilit_btn", "Kapat", None))

        self.restart_btn.setText(_translate("kilit_btn", "Restart", None))

        self.sudoku_btn.setText(_translate("kilit_btn", "Sudoku", None))
        self.mayin_btn.setText(_translate("kilit_btn", "Mayın", None))
        self.mah_btn.setText(_translate("kilit_btn", "Mahjongg", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("kilit_btn", "Oyunlar", None))
        self.users_btn.setText(_translate("kilit_btn", self.bilgi, None))
        self.belgeler_btn.setToolTip(
            _translate("kilit_btn", "<html><head/><body><p align=\"center\">Belgeler klasörü</p></body></html>", None))
        self.belgeler_btn.setText(_translate("kilit_btn", "Belgeler", None))
        self.resim_btn.setWhatsThis(
            _translate("kilit_btn", "<html><head/><body><p>Resimleriniz,Albümleriniz..</p></body></html>", None))
        self.resim_btn.setText(_translate("kilit_btn", "Resimler", None))
        self.muzik_btn.setWhatsThis(_translate("kilit_btn",
                                               "<html><head/><body><p>Müzik arşiviniz</p><p align=\"center\"><br/></p></body></html>",
                                               None))
        self.muzik_btn.setText(_translate("kilit_btn", "Müzik", None))
        self.video_btn.setWhatsThis(
            _translate("kilit_btn", "<html><head/><body><p>Video arşiviniz</p></body></html>", None))
        self.video_btn.setText(_translate("kilit_btn", "Videolar", None))
        self.pc_btn.setWhatsThis(
            _translate("kilit_btn", "<html><head/><body><p>Bilgisayar Bölümünüz</p></body></html>", None))
        self.pc_btn.setText(_translate("kilit_btn", "Bilgisayarım", None))
        self.denetim_btn.setText(_translate("kilit_btn", "Denetim Masası", None))
        self.aygit_btn.setText(_translate("kilit_btn", "Aygıtlar ve Yazıcılar", None))
        self.terminal_btn.setText(_translate("kilit_btn", "Terminal", None))
        self.yardim_btn.setText(_translate("kilit_btn", "Yardım ve Destek", None))
        self.textEdit.setHtml(_translate("kilit_btn",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Programları ve Dosyaları ara</span></p></body></html>",
                                         None))


####





####################veriTabani




#####

class myMainWindow(QtGui.QMainWindow):
    @pyqtSlot(QtCore.QPoint)
    def contextMenuRequested(self, point):
        menu = QtGui.QMenu()

        action1 = menu.addAction("Program Kısayol Düzenleme")
        # action2 = menu.addAction("Çıkar")


        self.connect(action1, SIGNAL("triggered()"),
                     self, SLOT("ekle()"))
        self.connect(action1, SIGNAL("triggered()"), self, SLOT("sil()"))
        menu.exec_(self.mapToGlobal(point))

    @pyqtSlot()
    def ekle(self):
        self.ui = Ui_Dialog()
        self.MainWindow = QtGui.QMainWindow()
        self.ui.setupUi(self.MainWindow)

        self.MainWindow.show()

    @pyqtSlot()
    def sil(self):
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    kilit_btn = myMainWindow()
    menu = QtGui.QMenu()
    kilit_btn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu);
    kilit_btn.connect(kilit_btn, SIGNAL("customContextMenuRequested(QPoint)"), kilit_btn,
                      SLOT("contextMenuRequested(QPoint)"))
    ui = Ui_kilit_btn()
    ui.setupUi(kilit_btn)
    kilit_btn.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
