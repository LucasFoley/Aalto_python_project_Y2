from RUN_ME import *
from basic_unit import BasicUnit, Wizard, Warrior, Shaman, EnemyMinion, EnemyBrute, EnemyBoss
from world_map import *
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
        self.shaman = Shaman()
        self.enemy_list = []

        self.room_counter = 1

        self.layout = QGridLayout()
        self.label = None
        self.play = None

        self.wizard_button = None
        self.warrior_button = None
        self.shaman_button = None

        self.attack_button = None
        self.stats_button = None
        self.stats_window = None
        self.text_box = None

        self.exit_button = None

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

        self.shaman_button = QPushButton("Shaman", self)
        self.shaman_button.setFont(QFont("DejaVu Sans", 20))
        self.shaman_button.setGeometry(540, 600, 200, 100)
        self.shaman_button.clicked.connect(self.shaman_clicked)

        self.layout.addWidget(self.wizard_button)
        self.layout.addWidget(self.warrior_button)
        self.layout.addWidget(self.shaman_button)
        self.wizard_button.show()
        self.warrior_button.show()
        self.shaman_button.show()

    def wizard_clicked(self):
        self.main_character = self.wizard
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.shaman_button.deleteLater()
        self.get_room()
        self.show_main_image()
        self.add_main_buttons()

    def warrior_clicked(self):
        self.main_character = self.warrior
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.shaman_button.deleteLater()
        self.get_room()
        self.show_main_image()
        self.add_main_buttons()

    def shaman_clicked(self):
        self.main_character = self.shaman
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.shaman_button.deleteLater()
        self.get_room()
        self.show_main_image()
        self.add_main_buttons()

    #   Main window of program below

    def get_room(self):
        self.enemy_list.clear()
        enemies = get_room_by_number(self.room_counter)
        for item in enemies:
            self.enemy_list.append(item)

    def show_main_image(self):
        self.label.setPixmap(QPixmap("background_2.png"))

    def add_main_buttons(self):
        self.attack_button = QPushButton("ATTACK", self)
        self.attack_button.setFont(QFont("DejaVu Sans", 25))
        self.attack_button.setGeometry(25, 545, 350, 100)
        self.attack_button.clicked.connect(self.attack_button_clicked)

        self.stats_button = QPushButton("STATS", self)
        self.stats_button.setFont(QFont("DejaVu Sans", 25))
        self.stats_button.setGeometry(425, 545, 350, 100)
        self.stats_button.clicked.connect(self.stats_button_clicked)

        self.text_box = QTextEdit("text here", self)
        self.text_box.setReadOnly(True)
        self.text_box.setGeometry(25, 660, 750, 120)
        self.text_box.setFont(QFont("DejaVu Sans", 12))

        self.layout.addWidget(self.attack_button)
        self.layout.addWidget(self.stats_button)
        self.layout.addWidget(self.text_box)
        self.attack_button.show()
        self.stats_button.show()
        self.text_box.show()

    def attack_button_clicked(self):
        if self.main_character.is_alive():
            print("enemy hp")
            for enemy in self.enemy_list:
                enemy.combat(self.main_character)
                print(enemy.get_hp())
            print("ally hp")
            if self.enemy_list.enemies_are_alive():
                for enemy in self.enemy_list:
                    self.main_character.combat(enemy)
                    print(self.main_character.get_hp())
        else:
            self.end_game()

    def stats_button_clicked(self):
        self.stats_window = QTableWidget(3, 2)
        self.stats_window.setWindowTitle("Stats")
        self.stats_window.resize(271, 800)
        self.stats_window.move(1360, 72)
        self.stats_window.show()

    #   Game ending part below

    def end_game(self):
        self.attack_button.deleteLater()
        self.stats_button.deleteLater()
        self.text_box.deleteLater()
        self.show_end_image()
        self.add_exit_button()

    def show_end_image(self):
        self.label.setPixmap(QPixmap("character_select.png"))

    def add_exit_button(self):
        self.exit_button = QPushButton("EXIT GAME", self)
        self.exit_button.setFont(QFont("DejaVu Sans", 25))
        self.exit_button.setGeometry(200, 545, 400, 100)
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.layout.addWidget(self.exit_button)
        self.exit_button.show()

    def exit_button_clicked(self):
        QApplication.quit()


def run_gui():
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Dark Dungeon")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())
