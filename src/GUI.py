import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

stylesheet = """
        MainWindow {
            background-image: url("C:/Users/lukif/OneDrive/Documents/Aalto/Programing Y2/Project/Images and backgrounds/castle_1.png")
            no-repeat center center fixed;
        }
    """


class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.push_play_button()

    def push_play_button(self):
        button = QPushButton("Play", self)
        button.setGeometry(225, 600, 250, 60)
        layout = QVBoxLayout()
        layout.addWidget(button)


class ImageWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.show_image()

    def show_image(self):
        image = QPixmap("castle_1.png")
        label = QLabel(self)
        label.setPixmap(image)


class StartLayout(QWidget):

    def __init__(self):
        super().__init__()

    def grid_layout(self):
        grid = QGr


def main():
    app = QApplication(sys.argv)
    window = ImageWidget()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
