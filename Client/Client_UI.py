# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2021ChatLayoutDecember.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(746, 561)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SlidingMenu = QtWidgets.QFrame(self.centralwidget)
        self.SlidingMenu.setEnabled(True)
        self.SlidingMenu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SlidingMenu.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"border:None")
        self.SlidingMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SlidingMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SlidingMenu.setObjectName("SlidingMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SlidingMenu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_layout_side = QtWidgets.QGridLayout()
        self.Button_layout_side.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Button_layout_side.setContentsMargins(-1, 0, 0, 0)
        self.Button_layout_side.setHorizontalSpacing(6)
        self.Button_layout_side.setVerticalSpacing(120)
        self.Button_layout_side.setObjectName("Button_layout_side")
        self.Settings_button = QtWidgets.QPushButton(self.SlidingMenu)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Settings_button.setFont(font)
        self.Settings_button.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"padding-left:72px;\n"
"height:50px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:5px;\n"
"    background-color: rgb(38, 38, 38);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/setting-icon-png-18.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_button.setIcon(icon)
        self.Settings_button.setIconSize(QtCore.QSize(32, 32))
        self.Settings_button.setFlat(True)
        self.Settings_button.setObjectName("Settings_button")
        self.Button_layout_side.addWidget(self.Settings_button, 4, 0, 1, 1)
        self.Hamburger = QtWidgets.QPushButton(self.SlidingMenu)
        self.Hamburger.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(38, 38, 38);\n"
"}")
        self.Hamburger.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/white-menu-icon-12.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Hamburger.setIcon(icon1)
        self.Hamburger.setIconSize(QtCore.QSize(64, 64))
        self.Hamburger.setObjectName("Hamburger")
        self.Button_layout_side.addWidget(self.Hamburger, 0, 0, 1, 1)
        self.UserLayout = QtWidgets.QVBoxLayout()
        self.UserLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.UserLayout.setContentsMargins(50, 0, 0, 0)
        self.UserLayout.setSpacing(13)
        self.UserLayout.setObjectName("UserLayout")
        self.UserIcon = QtWidgets.QLabel(self.SlidingMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserIcon.sizePolicy().hasHeightForWidth())
        self.UserIcon.setSizePolicy(sizePolicy)
        self.UserIcon.setMaximumSize(QtCore.QSize(120, 120))
        self.UserIcon.setStyleSheet("")
        self.UserIcon.setLineWidth(0)
        self.UserIcon.setText("")
        self.UserIcon.setPixmap(QtGui.QPixmap(":/Icons/824-8246267_time-left-user-icon-round-png.png"))
        self.UserIcon.setScaledContents(True)
        self.UserIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.UserIcon.setWordWrap(False)
        self.UserIcon.setIndent(0)
        self.UserIcon.setObjectName("UserIcon")
        self.UserLayout.addWidget(self.UserIcon)
        self.UserNickname = QtWidgets.QLabel(self.SlidingMenu)
        self.UserNickname.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(85)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserNickname.sizePolicy().hasHeightForWidth())
        self.UserNickname.setSizePolicy(sizePolicy)
        self.UserNickname.setMinimumSize(QtCore.QSize(0, 0))
        self.UserNickname.setMaximumSize(QtCore.QSize(200, 20))
        self.UserNickname.setBaseSize(QtCore.QSize(0, 4))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.UserNickname.setFont(font)
        self.UserNickname.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.UserNickname.setLineWidth(1)
        self.UserNickname.setScaledContents(True)
        self.UserNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.UserNickname.setWordWrap(False)
        self.UserNickname.setIndent(0)
        self.UserNickname.setObjectName("UserNickname")
        self.UserLayout.addWidget(self.UserNickname)
        self.Button_layout_side.addLayout(self.UserLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.Button_layout_side)
        self.horizontalLayout.addWidget(self.SlidingMenu)
        self.MainChat = QtWidgets.QWidget(self.centralwidget)
        self.MainChat.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"background-color: rgb(35, 35, 35);")
        self.MainChat.setObjectName("MainChat")
        self.gridLayout = QtWidgets.QGridLayout(self.MainChat)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.MainChat)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(102, 102, 102);\n"
"color: white;\n"
"border-radius:20px;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.Send_Button = QtWidgets.QPushButton(self.MainChat)
        self.Send_Button.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Send_Button.setFont(font)
        self.Send_Button.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"   border:none;\n"
"background-color: None;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:25px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 164, 141, 135), stop:0.732955 rgba(128, 194, 194, 203));\n"
"\n"
"}")
        self.Send_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/content+send+icon-1320087227200139227.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Send_Button.setIcon(icon2)
        self.Send_Button.setIconSize(QtCore.QSize(50, 50))
        self.Send_Button.setDefault(False)
        self.Send_Button.setFlat(False)
        self.Send_Button.setObjectName("Send_Button")
        self.gridLayout.addWidget(self.Send_Button, 1, 1, 1, 1)
        self.messagesView = QtWidgets.QListView(self.MainChat)
        self.messagesView.setStyleSheet("border:none;")
        self.messagesView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messagesView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messagesView.setResizeMode(QtWidgets.QListView.Adjust)
        self.messagesView.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.messagesView.setObjectName("messagesView")
        self.gridLayout.addWidget(self.messagesView, 0, 0, 1, 2)
        self.horizontalLayout.addWidget(self.MainChat)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Settings_button.setText(_translate("MainWindow", "Settings"))
        self.UserNickname.setText(_translate("MainWindow", "UserName"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:20px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import Icons_Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
