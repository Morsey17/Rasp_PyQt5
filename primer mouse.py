import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class EventFilter(QDialog):
    def __init__(self, parent=None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("Фильтр событий eventFilter")
        self.resize(400, 300)

        self.label1 = QLabel("Кликабельнай \nLabel\nПожалуйста, \nнажмите")
        self.label2 = QLabel("Label2")
        self.label3 = QLabel("Label3")
        self.labelState = QLabel("Результат кликов")

        self.image1 = QImage("E:/_Qt/img/qt-logo.png")

        self.label1.installEventFilter(self)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 5, 0)
        mainLayout.addWidget(self.label2, 5, 1)
        mainLayout.addWidget(self.label3, 5, 2)
        mainLayout.addWidget(self.labelState, 6, 1)
        self.setLayout(mainLayout)

    def eventFilter(self, obj, event):
        # Только фильтровать событие label1, переписать его поведение,
        # другие события будут проигнорированы
        if obj == self.label1:
            # здесь отфильтруйте событие mouse и перепишите его поведение
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.labelState.setText("Нажали левую кнопку мыши")
                elif mouseEvent.buttons() == Qt.MidButton:
                    self.labelState.setText("Нажали среднюю кнопку мыши")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.labelState.setText("Нажали правую кнопку мыши")

                ''' Преобразование размера изображения '''
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))

            # здесь отфильтруйте событие выпуска мыши и перепишите его поведение
            if event.type() == QEvent.MouseButtonRelease:
                self.labelState.setText("Отпустили кнопку мыши")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))

        return QDialog.eventFilter(self, obj, event)


if __name__ == '__main__':
    app    = QApplication(sys.argv)
    dialog = EventFilter()
    dialog.show()
    sys.exit(app.exec_())