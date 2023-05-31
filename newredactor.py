from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from typing import Union
import cv2
from PyQt5.QtGui import QImage
import numpy as np
from PIL import Image


class Ui_MainWindow(object):
    # Метод для открытия диалога выбора файла и отображения фотографии
    def select_file(self):
        global file_name
        # Открываем диалог выбора файла
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self.checkPhotoBtn, "Выбрать фотографию", "", "Images (*.png *.xpm *.jpg *.bmp *.gif)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.photoLable.setPixmap(pixmap)

    # Метод для удаления фотографии
    def del_photo(self):
        self.photoLable.setPixmap(QPixmap(""))

    # Метод для применения фильтра к фотографии
    def apply_filter(self):
        filter_strength = self.Slider.value() * 2 + 1
        img = cv2.imread(file_name)
        # Обрабатываем изображение с помощью выбранного фильтра
        if self.comboBox.currentText() == 'Медианный':
            filtered_image = cv2.medianBlur(img, filter_strength)
        elif self.comboBox.currentText() == 'Линейный':
            filtered_image = cv2.blur(
                img, (filter_strength, filter_strength))
        elif self.comboBox.currentText() == 'Адаптивный':
            img = Image.open(file_name)
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = img.convert('L')
            # filtered_image = cv2.adaptiveThreshold(
            # gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, filter_strength, 2)
            filtered_image = gray

        return filtered_image

    # Метод для обновления фотографии

    def updatePhoto(self):
        pict = self.apply_filter()
        qimage = QImage(
            pict.data, pict.shape[1], pict.shape[0], QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimage)
        self.photoLable.setPixmap(qpixmap)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photoLable = QtWidgets.QLabel(self.centralwidget)
        self.photoLable.setGeometry(QtCore.QRect(20, 10, 351, 531))
        self.photoLable.setText("")
        self.photoLable.setObjectName("photoLable")
        self.checkPhotoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkPhotoBtn.setGeometry(QtCore.QRect(460, 190, 171, 61))
        self.checkPhotoBtn.setObjectName("checkPhotoBtn")
        # Сигнал для выбора файла
        self.checkPhotoBtn.clicked.connect(self.select_file)
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setGeometry(QtCore.QRect(400, 500, 321, 22))
        self.Slider.setMinimum(1)
        self.Slider.setMaximum(23)
        self.Slider.setSingleStep(1)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        # Сигнал для обновления фотографии
        self.Slider.valueChanged.connect(self.updatePhoto)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 460, 141, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 130, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(460, 270, 171, 61))
        self.restartButton.setObjectName("restartButton")
        self.DelButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelButton.setGeometry(QtCore.QRect(460, 350, 171, 61))
        self.DelButton.setObjectName("DelButton")
        # Сигнал для удаления фотографии
        self.DelButton.clicked.connect(self.del_photo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkPhotoBtn.setText(_translate("MainWindow", "Выбрать фото"))
        self.label.setText(_translate("MainWindow", "Интенсивность"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Медианный"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Линейный"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Адаптивный"))
        self.restartButton.setText(_translate("MainWindow", "Сброс фильтра"))
        self.DelButton.setText(_translate("MainWindow", "Удалить фото"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Инструменты"))
        self.action.setText(_translate("MainWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
