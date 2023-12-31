from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        # Jarvis Image Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, -60, 821, 431))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setPixmap(QtGui.QPixmap("/Images/jarvis.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        # RUN Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 440, 121, 31))
        self.pushButton.setStyleSheet(
            "background-color: rgb(32, 99, 143);"
            "color: rgb(0, 0, 0);"
            "font: 75 8pt \"Myanmar Text\";"
            "border: 2px solid white;"
            "border-radius: 15px;"
        )
        self.pushButton.setObjectName("pushButton")

        # EXIT Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 480, 121, 31))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(200, 37, 53);"
            "color: rgb(0, 0, 0);"
            "font: 75 8pt \"Myanmar Text\";"
            "border-radius: 15px;"
            "border: 2px solid white;"
        )
        self.pushButton_2.setObjectName("pushButton_2")

        # Terminal Output
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 360, 571, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(
            "background-color: black;"
            "color: rgb(255, 255, 255);"
        )
        self.plainTextEdit.setObjectName("plainTextEdit")

        # User Input LineEdit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 530, 571, 41))
        self.lineEdit.setStyleSheet(
            "background-color: black;"
            "color: rgb(255, 255, 255);"
        )
        self.lineEdit.setObjectName("lineEdit")

        # Enter Button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 540, 75, 23))
        self.pushButton_3.setStyleSheet(
            "color: rgb(235, 235, 235);"
            "border-color: rgb(218, 218, 218);"
            "background-color: transparent;"
        )
        self.pushButton_3.setObjectName("pushButton_3")

        # Text Browsers
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(630, 0, 171, 31))
        self.textBrowser.setStyleSheet(
            "background: transparent;"
            "border-radius: none;"
        )
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(630, 30, 171, 31))
        self.textBrowser_2.setStyleSheet(
            "background: transparent;"
            "border-radius: none;"
        )
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Jarvis Logo Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 231, 121))
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setPixmap(QtGui.QPixmap("/Images/JLogo.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        # Initializing Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 30, 281, 111))
        self.label_4.setPixmap(QtGui.QPixmap("/Images/inilializing.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Terminal output Box"))
        self.lineEdit.setText(_translate("MainWindow", " "))
        self.pushButton_3.setText(_translate("MainWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
