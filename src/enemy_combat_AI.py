from basic_unit import *


def enemy_combat(enemy_list, main_character):
    for enemy in enemy_list:
        if enemy.name == "EnemyMinion":
            enemy_minion(enemy, main_character)
        elif enemy.name == "EnemySlime":
            enemy_slime(enemy, main_character)
        elif enemy.name == "EnemyWarlock":
            enemy_warlock(enemy, main_character)
        elif enemy.name == "EnemyBrute":
            enemy_brute(enemy, main_character)
        elif enemy.name == "EnemyBoss":
            enemy_boss(enemy, main_character)


def enemy_minion(minion, main_character):
    if check_status(minion, main_character):
        main_character.combat(minion)


def enemy_slime(slime, main_character):
    if check_status(slime, main_character):
        main_character.hp -= slime.hp
        slime.hp = 0


def enemy_warlock(warlock, main_character):
    if check_status(warlock, main_character):
        life_steal = (15 - main_character.armor)
        main_character.hp -= life_steal
        warlock.hp += life_steal


def enemy_brute(brute, main_character):
    if check_status(brute, main_character):
        main_character.combat(brute)


def enemy_boss(boss, main_character):
    if main_character.armor > 0:
        boss.use_special
    else:
        main_character.combat(boss)


def check_status(enemy, main_character):
    if enemy.status:
        for status in enemy.status:
            if status == "Stun, ":
                return 0
            elif status == "Freeze, ":
                return 0
            elif status == "Burn, ":
                enemy.hp -= 20
                return 1
            elif status == "Absorb, ":
                main_character.hp += 10
                enemy.hp -= 20
                return 1
    else:
        return 1



