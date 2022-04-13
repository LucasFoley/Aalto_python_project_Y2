from basic_unit import *
'''self.enemy_minion1 = EnemyMinion()
self.enemy_minion2 = EnemyMinion()
self.enemy_minion3 = EnemyMinion()
self.enemy_brute = EnemyBrute()
self.enemy_boss = EnemyBoss()

self.enemy_list.append(self.enemy_minion1)
self.enemy_list.append(self.enemy_minion2)
self.enemy_list.append(self.enemy_minion3)
'''


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
    enemy1 = EnemyBrute()
    enemy2 = EnemyBrute()
    enemy3 = EnemyBrute()
    return enemy1, enemy2, enemy3


def end_room():
    return None


def start_text():
    text = "By some great misfortune you have stumbled into this old and long forgotten place. " \
           "You hear a quite but but disturbing sound from the room up ahead.\n\n" \
           "PRESS  Continue to proceed and find out what is making that horrid sound."
    return text


def room2_text():
    text = "You have made it past your first trial!"
    return text


def room3_text():
    text = "You have made it past your second trial!"
    return text


def room4_text():
    text = "You have made it past your third trial!"
    return text


def end_text():
    text = "You have made it past your final trial!"
    return text

