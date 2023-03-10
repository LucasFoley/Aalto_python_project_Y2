from enemy_combat_AI import enemy_combat
from world_map import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

""" This is the main file for the entire game. Since the game is heavily dependent on graphical input all most 
    everything is handled in this file.    
    
    GUI creates a usable Start and Main window where the user can play the game. There are a few different buttons 
    and boxes that allows the user to input combat choices and receive information regarding the game state and the 
    units conditions and stats
    
    The first part of the program creates the main window class and widget from which the user can interact with the 
    game. All initial characters, buttons, and variables are created so that they can be used later on in the program"""


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.main_character = None
        self.wizard = Wizard()
        self.warrior = Warrior()
        self.shaman = Shaman()
        self.enemy_list = []

        self.room_number = 0

        self.layout = QGridLayout()
        self.label = None
        self.play = None

        self.wizard_button = None
        self.warrior_button = None
        self.shaman_button = None

        self.continue_button = None

        self.attack_button = None
        self.use_special_button = None
        self.stats_window = None
        self.text_box = None

        self.exit_button = None

        self.show_start_image()
        self.play_button()

    """ This part of the file handles the starting window of program. 
        
        It creates a play button and adds the background image. """

    def show_start_image(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("game_img/start_background.png"))

    def play_button(self):
        self.play = QPushButton("PLAY", self)
        self.play.setFont(QFont("DejaVu Sans", 20))
        self.play.setGeometry(275, 700, 250, 60)
        self.play.clicked.connect(self.play_button_clicked)
        self.layout.addWidget(self.play)

    def play_button_clicked(self):
        self.play.deleteLater()
        self.show_character_selection_image()
        self.add_choose_buttons()

    """ This part of the file handles the character selection.
        
        It changes the background and add a button for each of the playable characters."""

    def show_character_selection_image(self):
        self.label.setPixmap(QPixmap("game_img/character_select.png"))

    def add_choose_buttons(self):
        self.wizard_button = QPushButton("Wizard", self)
        self.wizard_button.setFont(QFont("DejaVu Sans", 20))
        self.wizard_button.setGeometry(60, 670, 200, 100)
        self.wizard_button.clicked.connect(self.wizard_clicked)

        self.warrior_button = QPushButton("Warrior", self)
        self.warrior_button.setFont(QFont("DejaVu Sans", 20))
        self.warrior_button.setGeometry(300, 670, 200, 100)
        self.warrior_button.clicked.connect(self.warrior_clicked)

        self.shaman_button = QPushButton("Shaman", self)
        self.shaman_button.setFont(QFont("DejaVu Sans", 20))
        self.shaman_button.setGeometry(540, 670, 200, 100)
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
        self.move_to_next_room()

    def warrior_clicked(self):
        self.main_character = self.warrior
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.shaman_button.deleteLater()
        self.move_to_next_room()

    def shaman_clicked(self):
        self.main_character = self.shaman
        self.wizard_button.deleteLater()
        self.warrior_button.deleteLater()
        self.shaman_button.deleteLater()
        self.move_to_next_room()

    """ Here is now the main part of the program.
        
        To put it simply the program switches between a combat room and a story/narrator room. There is room counter
        that will keep track of which room the player is in and load all the appropriate buttons, dialogs, and
        enemies.
        
        Here below are the two function that handle the switching of rooms. They will get the next room and enemies 
        until there are no more, in which case they will send the player to the end screen."""

    def get_room(self):
        self.enemy_list.clear()
        enemies = get_enemies_by_room_number(self.room_number)
        if enemies is None:
            self.end_game()
        elif type(enemies) is tuple:
            for item in enemies:
                self.enemy_list.append(item)
        else:
            self.enemy_list.append(enemies)

    def move_to_next_room(self):
        self.show_continue_image()
        self.add_continue_button()
        self.add_text_box()
        story_text = get_text_by_room_number(self.room_number)
        self.text_box.append(story_text)
        self.room_number += 1

    """ This part of the main part changes to the inbetween fights window"""

    def show_continue_image(self):
        self.label.setPixmap(QPixmap("game_img/base_background.png"))

    def add_continue_button(self):
        self.continue_button = QPushButton("CONTINUE", self)
        self.continue_button.setFont(QFont("DejaVu Sans", 25))
        self.continue_button.setGeometry(25, 540, 750, 100)
        self.continue_button.clicked.connect(self.continue_button_clicked)
        self.layout.addWidget(self.continue_button)
        self.continue_button.show()

    def continue_button_clicked(self):
        self.continue_button.deleteLater()
        self.get_room()
        if self.enemy_list:
            self.show_combat_image()
            self.add_combat_buttons()
            self.add_text_box()
        else:
            self.end_game()

    """ This part of the main part handles the combat window and the combat. The combat calculations and specifics are 
        handled in the basic_unit.py file and enemy_combat_AI.py but are ordered and combined into a working combat 
        system here in the main part.  
        
        First the combat related buttons, dialog box, and images are shown"""

    def show_combat_image(self):
        image = get_img_by_room(self.room_number)
        self.label.setPixmap(QPixmap(image))

    def add_text_box(self):
        self.text_box = QTextEdit("", self)
        self.text_box.setFont(QFont("DejaVu Sans", 12))
        self.text_box.setGeometry(25, 660, 750, 120)
        self.text_box.setReadOnly(True)

        self.layout.addWidget(self.text_box)
        self.text_box.show()

    def add_combat_buttons(self):
        self.attack_button = QPushButton("ATTACK", self)
        self.attack_button.setFont(QFont("DejaVu Sans", 25))
        self.attack_button.setGeometry(25, 540, 360, 100)
        self.attack_button.clicked.connect(self.attack_button_clicked)

        self.use_special_button = QPushButton("USE SPECIAL", self)
        self.use_special_button.setFont(QFont("DejaVu Sans", 25))
        self.use_special_button.setGeometry(415, 540, 360, 100)
        self.use_special_button.clicked.connect(self.use_special_button_clicked)

        self.layout.addWidget(self.attack_button)
        self.layout.addWidget(self.use_special_button)
        self.attack_button.show()
        self.use_special_button.show()

    """ This part handles the combat if the normal direct attack button is clicked.
    
        The player always starts attacking first and attacks every enemy in the enemy list. Relevant combat information
        is added to the dialog box each turn. The program checks that the player and the enemies are alive before each
        turn. If the enemies are dead it will move on to the next room and if the player dies it will take the player
        to the end window."""

    def attack_button_clicked(self):
        if self.main_character.is_alive():
            self.text_box.clear()
            for enemy in self.enemy_list:
                enemy.combat(self.main_character)
                if enemy.is_alive():
                    self.text_box.append("Enemy HP: " + str(enemy.get_hp()))
                else:
                    self.text_box.append("Enemy is DEAD")
            self.enemies_are_alive()
            if not self.enemy_list:
                self.attack_button.deleteLater()
                self.use_special_button.deleteLater()
                self.text_box.clear()
                self.move_to_next_room()
            else:
                enemy_combat(self.enemy_list, self.main_character)
                if self.main_character.is_alive():
                    self.text_box.append("Player HP: " + str(self.main_character.get_hp()))
                else:
                    self.text_box.append("You DIED")
        else:
            self.end_game()

    """ The use special attack section is similar to the attack section of the program. The main difference is that it
        must handle each of the separate playable characters differently and output only relevant combat information
        regarding their special ability. It functions almost identically to the attack section but just sorts out
        which information to output based on the main character that the player has selected."""

    def use_special_button_clicked(self):
        if self.main_character.is_alive():
            self.text_box.clear()
            for enemy in self.enemy_list:
                self.main_character.use_special(enemy)
                if self.main_character.name == "Warrior":
                    self.text_box.append("Player attack: " + str(self.main_character.atk)
                                         + "    Enemy HP:" + str(enemy.get_hp()))
                elif enemy.is_alive():
                    self.text_box.append(str(enemy.get_status()) + " applied to enemy.   Enemy HP:"
                                         + str(enemy.get_hp()))
                else:
                    self.text_box.append("Enemy is DEAD")
            self.enemies_are_alive()
            if not self.enemy_list:
                self.attack_button.deleteLater()
                self.use_special_button.deleteLater()
                self.text_box.clear()
                self.move_to_next_room()
            else:
                enemy_combat(self.enemy_list, self.main_character)
                if self.main_character.is_alive():
                    for enemy in self.enemy_list:
                        if self.main_character.name == "Shaman":
                            if "Freeze, " in enemy.status:
                                if "Burn, " in enemy.status:
                                    if "Absorb, " in enemy.status:
                                        self.text_box.append("Maximum amount of statuses applied")
                        elif self.main_character.name == "Wizard":
                            if "Stun, " in enemy.status:
                                self.text_box.append("Maximum amount of statuses applied")
                    if self.main_character.name == "Warrior":
                        if self.main_character.atk == 40:
                            self.text_box.append("Player has reached the max attack")
                    self.text_box.append("Player HP: " + str(self.main_character.get_hp()))
                else:
                    self.text_box.append("You DIED")
        else:
            self.end_game()

    def enemies_are_alive(self):
        for enemy in self.enemy_list:
            if not enemy.is_alive():
                self.enemy_list.remove(enemy)

    """ Lastly the game ending section which the player will be brought to depending on if they died or if they managed
        to beat the game.
        
        The try, except is used to allow both the winning route and the dying route to take the player to the end 
        window."""

    def end_game(self):
        try:
            self.attack_button.deleteLater()
            self.use_special_button.deleteLater()
            self.text_box.append(("\n"
                                  "Dark Dungeon\n"
                                  "Version 1.0\n"
                                  "\n"
                                  "Made by Lucas Foley"))
            self.show_end_image()
            self.add_exit_button()
        except RuntimeError:
            self.continue_button.deleteLater()
            self.show_end_image()
            self.text_box.clear()
            self.text_box.append(("\n"
                                  "Dark Dungeon\n"
                                  "Version 1.0\n"
                                  "\n"
                                  "Made by Lucas Foley"))
            self.add_exit_button()

    def show_end_image(self):
        self.label.setPixmap(QPixmap("game_img/end_background.png"))

    def add_exit_button(self):
        self.exit_button = QPushButton("EXIT GAME", self)
        self.exit_button.setFont(QFont("DejaVu Sans", 25))
        self.exit_button.setGeometry(200, 550, 400, 100)
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.layout.addWidget(self.exit_button)
        self.exit_button.show()

    def exit_button_clicked(self):
        QApplication.quit()


def run_gui():
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Dark Dungeon")
    window.setFixedSize(800, 800)
    window.show()
    sys.exit(app.exec_())
