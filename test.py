from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout


class Sketchpad(QWidget):
    def __init__(self):
        super().__init__()
        self.last_point = None
        self.pen = QPen(Qt.black, 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        if self.last_point:
            painter.drawPoint(self.last_point)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            painter = QPainter(self)
            painter.setPen(self.pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sketchpad = Sketchpad()
        layout = QVBoxLayout()
        layout.addWidget(self.sketchpad)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Sketchpad')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
