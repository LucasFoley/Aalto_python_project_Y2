import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.pushButton1 = QPushButton("Play", self.centralwidget)

        layout = QVBoxLayout(self.centralwidget)
        layout.addWidget(self.pushButton1)


stylesheet = """
    MainWindow {
        background-image: url("C:/Users/lukif/OneDrive/Documents/Aalto/Programing Y2/Project/Images and backgrounds/castle_1.png")
        no-repeat center center fixed;
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)  # <---
    window = MainWindow()
    window.resize(700, 700)
    window.show()
    sys.exit(app.exec_())
