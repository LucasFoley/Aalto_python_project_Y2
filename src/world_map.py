from basic_unit import *

""" This file stores all information for each room in the game
    
    The First part will create and return the enemies for the specific room"""


def get_enemies_by_room_number(number):
    if number == 1:
        return room1()
    elif number == 2:
        return room2()
    elif number == 3:
        return room3()
    elif number == 4:
        return room4()
    elif number == 5:
        return room5()
    else:
        return end_room()


def room1():
    enemy1 = EnemyMinion()
    enemy2 = EnemyMinion()
    enemy3 = EnemyMinion()
    return enemy1, enemy2, enemy3


def room2():
    enemy1 = EnemyWarlock()
    return enemy1


def room3():
    enemy1 = EnemyMinion()
    enemy2 = EnemyBrute()
    enemy3 = EnemyMinion()
    return enemy1, enemy2, enemy3


def room4():
    enemy1 = EnemySlime()
    enemy2 = EnemyMinion()
    enemy3 = EnemySlime()
    return enemy1, enemy2, enemy3


def room5():
    enemy1 = EnemyBoss()
    return enemy1


def end_room():
    return None


""" The second part will give the dialog text inbetween each room"""


def get_text_by_room_number(number):
    if number == 0:
        return start_text()
    elif number == 1:
        return room2_text()
    elif number == 2:
        return room3_text()
    elif number == 3:
        return room4_text()
    elif number == 4:
        return room5_text()
    else:
        return end_text()


def start_text():
    text = "By some great misfortune you have stumbled into this old and long forgotten place. " \
           "You hear a quite but disturbing sound from the room up ahead.\n\n" \
           "PRESS  Continue to proceed and find out what is making that horrible sound."
    return text


def room2_text():
    text = "You have made it past your first trial! You can hear evil laughs and see a weird green shining " \
           "light up ahead. A life stealing warlock awaits you in the next room.\n\n" \
            "PRESS  Continue to proceed to the next room."
    return text


def room3_text():
    text = "You have made it past your second trial! There are more enemies up ahead and it looks like one of them is " \
           "stronger than the rest of them.\n\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def room4_text():
    text = "You have made it past your third trial! As you approach the next room you notice some creatures made " \
           "out of slime. Beware they reduce your armor with each attack.\n\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def room5_text():
    text = "You have made it past your forth trial! You are almost there traveller but the next fight isn't going to " \
           "be easy as it is the Final Boss and it is immune to stuns and freezes!\n\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def end_text():
    text = "Congratulations, you have made it past your final trial and managed to escape this dungeon!\n\n\n" \
           "PRESS  Continue to proceed to the end credits."
    return text


""" The third part gives the GUI the correct background battle image as a string for each room"""


def get_img_by_room(number):
    if number == 1:
        return room1_img()
    elif number == 2:
        return room2_img()
    elif number == 3:
        return room3_img()
    elif number == 4:
        return room4_img()
    elif number == 5:
        return room5_img()


def room1_img():
    return "game_img/minion_battle.png"


def room2_img():
    return "game_img/warlock_battle.png"


def room3_img():
    return "game_img/minion_brute_minion_battle.png"


def room4_img():
    return "game_img/slime_minion_slime_battle.png"


def room5_img():
    return "game_img/boss_battle.png"


