from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class Bubble(QLabel):
    def __init__(self, text):
        super(Bubble, self).__init__(text)
        self.setContentsMargins(5, 5, 5, 5)

    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing, True)
        p.drawRoundedRect(0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(Bubble, self).paintEvent(e)


class MyWidget(QWidget):
    def __init__(self, text, left=True):
        super(MyWidget, self).__init__()
        hbox = QHBoxLayout()
        label = Bubble(text)

        if not left:
            hbox.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Preferred))
        hbox.addWidget(label)

        if left:
            hbox.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Preferred))
        hbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hbox)
        self.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    a = QApplication([])
    w = QWidget()

    vbox = QVBoxLayout()

    vbox.addWidget(MyWidget("Left side"))
    vbox.addWidget(MyWidget("Right side", left=False))
    vbox.addWidget(MyWidget("Left side"))
    vbox.addWidget(MyWidget("Left side"))

    w.setLayout(vbox)
    w.show()

    a.exec_()
