import socket
import sys
import threading
import errno

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, QTimer
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QMenu

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from Client.Bubble.LabelBubble import MessageDelegate, MessageModel, USER_ME, USER_THEM, USER_ADMIN
from Client.Username.Choose_Draggable import Draggable
from Client.Client_UI import Ui_MainWindow

import random
import colorsys
from time import time
# import uuid

# from PIL import Image as PillowImage

import ast

from DropButton.dropbutton import DropButton

HOST = '127.0.0.1'
PORT = 1234
# Server Messages
s_messages = ('connected to the server!', 'disconnected from the server!')
HEADER_LENGTH = 8192


# ============ Helpers ==============
# Random Color Generator
def rand_color():
    h, s, l = random.uniform(0, 360) / 360, random.uniform(0.2, 1), random.uniform(0.5, 1)
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return '#%02X%02X%02X' % (r, g, b)


# def fancy_dict(*args):
#     'Pass in a list of tuples, which will be key/value pairs'
#     ret = {}
#     for k, v in args:
#         for i in k:
#             ret[i] = v
#     return ret
#

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


def set_message_color(username):
    clientList.append(username)
    for names in clientList:
        if names not in clientColor:
            clientColor[names] = rand_color()


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
        self.send_server_messages()

    def threading(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def create_emojis(self):
        buttons = {}
        for i in range(27):  # controls rows
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
        curr_moji_length = len(self.Emo_Smiles.children()[1:162]) + 1
        for items in range(0, curr_moji_length):
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/EmojisOpened/emoji_{items}.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            icons.append(icon)
        for index, item in enumerate(self.Emo_Smiles.children()[1:163]):
            item.setIcon(icons[index])
            item.setIconSize(QtCore.QSize(32, 32))

        self.create_emojis_dropdown()

    def create_emojis_dropdown(self):
        buttons = {}
        for i in range(27, 34):  # controls rows example: range(27, 34) means 7 rows
            for j in range(6):  # controls columns
                # keep a reference to the buttons
                buttons[(i, j)] = DropButton(self.Emo_Smiles)
                buttons[(i, j)].setObjectName(f'emoji_{j}_smiles')
                buttons[(i, j)].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                buttons[(i, j)].setFlat(True)
                # add to the layout
                self.gridLayout_2.addWidget(buttons[(i, j)], i, j)
        # Display Emojis
        icons = []
        # Affect Only Emojis 162 to 205 or the first 42 emojis (for testing)
        curr_moji_length = len(self.Emo_Smiles.children()[163:205])

        initial_counter = 163
        for items in range(0, curr_moji_length):
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/Yellow/emoji_{initial_counter}.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            initial_counter += 6
            # if initial_counter == 385:
            #     initial_counter = 405
            icons.append(icon)

        for index, item in enumerate(self.Emo_Smiles.children()[163:205]):
            item.setIcon(icons[index])
            item.setIconSize(QtCore.QSize(32, 32))
        # Set dynamic button before sub menu here from dynamic emojis list which contains all yellows
        for index,item in enumerate(self.Emo_Smiles.children()[163:205]): # starts from button 163 to 205
            item.clicked.connect(lambda checked, text=index: self.textEdit.insertPlainText(self.dynamic_emojis[text]))

        self.dynamic_emojis_menu()

    def dynamic_emojis_menu(self):
        # item.clicked.connect(lambda checked, text=index: self.textEdit.insertPlainText(self.emojis[text]))
        button_index = 164
        emoji_index = 0
        jump = [i for i in range(163, 424, 6)]
        # jump_icon = [i for i in range(385,404)]
        display_icons = []

        # Set Icons HEre
        for items in range(164, 424):
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/EmojisOpened/emoji_{items}.png"))
            # print(items)
            display_icons.append(icon)
        # Set actions for sub menus here
        for button in self.Emo_Smiles.children()[163:424]:
            self.menu_emoji = QMenu()
            if button_index in jump:
                button_index += 1
                emoji_index += 1
            self.menu_emoji.addAction(display_icons[emoji_index], "",
                                      lambda index=button_index: self.textEdit.insertPlainText(self.emojis[index]))
            button_index += 1
            emoji_index += 1
            self.menu_emoji.addAction(display_icons[emoji_index], "",
                                      lambda index=button_index: self.textEdit.insertPlainText(self.emojis[index]))
            button_index += 1
            emoji_index += 1
            self.menu_emoji.addAction(display_icons[emoji_index], "",
                                      lambda index=button_index: self.textEdit.insertPlainText(self.emojis[index]))
            button_index += 1
            emoji_index += 1
            self.menu_emoji.addAction(display_icons[emoji_index], "",
                                      lambda index=button_index: self.textEdit.insertPlainText(self.emojis[index]))
            button_index += 1
            emoji_index += 1
            self.menu_emoji.addAction(display_icons[emoji_index], "",
                                      lambda index=button_index: self.textEdit.insertPlainText(self.emojis[index]))
            button_index += 1
            emoji_index += 1
            button.setMenu(self.menu_emoji)

    def uiFunctions(self):
        self.Hamburger.clicked.connect(self.slide_left_menu)
        self.Send_Button.clicked.connect(self.write)
        self.emojiButton.clicked.connect(self.emoji_pane)
        self.attachButton.clicked.connect(self.send_image)
        # Emojis
        # Get emojis from text file
        self.emojis = []

        self.textEdit.document()
        # cursor = QTextCursor(textArea)
        with open('EmojiList.txt', 'r', encoding="utf8") as file:
            self.emojis = file.read().splitlines()
        for index, item in enumerate(self.Emo_Smiles.children()[1:163]):
            # Add option to insert html image instead of plain text after inserting images in qlistview
            item.clicked.connect(lambda checked, text=index: self.textEdit.insertPlainText(self.emojis[text]))
            # item.clicked.connect(lambda checked, text=index: cursor.insertImage(f":/EmojisOpened/emoji_{text}.png"))
        self.dynamic_emojis = self.emojis[163::6]
        print(self.dynamic_emojis)
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

    def send_server_messages(self, s_msg_type="Connected"):
        """Send server messages upon connecting to server or disconnecting"""
        if s_msg_type == "Connected":
            message = f"{self.username} > connected to the server! \n".encode('utf-8')
            message_header = f'{len(message):< {HEADER_LENGTH}}'.encode('utf-8')
            self.sock.send(message_header + message)
            self.model.add_message(USER_ADMIN, "You Connected To the Server", time(), self.username.decode('utf-8'),
                                   "#ffffff")
        elif s_msg_type == "Disconnected":
            message = f"{self.username} > disconnected from the server! \n".encode('utf-8')
            message_header = f'{len(message):< {HEADER_LENGTH}}'.encode('utf-8')
            self.sock.send(message_header + message)

    def write(self):
        """This function gets the message and sends it to the server which broadcasts it"""
        message = f"{self.username} > {self.textEdit.toPlainText()} \n".encode('utf-8')
        message_header = f'{len((message)):< {HEADER_LENGTH}}'.encode('utf-8')
        self.sock.send(message_header + message)
        self.model.add_message(USER_ME, self.textEdit.toPlainText(), time(), self.username.decode('utf-8'), "#90caf9")
        self.textEdit.clear()
        self.textEdit.setHtml(self.getTextStyles)

    def send_image(self, open_file=None):
        if not open_file:
            open_file = QFileDialog.getOpenFileName(None, 'Open File:', '', 'Images (*.png *.jpg)')
        if open_file[0]:
            with open(open_file[0], 'rb') as file:
                openFile_ok = file.read()
                image = QImage()
                image.loadFromData(openFile_ok)
                # For now use arbitrary message "sentIMage to denote message sent"
                message = f"{self.username} > {openFile_ok} \n".encode('utf-8')
                message_header = f'{len((message)):< {HEADER_LENGTH}}'.encode('utf-8')
                self.sock.send(message_header + message)
                self.model.add_message(USER_ME, "Sent Image", time(), self.username.decode('utf-8'), "#90caf9", image)
                self.textEdit.clear()
                self.textEdit.setHtml(self.getTextStyles)
        else:
            pass

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
                # AFTER GETTING USERNAME GET COLOR
                set_message_color(username)
                # GET MESSAGE HERE
                message_header = self.sock.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = self.sock.recv(message_length).decode('utf-8')
                message = message[message.find(">") + 1:].replace(" ", "", 1)
                # Check if admin then print message or nevermind
                if any(check in message.strip("\n") for check in s_messages):
                    self.model.add_message(USER_ADMIN, f'{username} {message}', time(), "", "#FFFFFF")
                else:
                    if message.startswith("b'"):
                        image = QImage()
                        image.loadFromData(ast.literal_eval(message))
                        self.model.add_message(USER_THEM, "Received Image", time(), username, clientColor[username],
                                               image)
                    else:
                        self.model.add_message(USER_THEM, message, time(), username, clientColor[username])
                print("Username:", username)
                print("Message:", message)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print("reading error:", str(e))
                sys.exit()

        except Exception as e:
            print('General Error:', str(e))
            sys.exit()

    def closeEvent(self, event):
        """Close Sock and Exit application"""
        self.send_server_messages("Disconnected")
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
            new_width = 400  # 296
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
