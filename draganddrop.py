# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit)
#
# class Button(QPushButton):
#     def __init__(self, title, parent):
#         super().__init__(title, parent)
#         self.setAcceptDrops(True)
#     def dragEnterEvent(self, e):
#         if e.mimeData().hasText:
#             e.accept()
#         else: e.ignore()
#     def dropEvent(self, e):
#         self.setText(e.mimeData().text())
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         edit = QLineEdit('', self)
#         edit.setDragEnabled(True)
#         edit.move(30, 65)
#
#         button = Button('Button', self)
#         button.move(190, 65)
#
#         self.setWindowTitle('Simple Drag and Drop')
#         self.setGeometry(300, 300, 300, 150)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     app.exec_()

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        print(e.pos())
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)
    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setAcceptDrops(True)
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('click or move')
        self.setGeometry(300, 300, 280, 150)
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()