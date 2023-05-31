import cv2

# загрузка изображения
img = cv2.imread('moscow.png')

# преобразование в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# применение адаптивного порога
adaptive_threshold = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)

# отображение изображения с адаптивным порогом
cv2.imshow('Adaptive Threshold', adaptive_threshold)

# ожидание нажатия клавиши для закрытия окна
cv2.waitKey(0)

# освобождение ресурсов
cv2.destroyAllWindows()
