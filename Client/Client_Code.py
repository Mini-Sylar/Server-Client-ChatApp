import socket
import threading

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
import Icons_Resource_rc
from Client_UI import Ui_MainWindow
from Choose_Draggable import Draggable

HOST = '127.0.0.1'
PORT = 9090

class Client_Code(Ui_MainWindow, QMainWindow):
    def __init__(self,host,port):
        super(Client_Code, self).__init__()
        self.setupUi(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        # Accept Username here
        self.windowAvailable = None
        self.getUsername()
        #Set threading here
        self.gui_done = True
        self.running = True
        self.uiFunctions()
        self.threading()


    def threading(self):
        # gui_thread = threading.Thread(target=self.setupUi(self))
        receive_thread = threading.Thread(target=self.receive)
        # gui_thread.start()
        receive_thread.start()

    def uiFunctions(self):
        self.Hamburger.clicked.connect(self.slide_left_menu)
        self.Send_Button.clicked.connect(self.write)


    def getUsername(self):
        if self.windowAvailable is None:
            self.windowAvailable = Draggable()
        if self.windowAvailable.exec_():
            self.nickname=self.windowAvailable.lineEdit.text()
            self.UserNickname.setText(self.nickname)
        self.windowAvailable = None


    def write(self):
        '''This function gets the message and sends it to the server which broadcasts it'''
        message = f"{self.nickname}:{self.textEdit.toPlainText()}\n"
        self.sock.send(message.encode('UTF-8'))
        self.textEdit.clear()

    def receive(self):
        '''While client is running decode every message from the server and insert it as plain text
        Close connection if there is a disconnect or error
        '''
        while self.running:
            try:
                message = self.sock.recv(1024).decode('UTF-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('UTF-8'))
                else:
                    if self.gui_done:
                        self.textBrowser.insertPlainText(message + "\n")
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break

    def closeEvent(self, event):
        '''Close Sock and Exit application'''
        self.running = False
        self.sock.close()
        QMainWindow.closeEvent(self, event)
        exit(0)

    def slide_left_menu(self):
            '''Function To create Sliding Left Menu With QFrame'''
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
                    self.UserNickname.setContentsMargins(0, 0, 0, 0)
                    self.UserNickname.setAlignment(Qt.AlignAbsolute)

            else:
                newwidth = 50

            # Animate the transiton
            self.animation = QPropertyAnimation(self.SlidingMenu, b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newwidth)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    clientCode = Client_Code(HOST,PORT)
    clientCode.show()
    sys.exit(app.exec_())
