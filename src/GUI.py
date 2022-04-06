import sys
from Basic_unit import *
from RUN_ME import main
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


#   GUI creates a usable Start and Main window where the user can play the game
#   There are a few different buttons and boxes that allows the user to input combat choices and receive information
#   about the game state and the unit stats


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.label = None
        self.button = None
        self.button1 = None
        self.button2 = None
        self.text_box = None
        self.stats_window = None
        self.show_start_image()
        self.play_button()

    #   Starting window of program below

    def show_start_image(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("start_background.png"))

    def play_button(self):
        self.button = QPushButton("PLAY", self)
        self.button.setGeometry(275, 700, 250, 60)
        self.button.setFont(QFont("DejaVu Sans", 20))
        self.button.clicked.connect(self.play_button_clicked)
        self.layout.addWidget(self.button)

    def play_button_clicked(self):
        self.button.deleteLater()
        self.show_main_image()
        self.add_main_buttons()

    #   Main window of program below

    def show_main_image(self):
        self.label.setPixmap(QPixmap("background.png"))

    def add_main_buttons(self):
        self.button1 = QPushButton("ATTACK", self)
        self.button1.setFont(QFont("DejaVu Sans", 25))
        self.button1.setGeometry(25, 545, 350, 100)

        self.button2 = QPushButton("STATS", self)
        self.button2.setFont(QFont("DejaVu Sans", 25))
        self.button2.setGeometry(425, 545, 350, 100)
        self.button2.clicked.connect(self.stats_button_clicked)

        self.text_box = QTextEdit("text here", self)
        self.text_box.setReadOnly(True)
        self.text_box.setGeometry(25, 660, 750, 120)
        self.text_box.setFont(QFont("DejaVu Sans", 12))

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.text_box)
        self.button1.show()
        self.button2.show()
        self.text_box.show()

    def stats_button_clicked(self):
        self.stats_window = QWidget()
        self.stats_window.setWindowTitle("Stats")
        self.stats_window.resize(400, 800)
        self.stats_window.move(1360, 72)
        self.stats_window.show()

        print(main.ally_position)

        """for unit in main.ally_positions:
            hp = unit.get_hp()
            atk = unit.get_atk()
            armor = unit.get_armor()
            print(hp, atk, armor)"""


def run_gui():
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())
