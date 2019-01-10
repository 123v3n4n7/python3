# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber,
#                              QVBoxLayout, QSlider, QApplication)
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         lcd = QLCDNumber(self)
#         slider = QSlider(Qt.Horizontal, self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(slider)
#
#         self.setLayout(vbox)
#         slider.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Сигнал и слот')
#         self.show()
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         btn1 = QPushButton('Button 1', self)
#         btn1.move(30, 50)
#
#         btn2 = QPushButton('Button 2', self)
#         btn2.move(150, 50)
#
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Test')
#         self.show()
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + "was clicked")
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import  QApplication, QMainWindow

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Test')
        self.show()
    def mousePressEvent(self, QMouseEvent):
        self.c.closeApp.emit()
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())