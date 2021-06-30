import socket
import sys
import threading

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView

from Client.Bubble.LabelBubble import MessageDelegate, MessageModel, USER_ME, USER_THEM
from Client.Username.Choose_Draggable import Draggable
from Client_UI import Ui_MainWindow

import Icons_Resource_rc

HOST = '127.0.0.1'
PORT = 9090


class ClientCode(Ui_MainWindow, QMainWindow):
    def __init__(self, host, port):
        super(ClientCode, self).__init__()
        self.setupUi(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        # Accept Username here
        self.windowAvailable = None
        self.getUsername()
        # Set threading here
        self.gui_done = True
        self.running = True
        self.uiFunctions()
        self.threading()
        self.bubbleChat()

    def threading(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def uiFunctions(self):
        self.Hamburger.clicked.connect(self.slide_left_menu)
        self.Send_Button.clicked.connect(self.write)
        # Add a timer to keep refreshing the qlistview
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.model.layoutChanged.emit())
        self.timer.start(0)

    def getUsername(self):
        if self.windowAvailable is None:
            self.windowAvailable = Draggable()
        if self.windowAvailable.exec_():
            self.nickname = self.windowAvailable.lineEdit.text()
            self.UserNickname.setText(self.nickname)
        self.windowAvailable = None

    def write(self):
        '''This function gets the message and sends it to the server which broadcasts it'''
        message = f"{self.nickname}:{self.textEdit.toPlainText()}\n"
        self.sock.send(message.encode('UTF-8'))
        # Check if username is in message by splitting up
        if self.nickname == message.split(':')[0]:
            self.model.add_message(USER_ME, message)
        self.textEdit.clear()

    def receive(self):
        """While client is running decode every message from the server and insert it as plain text
        Close connection if there is a disconnect or error"""
        while self.running:
            try:
                message = self.sock.recv(1024).decode('UTF-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('UTF-8'))
                else:
                    if self.gui_done:
                        self.textBrowser.insertPlainText(message + "\n")
                        if self.nickname != message.split(':')[0]:
                            self.model.add_message(USER_THEM, message)
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break

    def closeEvent(self, event):
        """Close Sock and Exit application"""
        self.running = False
        self.sock.close()
        QMainWindow.closeEvent(self, event)
        exit(0)

    def slide_left_menu(self):
        """Function To create Sliding Left Menu With QFrame"""
        width = self.SlidingMenu.width()
        if width == 50:
            newwidth = 180
            if ' ' in self.UserNickname.text():
                self.UserNickname.setFixedWidth(110)
                self.UserNickname.setContentsMargins(0, 0, 30, 0)
                self.UserNickname.setWordWrap(True)
                self.UserNickname.setAlignment(Qt.AlignHCenter)
            else:
                self.UserNickname.setFixedWidth(150)
                self.UserNickname.setContentsMargins(23, 0, 0, 0)
                self.UserNickname.setAlignment(Qt.AlignJustify)

        else:
            newwidth = 50

        # Animate the transition
        self.animation = QPropertyAnimation(self.SlidingMenu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    ## ---------BUBBLE STUFF--------------
    def bubbleChat(self):
        self.textBrowser.setDisabled(True)
        # Start listview here
        self.messagesView = QListView(self.MainChat)
        self.messagesView.setResizeMode(QListView.Adjust)
        # Use our delegate to draw items in this view.
        self.messagesView.setItemDelegate(MessageDelegate())
        self.model = MessageModel()
        self.messagesView.setModel(self.model)
        # Add layout to grid here Done
        self.gridLayout.addWidget(self.messagesView, 0, 0, 1, 2)

    def resizeEvent(self, e):
        self.model.layoutChanged.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientCode = ClientCode(HOST, PORT)
    clientCode.show()
    sys.exit(app.exec_())
