import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем QLabel и устанавливаем в него изображение
        self.photo_label = QLabel(self)
        pixmap = QPixmap('example.jpg')
        self.photo_label.setPixmap(pixmap)
        self.setCentralWidget(self.photo_label)

        # Создаем действия для меню
        self.pencil_action = QAction('Pencil', self, checkable=True)
        self.pencil_action.triggered.connect(self.toggle_pencil)

        # Создаем меню и добавляем в него действия
        tools_menu = self.menuBar().addMenu('Tools')
        tools_menu.addAction(self.pencil_action)

        # Создаем перо для рисования
        self.pen = QPen(QColor('black'), 5, Qt.SolidLine)

        # Флаг для отслеживания состояния карандаша
        self.pencil_enabled = False

    def toggle_pencil(self, state):
        # Метод, вызываемый при нажатии на кнопку "Pencil"
        if state:
            self.pencil_enabled = True
        else:
            self.pencil_enabled = False

    def mousePressEvent(self, event):
        # Обрабатываем событие нажатия кнопки мыши
        if self.pencil_enabled:
            # Если карандаш включен, то начинаем рисование
            pixmap = self.photo_label.pixmap()
            painter.begin()
            painter = QPainter(pixmap)
            painter.setPen(self.pen)
            painter.drawPoint(event.pos())

            self.photo_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
