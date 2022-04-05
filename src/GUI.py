import sys
from Basic_unit import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


started = False


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
        main_window = MainWindow()
        started = True


    def show_image(self):
        image = QPixmap("start_background.png")
        label = QLabel(self)
        label.setPixmap(image)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.show_image()
        self.add_buttons()

    def show_image(self):
        image = QPixmap("background.png")
        label = QLabel(self)
        label.setPixmap(image)

    def add_buttons(self):
        button1 = QPushButton("ATTACK", self)
        button1.setFont(QFont("DejaVu Sans", 25))
        button1.setGeometry(25, 545, 350, 100)
        button2 = QPushButton("STATS", self)
        button2.setFont(QFont("DejaVu Sans", 25))
        button2.setGeometry(425, 545, 350, 100)
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        text_box = QTextEdit("text here", self)
        text_box.setGeometry(25, 660, 750, 120)
        text_box.setFont(QFont("DejaVu Sans", 12))
        layout.addWidget(text_box)






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
