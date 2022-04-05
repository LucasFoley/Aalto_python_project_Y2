import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

stylesheet = """
        MainWindow {
            background-image: url("C:/Users/lukif/OneDrive/Documents/Aalto/Programing Y2/Project/Images and backgrounds/start_background.png")
            no-repeat center center fixed;
        }
    """


class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.show_image()
        self.push_play_button()

    def push_play_button(self):
        button = QPushButton("Play", self)
        button.setGeometry(275, 700, 250, 60)
        button.clicked.connect(self.play_button_clicked)
        layout = QVBoxLayout()
        layout.addWidget(button)

    def play_button_clicked(self):
        print("click")

    def show_image(self):
        image = QPixmap("start_background.png")
        label = QLabel(self)
        label.setPixmap(image)

class MainWindow(QWidget)


def main():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
