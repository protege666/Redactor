import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QToolBar, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # создаем действия для тулбара
        self.pencil_action = QAction('Pencil', self)
        self.pencil_action.setCheckable(True)
        self.pencil_action.setChecked(True)
        self.pencil_action.triggered.connect(self.set_pencil)

        # создаем тулбар и добавляем действия
        self.toolbar = QToolBar()
        self.toolbar.addAction(self.pencil_action)
        self.addToolBar(self.toolbar)

        # создаем лейбл и добавляем его на главное окно
        self.photo_label = QLabel()
        self.setCentralWidget(self.photo_label)

        # устанавливаем начальные параметры для рисования карандашом
        self.drawing = False
        self.last_point = QPoint()

        # загружаем фото
        self.load_photo()

    def set_pencil(self, checked):
        # если выбран инструмент карандаш, включаем возможность рисования
        if checked:
            self.photo_label.mousePressEvent = self.mouse_press
            self.photo_label.mouseMoveEvent = self.mouse_move
            self.photo_label.mouseReleaseEvent = self.mouse_release
        # если выбран другой инструмент, отключаем возможность рисования
        else:
            self.photo_label.mousePressEvent = None
            self.photo_label.mouseMoveEvent = None
            self.photo_label.mouseReleaseEvent = None

    def load_photo(self):
        # открываем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "Image Files (*.png *.jpg *.bmp)")

        # загружаем фото и отображаем его в лейбле
        if file_name:
            pixmap = QPixmap(file_name)
            self.photo_label.setPixmap(pixmap)

    def mouse_press(self, event):
        # сохраняем текущую точку
        self.last_point = event.pos()
        self.drawing = True

    def mouse_move(self, event):
        # если выбран инструмент карандаш и мы рисуем, рисуем линию между последней точкой и текущей
        if self.pencil_action.isChecked() and self.drawing:
            painter = QPainter(self.photo_label.pixmap())
            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.photo_label.update()

    def mouse_release(self, event):
        self.drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
