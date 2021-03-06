
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/unnamed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(285, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(282, 290, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Button_Vietnamese = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Vietnamese.setGeometry(QtCore.QRect(30, 560, 93, 28))
        self.Button_Vietnamese.setObjectName("Button_Vietnamese")
        self.Button_English = QtWidgets.QPushButton(self.centralwidget)
        self.Button_English.setGeometry(QtCore.QRect(180, 560, 93, 28))
        self.Button_English.setObjectName("Button_English")
        self.Button_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Clear.setGeometry(QtCore.QRect(330, 560, 93, 28))
        self.Button_Clear.setObjectName("pushButton_5")
        self.Button_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Exit.setGeometry(QtCore.QRect(480, 560, 93, 28))
        self.Button_Exit.setObjectName("Button_Exit")
        self.bot_chat = QtWidgets.QTextEdit(self.centralwidget)
        self.bot_chat.setGeometry(QtCore.QRect(10, 330, 580, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bot_chat.setFont(font)
        self.bot_chat.setObjectName("bot_chat")
        self.me_chat = QtWidgets.QTextEdit(self.centralwidget)
        self.me_chat.setGeometry(QtCore.QRect(10, 70, 580, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.me_chat.setFont(font)
        self.me_chat.setObjectName("me_chat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Assistant"))
        self.label_2.setText(_translate("MainWindow", "ME"))
        self.label_3.setText(_translate("MainWindow", "BOT"))
        self.Button_Vietnamese.setText(_translate("MainWindow", "Vietnamese"))
        self.Button_English.setText(_translate("MainWindow", "English"))
        self.Button_Exit.setText(_translate("MainWindow", "Exit"))
        self.Button_Clear.setText(_translate("MainWindow", "Clear"))
import bg
import icon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
