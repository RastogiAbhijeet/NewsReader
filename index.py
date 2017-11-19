from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import threading
import time
class Loader(object):

    def __init__(self):
        self.MainWindow = QMainWindow()
        self.MainWindow.resize(400,300)
        self.MainWindow.setWindowFlags(Qt.FramelessWindowHint)


    def changeProgress(self):
        value = 0
        for i in range(101):
            value = i
            self.progressBar.setValue(value)
            time.sleep(0.5)
            print(value)

    def setupUi(self):



        label = QLabel(self.MainWindow)
        label.setText("skskf")

        self.progressBar = QProgressBar(self.MainWindow)
        self.progressBar.setGeometry(QRect(0,150,400,8))
        self.progressBar.setEnabled(True)
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet("border:None;")

        self.MainWindow.show()

app = QApplication(sys.argv)
obj = Loader()

threadOne = threading.Thread(target=obj.setupUi())
# threadTwo = threading.Thread(target=obj.changeProgress())

threadOne.start()
# threadTwo.start()

# obj.setupUi()
# obj.changeProgress()



sys.exit(app.exec_())
