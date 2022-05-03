from basic_unit import *


def get_enemies_by_room_number(number):
    if number == 0:
        return room0()
    elif number == 1:
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


def room0():
    enemy1 = EnemyMinion()
    return enemy1


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


def start_text():
    text = "By some great misfortune you have stumbled into this old and long forgotten place. " \
           "You hear a quite but disturbing sound from the room up ahead.\n\n" \
           "PRESS  Continue to proceed and find out what is making that horrid sound."
    return text


def room2_text():
    text = "You have made it past your first trial! You can hear evil laughs and see a weird green shining " \
           "light up ahead. A life stealing warlock awaits for you in the next room.\n" \
            "PRESS  Continue to proceed to the next room."
    return text


def room3_text():
    text = "You have made it past your second trial! There are more enemies up ahead and they look stronger.\n\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def room4_text():
    text = "You have made it past your third trial! There seems to some sort of slime on the floor. As you approach " \
           "the next room you see slimes that look like they are about to explode!\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def room5_text():
    text = "You have made it past your forth trial! You are almost there traveller. The next fight isn't going to be " \
           "easy as it is the Final Boss!\n\n" \
           "PRESS  Continue to proceed to the next room."
    return text


def end_text():
    text = "You have made it past your final trial!" \
           "PRESS  Continue to proceed to the end credits."
    return text

