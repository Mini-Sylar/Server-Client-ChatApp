from PyQt5 import QtCore, QtWidgets


class DropButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(DropButton, self).__init__(parent)

    def mousePressEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # figure out press location
            pos = event.pos
            topRight = self.rect().topRight()
            bottomRight = self.rect().bottomRight()
            frameWidth = self.style().pixelMetric(QtWidgets.QStyle.PM_DefaultFrameWidth)
            # print(topRight, bottomRight, frameWidth)
            # get the rect from QStyle instead of hardcode numbers here
            arrowTopLeft = QtCore.QPoint(topRight.x() - 20, topRight.y())
            arrowRect = QtCore.QRect(arrowTopLeft, bottomRight)

            if arrowRect.contains(event.pos()):
                # print('clicked near arrow')
                # event.accept()
                QtWidgets.QPushButton.mousePressEvent(self, event)
            else:
                # print('clicked outside')
                # call the slot connected, without popup the menu
                # the following code now does not make
                # the button pressed
                self.clicked.emit(True)
                event.accept()
