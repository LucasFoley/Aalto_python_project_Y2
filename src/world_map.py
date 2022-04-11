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


def get_room_by_number(number):
    if number == 1:
        return room1()
    if number == 2:
        return room2()


def room1():
    enemy1 = EnemyMinion()
    enemy2 = EnemyMinion()
    enemy3 = EnemyMinion()
    return enemy1, enemy2, enemy3


def room2():
    enemy1 = EnemyMinion()
    enemy2 = EnemyBrute()
    enemy3 = EnemyMinion()
    return enemy1, enemy2, enemy3

