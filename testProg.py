import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QSlider, QLabel


class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем элементы пользовательского интерфейса
        self.combo_box = QComboBox()
        self.combo_box.addItems(['Медианный', 'Линейный', 'Адаптивный'])
        self.slider = QSlider(Qt.Horizontal)
        self.label = QLabel()

        # Настраиваем макет
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Загружаем изображение
        self.image = cv2.imread('moscow.png')

        # Настраиваем обработчики событий
        self.combo_box.currentIndexChanged.connect(self.apply_filter)
        self.slider.valueChanged.connect(self.apply_filter)

        # Отображаем изображение
        self.update_image()

    def apply_filter(self):
        # Получаем выбранный фильтр
        filter_name = self.combo_box.currentText()

        # Получаем значение слайдера
        filter_strength = self.slider.value() * 2 + 1

        # Обрабатываем изображение с помощью выбранного фильтра
        if filter_name == 'Медианный':
            filtered_image = cv2.medianBlur(self.image, filter_strength)
        elif filter_name == 'Линейный':
            filtered_image = cv2.blur(
                self.image, (filter_strength, filter_strength))
        else:
            filtered_image = cv2.adaptiveThreshold(
                self.image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, filter_strength, 2)

        # Обновляем изображение
        self.image = filtered_image
        self.update_image()

    def update_image(self):
        # Конвертируем изображение в формат, подходящий для отображения в QLabel
        # q_image = QPixmap.fromImage(
        #     cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        pict = self.image
        qimage = QImage(
            pict.data, pict.shape[1], pict.shape[0], QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimage)
        # Устанавливаем изображение в QLabel
        self.label.setPixmap(qpixmap)


if __name__ == '__main__':
    app = QApplication([])
    window = ImageProcessor()
    window.show()
    app.exec_()
