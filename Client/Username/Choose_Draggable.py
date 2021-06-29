from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QMessageBox

from Client.Username.Username_UI import Ui_Dialog


class Draggable(Ui_Dialog, QDialog):
    def __init__(self):
        super(Draggable, self).__init__()
        self.setupUi(self)
        # <MainWindow Properties>
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        self.oldPos = self.pos()
        self.SaveDetails.clicked.connect(self.saved_messagebox)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def saved_messagebox(self):
        if self.lineEdit.text() != "":
            # QMessageBox.information(self, "Information", "Username Saved Successfully")
            self.accept()
        elif self.lineEdit.text() == "":
            QMessageBox.warning(self, "Warning", "You must input at least one character")



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Draggable()
    window.show()
    sys.exit(app.exec_())
