from RUN_ME import *
from basic_unit import BasicUnit, Wizard, Warrior, Healer, EnemyMinion, EnemyBrute, EnemyBoss
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


#   GUI creates a usable Start and Main window where the user can play the game
#   There are a few different buttons and boxes that allows the user to input combat choices and receive information
#   about the game state and the unit stats


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.main_character = None
        self.wizard = Wizard()
        self.warrior = Warrior()
        self.healer = Healer()
        self.enemy_minion1 = EnemyMinion()
        self.enemy_minion2 = EnemyMinion()
        self.enemy_minion3 = EnemyMinion()
        self.enemy_brute = EnemyBrute()
        self.enemy_boss = EnemyBoss()
        self.enemy_list = []
        self.enemy_list.append(self.enemy_minion1)
        self.enemy_list.append(self.enemy_minion2)
        self.enemy_list.append(self.enemy_minion3)

        self.layout = QGridLayout()
        self.label = None
        self.play = None

        self.wizard_button = None
        self.warrior_button = None
        self.healer_button = None

        self.attack = None
        self.stats = None
        self.stats_window = None
        self.text_box = None

        self.show_start_image()
        self.play_button()

    #   Starting window of program below

    def show_start_image(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("start_background.png"))

    def play_button(self):
        self.play = QPushButton("PLAY", self)
        self.play.setGeometry(275, 700, 250, 60)
        self.play.setFont(QFont("DejaVu Sans", 20))
        self.play.clicked.connect(self.play_button_clicked)
        self.layout.addWidget(self.play)

    def play_button_clicked(self):
        self.play.deleteLater()
        self.show_character_selection_image()
        self.add_choose_buttons()

    #   Choose character window

    def show_character_selection_image(self):
        self.label.setPixmap(QPixmap("character_select.png"))

    def add_choose_buttons(self):
        self.wizard_button = QPushButton("Wizard", self)
        self.wizard_button.setFont(QFont("DejaVu Sans", 20))
        self.wizard_button.setGeometry(60, 600, 200, 100)
        self.wizard_button.clicked.connect(self.wizard_clicked)

        self.warrior_button = QPushButton("Warrior", self)
        self.warrior_button.setFont(QFont("DejaVu Sans", 20))
        self.warrior_button.setGeometry(300, 600, 200, 100)
        self.warrior_button.clicked.connect(self.warrior_clicked)

        self.healer_button = QPushButton("Healer", self)
        self.healer_button.setFont(QFont("DejaVu Sans", 20))
        self.healer_button.setGeometry(540, 600, 200, 100)
        self.healer_button.clicked.connect(self.healer_clicked)

        self.layout.addWidget(self.wizard_button)
        self.layout.addWidget(self.warrior_button)
        self.layout.addWidget(self.healer_button)
        self.wizard_button.show()
        self.warrior_button.show()
        self.healer_button.show()

    def wizard_clicked(self):
        self.main_character = self.wizard
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.healer_button.deleteLater()
        self.show_main_image()
        self.add_main_buttons()

    def warrior_clicked(self):
        self.main_character = self.warrior
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.healer_button.deleteLater()
        self.show_main_image()
        self.add_main_buttons()

    def healer_clicked(self):
        self.main_character = self.healer
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.healer_button.deleteLater()
        self.show_main_image()
        self.add_main_buttons()

    #   Main window of program below

    def show_main_image(self):
        self.label.setPixmap(QPixmap("background_2.png"))

    def add_main_buttons(self):
        self.attack = QPushButton("ATTACK", self)
        self.attack.setFont(QFont("DejaVu Sans", 25))
        self.attack.setGeometry(25, 545, 350, 100)

        self.stats = QPushButton("STATS", self)
        self.stats.setFont(QFont("DejaVu Sans", 25))
        self.stats.setGeometry(425, 545, 350, 100)
        self.stats.clicked.connect(self.stats_button_clicked)

        self.text_box = QTextEdit("text here", self)
        self.text_box.setReadOnly(True)
        self.text_box.setGeometry(25, 660, 750, 120)
        self.text_box.setFont(QFont("DejaVu Sans", 12))

        self.layout.addWidget(self.attack)
        self.layout.addWidget(self.stats)
        self.layout.addWidget(self.text_box)
        self.attack.show()
        self.stats.show()
        self.text_box.show()

    def attack_button_clicked(self):
        if self.main_character.is_alive():
            for enemy in self.enemy_list:
                self.main_character.combat(enemy)
                print(enemy.get_hp())
            for enemy in self.enemy_list:
                enemy.combat(self.main_character)
                print(self.main_character.get_hp())

    def stats_button_clicked(self):
        self.stats_window = QTableWidget(3, 2)
        self.stats_window.setWindowTitle("Stats")
        self.stats_window.resize(271, 800)
        self.stats_window.move(1360, 72)
        self.stats_window.show()


def run_gui():
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())
