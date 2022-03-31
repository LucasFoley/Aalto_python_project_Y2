import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Dark Dungeon")
window.setMinimumSize(1000, 800)
window.setStyleSheet("""
        QWidget {
            border: 20px solid black;
            border-radius: 10px;
            background-color: rgb(255, 255, 255);
            }
        """)

window.show()
sys.exit(app.exec_())

if __name__ == '__main__':
    main()

