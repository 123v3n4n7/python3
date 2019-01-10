# import sys
# from PyQt5.QtWidgets import (QWidget, QSlider,
#     QLabel, QApplication)
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         sld = QSlider(Qt.Horizontal, self)
#         sld.setFocusPolicy(Qt.NoFocus)
#         sld.setGeometry(30, 40, 100, 30)
#         sld.valueChanged[int].connect(self.changeValue)
#
#         self.label = QLabel(self)
#         self.label.setPixmap(QPixmap('smiley1.png'))
#         self.label.setGeometry(160, 40, 80, 30)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QSlider')
#         self.show()
#
#
#     def changeValue(self, value):
#
#         if value == 0:
#             self.label.setPixmap(QPixmap('smiley1.png'))
#         elif value > 0 and value <= 30:
#             self.label.setPixmap(QPixmap('smiley2.png'))
#         elif value > 30 and value < 80:
#             self.label.setPixmap(QPixmap('smiley4.png'))
#         else:
#             self.label.setPixmap(QPixmap('smiley5.png'))
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QWidget, QSlider, QLCDNumber, QVBoxLayout,
#     QLabel, QApplication)
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         sld = QSlider(Qt.Horizontal, self)
#         sld.setFocusPolicy(Qt.NoFocus)
#         sld.setGeometry(30, 40, 100, 30)
#         sld.valueChanged[int].connect(self.changeValue)
#
#         self.label = QLabel(self)
#         self.label.setPixmap(QPixmap('smiley1.png'))
#         self.label.setGeometry(160, 40, 80, 30)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QSlider')
#         self.show()
#
#
#     def changeValue(self, value):
#         if value:
#             lcd = QLCDNumber(self)
#             lcd.display(value)
#             vbox = QVBoxLayout()
#             vbox.addWidget(lcd)
#             self.setLayout(vbox)
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QProgressBar, QCalendarWidget, QMainWindow, QLabel)
# from PyQt5.QtCore import QBasicTimer, QDate
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#     def initUi(self):
#         self.timer = QBasicTimer()
#         self.progBar = QProgressBar(self)
#         self.progBar.setGeometry(30, 40, 200, 25)
#
#         self.btn = QPushButton('start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.lbl = QLabel(self)
#         self.lbl.move(130, 260)
#
#
#         self.step = 0
#
#         cal = QCalendarWidget(self)
#         cal.setGridVisible(True)
#         cal.move(180, 80)
#         date = cal.selectedDate()
#         print(date)
#         self.lbl.setText(date.toString())
#         cal.clicked[QDate].connect(self.showDate)
#         print(cal.clicked[QDate])
#
#         self.setGeometry(300, 300, 580, 170)
#         self.setWindowTitle('Test                        ')
#         self.show()
#
#     def showDate(self, date):
#         print(date)
#         self.lbl.setText(date.toString())
#
#
#     def timerEvent(self, QTimerEvent):
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#         self.step += 1
#         self.progBar.setValue(self.step)
#
#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QApplication)
# from PyQt5.QtGui import QPixmap
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#     def initUi(self):
#         hbox = QHBoxLayout(self)
#         pixmap = QPixmap('smiley1.png')
#
#         lbl = QLabel(self)
#         lbl.setPixmap(pixmap)
#
#         hbox.addWidget(lbl)
#         self.setLayout(hbox)
#         self.move(300, 200)
#         self.setWindowTitle('Smiley')
#         self.show()
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel,
#                              QLineEdit, QWidget)
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         self.lbl = QLabel(self)
#         qle = QLineEdit(self)
#
#         qle.move(60, 100)
#         self.lbl.move(20, 80)
#
#         qle.textChanged[str].connect(self.onChanged)
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QLineEdit')
#         self.show()
#
#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QSplitter, QStyleFactory, QHBoxLayout)
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#     def initUi(self):
#         hbox = QHBoxLayout(self)
#         topleft = QFrame(self)
#         topleft.setFrameShape(QFrame.StyledPanel)
#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)
#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)
#
#         splitter1 = QSplitter(Qt.Vertical)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#
#         splitter2 = QSplitter(Qt.Horizontal)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Splitter')
#         self.show()
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QComboBox, QLabel)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.lbl = QLabel("Ubuntu", self)
        combo = QComboBox(self)
        combo.addItems(["Ubuntu", "Gentoo", "Arch", "Fedora"])
        combo.move(50, 50)
        self.lbl.move(50, 100)
        combo.activated[str].connect(self.doAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ComboBox')
        self.show()
    def doAction(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())