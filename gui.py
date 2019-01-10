#from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
#
##########Процедурное создание окна###################
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()
#
#     sys.exit(app.exec_())
#
#########ООП(класс окна с иконкой)###################
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('smiley.png'))
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
###################Подсказки#################
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSarif', 10))
#         self.setToolTip('This is a <b>QWidget</b> widget')
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Tooltips')
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
###############Сигналы и слоты###################
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtCore import QCoreApplication
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
#         qbtn = QPushButton('Quit', self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Quit button')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        print(qr)
        cp = QDesktopWidget().availableGeometry().center()
        print(cp)
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())