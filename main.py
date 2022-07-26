from PyQt5 import QtCore, QtGui, QtWidgets
import snake
import pygame

s = snake

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speedTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.speedTextEdit.setGeometry(QtCore.QRect(290, 10, 104, 31))
        self.speedTextEdit.setAcceptRichText(False)
        self.speedTextEdit.setObjectName("speedTextEdit")
        self.gridSizeTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.gridSizeTextEdit.setGeometry(QtCore.QRect(290, 50, 104, 31))
        self.gridSizeTextEdit.setAcceptRichText(False)
        self.gridSizeTextEdit.setObjectName("gridSizeTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 281, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 381, 38))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.save_data_to_snek)

        try:
            speed = 0
            grid = 0
            file = open('speed.txt', 'r')
            speed = int(file.read())
            file = open('grid.txt', 'r')
            grid = file.read()
            file.close()
        except FileNotFoundError:
            pass

        self.speedTextEdit.setText(str(speed))
        self.gridSizeTextEdit.setText(str(grid))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snek game"))
        self.speedTextEdit.setPlaceholderText(_translate("MainWindow", "Enter num:"))
        self.gridSizeTextEdit.setPlaceholderText(_translate("MainWindow", "Enter num:"))
        self.label.setText(_translate("MainWindow", "Set snek speed (updates per second):"))
        self.label_2.setText(_translate("MainWindow", "Set the grid size (8 is for 8x8 for example):"))
        self.pushButton.setText(_translate("MainWindow", "Start game"))

    def save_data_to_snek(self):
        try:
            s.grid_size = int(str(self.gridSizeTextEdit.toPlainText()))
            s.speed = int(str(self.speedTextEdit.toPlainText()))

            # FOR LAUNCHING THE GAME CODE HERE
            s.q = pygame.display.set_mode((s.tile_size * s.grid_size, s.tile_size * s.grid_size))

            MainWindow.close()
            s.apple_generate()

            file = open('speed.txt', 'w')
            file.write(str(s.speed))
            file.close()

            file = open('grid.txt', 'w')
            file.write(str(s.grid_size))
            file.close()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            s.direction = 'right'

                        if event.key == pygame.K_a:
                            s.direction = 'left'

                        if event.key == pygame.K_w:
                            s.direction = 'up'

                        if event.key == pygame.K_s:
                            s.direction = 'down'

                s.move(s.direction)

                s.c.tick(s.speed)

        except ValueError:
            print("error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())