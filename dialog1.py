# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QInputDialog, QLineEdit)
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#
#     def initUi(self):
#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le = QLineEdit(self)
#         self.le.move(130, 22)
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Test')
#         self.show()
#     def showDialog(self):
#
#         text, ok = QInputDialog.getText(self, 'Input DIalog', 'Enter your name: ')
#
#         if ok:
#             self.le.setText(str(text))
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFrame
# from PyQt5.QtGui import QColor
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         col = QColor(0, 0, 0)
#
#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#
#         self.btn.clicked.connect(self.showDialog)
#
#         self.frm = QFrame(self)
#         self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)
#
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Test')
#         self.show()
#
#     def showDialog(self):
#
#         col = QColorDialog.getColor()
#
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QFontDialog, QSizePolicy, QVBoxLayout)
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUi()
#
#     def initUi(self):
#         vbox = QVBoxLayout()
#
#         btn = QPushButton('Dialog', self)
#         btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#
#         btn.move(20, 20)
#         vbox.addWidget(btn)
#         btn.clicked.connect(self.showDialog)
#         self.lbl = QLabel('Knowlege only matter', self)
#         self.lbl.move(130, 20)
#
#         vbox.addWidget(self.lbl)
#         self.setLayout(vbox)
#         self.setGeometry(300, 300, 250, 180)
#         self.show()
#
#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.lbl.setFont(font)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, QFileDialog)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('smiley5.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        menubar.setNativeMenuBar(False)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Test')
        self.show()
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print(fname)
        if fname:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())