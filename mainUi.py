# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'haha.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from databaseHandling import InterfaceClass
# from webcam.webcam import Webcam
import sys

class Ui_MainWindow(object):

    def __init__(self):
        self.databaseObj = InterfaceClass()
        self.fetchDataList = []
        self.counterForNews = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(718, 530)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0,100);\n"
    "color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(5)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setIndent(155)
        self.label.setObjectName("label")
        self.tableEmoValue = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEmoValue.setGeometry(QtCore.QRect(20, 331, 281, 171))
        self.tableEmoValue.setMaximumSize(QtCore.QSize(281, 192))
        self.tableEmoValue.setObjectName("tableEmoValue")
        self.tableEmoValue.setColumnCount(2)
        self.tableEmoValue.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.tableEmoValue.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(False)
        item.setFont(font)
        self.tableEmoValue.setHorizontalHeaderItem(1, item)
        self.tableEmoValue.horizontalHeader().setVisible(True)
        self.tableEmoValue.verticalHeader().setVisible(True)
        self.tableEmoValue.verticalHeader().setHighlightSections(True)
        self.tableEmoValue.verticalHeader().setSortIndicatorShown(False)
        self.tableEmoValue.verticalHeader().setStretchLastSection(False)
        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        self.videoWidget.setGeometry(QtCore.QRect(20, 70, 281, 251))
        self.videoWidget.setObjectName("videoWidget")
        self.startTraining = QtWidgets.QPushButton(self.centralwidget)
        self.startTraining.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.startTraining.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"font: 75 13pt \"Myanmar Text\";\n"
"")
        self.startTraining.setObjectName("startTraining")
        self.topicSelection = QtWidgets.QComboBox(self.centralwidget)
        self.topicSelection.setGeometry(QtCore.QRect(320, 70, 381, 22))
        self.topicSelection.setObjectName("topicSelection")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 47, 13))
        self.label_2.setObjectName("label_2")

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(560, 470, 75, 23))
        self.nextButton.setStyleSheet("background-color: rgb(0, 0, 0,200);\n"
"color:rgb(255, 255, 255);\n"
"border:None;")
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.next_news)

        self.previousNews = QtWidgets.QPushButton(self.centralwidget)
        self.previousNews.setGeometry(QtCore.QRect(380, 470, 91, 23))
        self.previousNews.setStyleSheet("background-color: rgb(0, 0, 0,200);\n"
"color:rgb(255, 255, 255);\n"
"border:None;")
        self.previousNews.setObjectName("previousNews")
        self.previousNews.clicked.connect(self.prev_news)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.articleTitleText = QtWidgets.QTextBrowser(self.centralwidget)
        self.articleTitleText.setGeometry(QtCore.QRect(320, 210, 381, 31))
        self.articleTitleText.setStyleSheet("border:None;")
        self.articleTitleText.setObjectName("articleTitleText")
        self.articleText = QtWidgets.QTextEdit(self.centralwidget)
        self.articleText.setGeometry(QtCore.QRect(320, 250, 381, 211))
        self.articleText.setStyleSheet("border-top:None;")
        self.articleText.setObjectName("articleText")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(320, 100, 381, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.classificationOfArticleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classificationOfArticleLabel.setObjectName("classificationOfArticleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.classificationOfArticleLabel)
        self.classificationOfArticleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.classificationOfArticleLineEdit.setObjectName("classificationOfArticleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.classificationOfArticleLineEdit)
        self.polarityOfTheArticleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.polarityOfTheArticleLabel.setObjectName("polarityOfTheArticleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.polarityOfTheArticleLabel)
        self.polarityOfTheArticleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.polarityOfTheArticleLineEdit.setObjectName("polarityOfTheArticleLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.polarityOfTheArticleLineEdit)
        self.topicLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.topicLabel.setObjectName("topicLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.topicLabel)
        self.topicLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.topicLineEdit.setObjectName("topicLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.topicLineEdit)
        self.dateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dateLineEdit.setObjectName("dateLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateLineEdit)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(296, -10, 31, 561))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")

        self.displayButton = QtWidgets.QPushButton(self.centralwidget)
        self.displayButton.setGeometry(QtCore.QRect(170, 10, 121, 31))
        self.displayButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"font: 75 13pt \"Myanmar Text\";\n"
"")
        self.displayButton.setObjectName("displayButton")
        self.displayButton.clicked.connect(self.fetch_news)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NewsReader"))
        self.label.setText(_translate("MainWindow", "Articles"))
        item = self.tableEmoValue.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Emotion"))
        item = self.tableEmoValue.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.startTraining.setText(_translate("MainWindow", "Start Training"))
        self.label_2.setText(_translate("MainWindow", "Filter"))
        self.nextButton.setText(_translate("MainWindow", "Next News"))
        self.previousNews.setText(_translate("MainWindow", "Previous News"))
        self.label_3.setText(_translate("MainWindow", "Press the button to start training"))
        self.classificationOfArticleLabel.setText(_translate("MainWindow", "Classification of Article"))
        self.polarityOfTheArticleLabel.setText(_translate("MainWindow", "Polarity of the Article"))
        self.topicLabel.setText(_translate("MainWindow", "Topic"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.displayButton.setText(_translate("MainWindow", "Display News"))
        self.label_4.setText(_translate("MainWindow", "Press the button after training"))

    def fetch_news(self):
        temp_dict = self.databaseObj.fetchData()
        for document in temp_dict:
            self.fetchDataList.append(document)
        self.display_news(0)

    def display_news(self,index):
        self.articleText.setText(self.fetchDataList[index]["NewsData"])
        self.articleTitleText.setText(self.fetchDataList[index]["NewsTitle"])
        self.dateLineEdit.setText(self.fetchDataList[index]["Date"])
        self.polarityOfTheArticleLineEdit.setText(str(self.fetchDataList[index]["Sentiment"]))

    def next_news(self):
        self.counterForNews = self.counterForNews+1
        if self.counterForNews > len(self.fetchDataList)-1:
            self.counterForNews = 0
        self.display_news(self.counterForNews)
        pass

    def prev_news(self):
        self.counterForNews = self.counterForNews-1
        if self.counterForNews < 0:
            self.counterForNews = len(self.fetchDataList)-1
        self.display_news(self.counterForNews)
        pass

# print(obj.startModel())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())