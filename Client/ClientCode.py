import socket
import sys
import threading
import select
import errno

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, QTimer
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog

from Client.Bubble.LabelBubble import MessageDelegate, MessageModel, USER_ME, USER_THEM, USER_ADMIN
from Client.Username.Choose_Draggable import Draggable
from Client.Client_UI import Ui_MainWindow

import random
from time import time
import uuid

import ast

HOST = '127.0.0.1'
PORT = 1234
# Server Messages
s_messages = ('connected to the server!', 'Disconnected from the server!')
HEADER_LENGTH = 8192


# ============ Helpers ==============
# Random Color Generator
def rand_color(def_color='#a5d6a7'):
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r()) if r else def_color


# Find Character at a given position
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + 1)
        n -= 1
    return start


# Client List
clientColor = dict()
clientUser = list()
clientList = list()
fragments = list()


class ClientCode(Ui_MainWindow, QMainWindow):
    def __init__(self, host, port):
        super(ClientCode, self).__init__()
        self.setupUi(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.setblocking(True)
        # Accept Username here
        self.windowAvailable = None
        self.getUsername()
        # Set threading here
        self.gui_done = True
        self.running = True
        self.create_emojis()
        # self.myPixmap = QPixmap(600, 600)
        self.uiFunctions()
        self.threading()
        self.bubbleChat()
        # unique Identifier
        self.uuid = uuid.uuid4().hex

    def threading(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def create_emojis(self):
        buttons = {}
        for i in range(58):  # controls rows
            for j in range(6):  # controls columns
                # keep a reference to the buttons
                buttons[(i, j)] = QPushButton(self.Emo_Smiles)
                buttons[(i, j)].setObjectName(f'emoji_{j}_smiles')
                buttons[(i, j)].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                buttons[(i, j)].setFlat(True)
                # add to the layout
                self.gridLayout_2.addWidget(buttons[(i, j)], i, j)
        # Display Emojis
        icons = []
        curr_moji_length = len(self.Emo_Smiles.children()[1:]) + 1
        for items in range(0, curr_moji_length):
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/EmojisOpened/emoji_{items}.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            icons.append(icon)
        for index, item in enumerate(self.Emo_Smiles.children()[1:]):
            item.setIcon(icons[index])
            item.setIconSize(QtCore.QSize(32, 32))

    def uiFunctions(self):
        self.Hamburger.clicked.connect(self.slide_left_menu)
        self.Send_Button.clicked.connect(self.write)
        self.emojiButton.clicked.connect(self.emoji_pane)
        self.attachButton.clicked.connect(self.openfile)
        # Emojis
        # Get emojis from text file
        emojis = []
        textArea = self.textEdit.document()
        # cursor = QTextCursor(textArea)
        with open('EmojiList.txt', 'r', encoding="utf8") as file:
            emojis = file.read().splitlines()
        for index, item in enumerate(self.Emo_Smiles.children()[1:]):
            # Add option to insert html image instead of plain text after inserting images in qlistview
            item.clicked.connect(lambda checked, text=index: self.textEdit.insertPlainText(emojis[text]))
            # item.clicked.connect(lambda checked, text=index: cursor.insertImage(f":/EmojisOpened/emoji_{text}.png"))

        # Add a timer to keep refreshing the Qlistview
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.model.layoutChanged.emit())
        self.timer.start(150)

    def getUsername(self):
        if self.windowAvailable is None:
            self.windowAvailable = Draggable()
        if self.windowAvailable.exec_():
            self.username = self.windowAvailable.lineEdit.text().encode('utf-8')
            self.username_header = f'{len(self.username):<{HEADER_LENGTH}}'.encode('utf-8')
            self.sock.send(self.username_header + self.username)
            self.UserNickname.setText(self.username.decode('utf-8'))
        self.windowAvailable = None

    def openfile(self, open_file=None):
        if not open_file:
            open_file = QFileDialog.getOpenFileName(None, 'Open File:', '', 'Images (*.png *.bmp *.jpg)')
        if open_file[0]:
            with open(open_file[0], 'rb') as file:
                openFile_ok = file.read()
                image = QImage()
                image.loadFromData(openFile_ok)
                tobesent = openFile_ok
                # For now use arbitrary message "sentIMage to denote message sent"
                message = f"{self.username}: {self.uuid}: SentImage: {tobesent} \n"
                findmessage = message[
                              find_nth_overlapping(message, " ", 2):find_nth_overlapping(message, " ", 3)].replace(":",
                                                                                                                   "").strip()
                self.sock.send(message.encode('utf-8'))
                # Check if userID matches and then display
                if self.uuid == self.uuid:
                    self.model.add_message(USER_ME, findmessage, time(), self.username, "#90caf9", image)
                self.textEdit.clear()
                self.textEdit.setHtml(self.getTextStyles)
        else:
            pass

    def write(self):
        """This function gets the message and sends it to the server which broadcasts it"""
        message = f"{self.username} > {self.textEdit.toPlainText()} \n"
        # if message:
        message = message.encode('utf-8')
        message_header = f'{len((message)):< {HEADER_LENGTH}}'.encode('utf-8')
        self.sock.send(message_header + message)
        self.model.add_message(USER_ME, self.textEdit.toPlainText(), time(), self.username.decode('utf-8'), "#90caf9")

        # Check if userID matches and then display
        # if self.uuid == self.uuid:
        #     self.model.add_message(USER_ME, self.textEdit.toPlainText(), time(), self.username.decode('utf-8'), "#90caf9")
        self.textEdit.clear()
        self.textEdit.setHtml(self.getTextStyles)

    # def receive(self):
    #     """While client is running decode every message from the server and insert it as plain text
    #     Close connection if there is a disconnect or error"""
    #     while self.running:
    #         full_message  = ''
    #         new_message  = True
    #         while True:
    #             text = self.sock.recv(8192)
    #             if new_message:
    #                 print(f"New Message Length: {text[:HEADER_SIZE]}")
    #             try:
    #                 # Don't Check messages here because at when NICK is sent, you haven't received the message yet to
    #                 # break into pieces
    #                 text = self.sock.recv(8192)
    #                 message = text.decode('utf-8')
    #                 if message == 'NICK':
    #                     self.sock.send(self.nickname.encode('UTF-8'))
    #                 #     Parse Everything here including usernames and color (admin)
    #                 elif any(check in message for check in s_messages):
    #                     r_adminNick = message.split(':')[0]
    #                     r_adminMessage = message.split(':')[-1]
    #                     self.model.add_message(USER_ADMIN, r_adminMessage, time(), r_adminNick, "#FFFFFF")
    #                     # Find Users and Append Them to List
    #                     find_names = message[message.find("(") + 1:   message.find(")")]
    #                     if s_messages[0] in find_names:
    #                         find_names = find_names.replace(s_messages[0], "").rstrip()
    #                     elif s_messages[1] in find_names:
    #                         find_names = find_names.replace(s_messages[1], "").rstrip()
    #                     else:
    #                         find_names = find_names.replace("\n", "")
    #                     # Append color to any user who joins by stripping connected server
    #                     for users in find_names.split(','):
    #                         clientList.append(users)
    #                     # Add and assign user color here
    #                     for names in clientList:
    #                         if names not in clientColor:
    #                             clientColor[names] = rand_color()
    #                 else:
    #                     if self.gui_done:
    #                         # Message form ['Username[0] ', 'UUID[1]', 'Message[2]']
    #                         if not message:
    #                             break
    #                         else:
    #                             fragments.append(message)
    #                         # Get all data from databytes
    #                         print(fragments)
    #                         data_bytes = "".join(fragments).strip("\n")
    #                         # !Username Find Properly
    #                         findusername = data_bytes[0:find_nth_overlapping(data_bytes, ":", 1)].strip('\n')
    #                         # !Find ID
    #                         find_user_ID = data_bytes[
    #                                        find_nth_overlapping(data_bytes, ":", 1):find_nth_overlapping(data_bytes, ":",
    #                                                                                                      2)]
    #                         find_user_ID = find_user_ID.replace(':', "", 1).replace(" ", "", 1)
    #                         # !Find Message Here
    #                         find_message = data_bytes[
    #                                        find_nth_overlapping(data_bytes, ":", 2) + 1:find_nth_overlapping(data_bytes,
    #                                                                                                          "b'",
    #                                                                                                          1)].strip('\n')
    #                         find_message = find_message.replace(' ', '', 1)
    #                         # !Find the rest here
    #                         found_bytes = data_bytes[find_nth_overlapping(data_bytes, " ", 3):].replace(" ", "", 1)
    #                         print(found_bytes)
    #                         image = QImage()
    #                         # testimage = PillowImage.open(io.BytesIO(prepImage))
    #                         # testimage.show()
    #                         if len(found_bytes) > 1:
    #                             try:
    #                                 prepImage = ast.literal_eval(found_bytes)
    #                             except (ValueError, NameError,SyntaxError):
    #                                 prepImage = None
    #                         else:
    #                             prepImage = None
    #
    #                         image.loadFromData(prepImage)
    #                         # Fail Safe Here
    #                         if self.nickname == find_user_ID:
    #                             break
    #                         if self.uuid not in find_user_ID:
    #                             if  prepImage is None:
    #                                 self.model.add_message(USER_THEM, find_message, time(), findusername,
    #                                                        clientColor[findusername])  # clientColor[r_nickname]
    #                             else:
    #                                 self.model.add_message(USER_THEM, find_message, time(), findusername,
    #                                                        clientColor[findusername], image)  # clientColor[r_nickname]
    #                         fragments.clear()
    #             except ConnectionAbortedError:
    #                 break
    #             except OSError as e:
    #                 print(e)
    #                 self.sock.close()
    #                 break

    def receive(self):
        try:
            while True:
                username_header = self.sock.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("Connection closed by the server")
                    sys.exit()
                # Get USERNAME
                username_length = int(username_header.decode('utf-8').strip())
                username = self.sock.recv(username_length).decode('utf-8')
                # GET MESSAGE HERE
                message_header = self.sock.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = self.sock.recv(message_length).decode('utf-8')

                # Print OTHER MESSAGE HERE
                self.model.add_message(USER_THEM, message, time(), username,"#a5d6a7")  # clientColor[r_nickname]
                print(f'{username} > {message}')
                print("Username:",username)
                print("Message:",message)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print("reading error:",str(e))
                sys.exit()


        except Exception as e:
            print('General Error:',str(e))
            sys.exit()

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
            new_width = 180
            self.UserLayout.setContentsMargins(-53, 0, -51, 9)
        else:
            new_width = 50
            self.UserLayout.setContentsMargins(51, 0, 51, 9)
        # Animate the transition
        self.animation = QPropertyAnimation(self.SlidingMenu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def emoji_pane(self):
        """Function To create Sliding Left Menu With QFrame"""
        width = self.EmojiPane.width()
        if width == 0:
            new_width = 296
        else:
            new_width = 0
        # Animate the transition
        self.emoji_panel = QPropertyAnimation(self.EmojiPane, b"minimumWidth")
        self.emoji_panel.setDuration(250)
        self.emoji_panel.setStartValue(width)
        self.emoji_panel.setEndValue(new_width)
        self.emoji_panel.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.emoji_panel.start()

    # ---------BUBBLE STUFF--------------
    def bubbleChat(self):
        """ Attach model view to message view here, creating a list view is no longer needed as it pre-created  """
        # Start listview here
        # Use our delegate to draw items in this view.
        self.messagesView.setItemDelegate(MessageDelegate())
        self.model = MessageModel()
        self.messagesView.setModel(self.model)

    def resizeEvent(self, e):
        self.model.layoutChanged.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientCode = ClientCode(HOST, PORT)
    clientCode.show()
    sys.exit(app.exec_())
