from datetime import datetime

from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, Qt, QSize
from PyQt5.QtGui import QColor, QTextDocument, QTextOption, QFont, QPixmap
# from PyQt5.QtGui import
from PyQt5.QtWidgets import (
    QStyledItemDelegate
)

USER_ME = 0
USER_THEM = 1
USER_ADMIN = 2

BUBBLE_COLORS = {USER_ME: "#90caf9", USER_THEM: "#a5d6a7", USER_ADMIN: "#FFFFFF"}
USER_TRANSLATE = {USER_ME: QPoint(20, 0), USER_THEM: QPoint(0, 0), USER_ADMIN: QPoint(0, 0)}

BUBBLE_PADDING = QMargins(15, 5, 35, 5)
TEXT_PADDING = QMargins(25, 15, 45, 15)
IMAGE_PADDING = QMargins(30, 60, 50, 60)
# for ADMIN (left-margin, top-margin, right margin, bottom margin)

class MessageDelegate(QStyledItemDelegate):
    """
    Draws each message.
    """

    _font = None

    def paint(self, painter, option, index):
        painter.save()
        # Retrieve the user,message tuple from our model.data method.
        user, text, timestamp, username, user_color,image = index.model().data(index, Qt.DisplayRole)
        # ... add timestamp param, keep the rest the same until top...

        trans = USER_TRANSLATE[user]
        painter.translate(trans)

        # option.rect contains our item dimensions. We need to pad it a bit
        # to give us space from the edge to draw our shape.
        bubblerect = option.rect.marginsRemoved(BUBBLE_PADDING)
        textrect = option.rect.marginsRemoved(TEXT_PADDING)
        imagerect = option.rect.marginsRemoved(IMAGE_PADDING)

        # draw the bubble, changing color + arrow position depending on who
        # sent the message. the bubble is a rounded rect, with a triangle in
        # the edge.
        painter.setPen(Qt.NoPen)
        color = QColor(BUBBLE_COLORS[user])
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        # Draw User Colors Here
        painter.setPen(Qt.NoPen)
        color = QColor(user_color)
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        # TODO Draw User Image Here
        painter.setPen(Qt.NoPen)
        d_image = QPixmap(image)
        painter.drawPixmap(imagerect, d_image)
        # painter.drawRoundedRect(bubblerect, 10, 10)

        # draw the triangle bubble-pointer, starting from the top left/right.
        if user == USER_ME:
            p1 = bubblerect.topRight()
        else:
            p1 = bubblerect.topLeft()
        if user == USER_ADMIN:
            p1 = bubblerect.center()
        painter.drawPolygon(p1 + QPoint(-20, 0), p1 + QPoint(20, 0), p1 + QPoint(0, 20))
        # Set alignment options here
        toption = QTextOption()
        toption.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        # Set Alignment Options Here for center
        coption = QTextOption()
        coption.setAlignment(Qt.AlignHCenter)
        coption.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        # draw the timestamp
        font = painter.font()
        # font.setPointSize(7)
        font.setPointSize(8)
        painter.setFont(font)
        painter.setPen(Qt.black)
        time_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        # painter timestamp depending on who said
        if user == USER_ADMIN:
            # painter.drawText(textrect.center() + QPoint(-40, 25), time_str) => default
            painter.drawText(textrect.center() + QPoint(-50, 25), time_str)
        else:
            painter.drawText(textrect.bottomLeft() + QPoint(5, 5), time_str)
        # End timestamp Here

        # Draw User-name here
        if user == USER_ADMIN:
            painter.drawText(textrect.center(), "")
        else:
            painter.setFont(QFont("Segoe UI", 9, QFont.ExtraBold))
            painter.drawText(textrect.topLeft() + QPoint(5, 5), username)

        # draw the text
        doc = QTextDocument(text)
        doc.setTextWidth(textrect.width())
        doc.setDefaultTextOption(toption)
        doc.setDocumentMargin(0)
        # Set font here, you must also set font in the size hinting
        textfont = QFont('Segoe UI', 10)
        doc.setDefaultFont(textfont)
        # doc.setHtml("<p style=\" margin-top:0px; "
        #                                                                           "margin-bottom:0px; "
        #                                                                           "margin-left:0px; "
        #                                                                           "margin-right:0px; "
        #                                                                           "-qt-block-indent:0; "
        #
        #                                                                           "text-indent:0px;\"><img "
        #                                                                           "style=\"width:10pt\""
        #                                                                           "src=\":/EmojisOpened/emoji_1.png\"/>"
        #
        #                                                                           "</p> "
        #                                                                           )

        # Set where text should be drawn
        # For admin text
        if user == USER_ADMIN:
            doc.setDefaultTextOption(coption)
            painter.translate(textrect.topLeft())
        else:
            doc.setDocumentMargin(5)
            painter.translate(textrect.topLeft())

        doc.drawContents(painter)
        painter.restore()

    def sizeHint(self, option, index):
        _, text, _, _,_,image = index.model().data(index, Qt.DisplayRole)
        textrect = option.rect.marginsRemoved(TEXT_PADDING)

        toption = QTextOption()
        toption.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        doc = QTextDocument(text)
        doc.setTextWidth(textrect.width())
        doc.setDefaultTextOption(toption)
        doc.setDocumentMargin(0)
        # You must also set font size here
        textfont = QFont('Segoe UI', 10)
        doc.setDefaultFont(textfont)

        textrect.setHeight(int(doc.size().height()))
        textrect = textrect.marginsAdded(TEXT_PADDING)

        if image:
            textrect.setHeight(int(doc.size().height()+400))
            textrect = textrect.marginsAdded(BUBBLE_PADDING)
        return textrect.size() + QSize(0, 15)


class MessageModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(MessageModel, self).__init__(*args, **kwargs)
        self.messages = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Here we pass the delegate the user, message tuple.
            return self.messages[index.row()]

    def setData(self, index, role, value):
        self._size[index.row()]

    def rowCount(self, index):
        return len(self.messages)

    def add_message(self, who, text, timestamp, username,user_color,image=None):
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.messages.append((who, text, timestamp, username,user_color,image))
            # Trigger refresh.
            self.layoutChanged.emit()
