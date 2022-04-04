import sys
from PyQt5.QtWidgets import *

stylesheet = """
        MainWindow {
            background-image: url("C:/Users/lukif/OneDrive/Documents/Aalto/Programing Y2/Project/Images and backgrounds/castle_1.png")
            no-repeat center center fixed;
        }
    """


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

    def push_play_button(self):
        button = QPushButton("Play", self)
        button.setGeometry(225, 600, 250, 60)
        layout = QVBoxLayout()
        layout.addWidget(button)

class ImageWidget(QWidget):

    def __init__(self):
        super().show_image()

    #def show_image(self):



def main():
    app = QApplication(sys.argv)
    main_widget = QWidget()
    main_widget.setWindowTitle("Dark Dungeon")
    main_widget.push_play_button()
    window = MainWindow()
    window.resize(700, 700)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
