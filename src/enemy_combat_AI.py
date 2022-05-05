""" This file handles all enemy combat and strategies

    It takes in a list of enemies for each room and separates them into the correct corresponding
    combat strategy based on the name of the enemy. Then it performs the combat functions and
    applies the damage and/or status effects to the players character"""


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
        main_character.hp -= 5
        if main_character.atk > 5:
            main_character.atk -= 2
            main_character.atk = 5


def enemy_warlock(warlock, main_character):
    if check_status(warlock, main_character):
        main_character.hp -= 10
        warlock.hp += 10


def enemy_brute(brute, main_character):
    if check_status(brute, main_character):
        main_character.combat(brute)


def enemy_boss(boss, main_character):
    check_status(boss, main_character)
    boss.use_special(main_character)
    main_character.combat(boss)


""" This part checks what statuses have been applied to the enemy so it can decide what should happen or
    shouldn't happen in the cases where the enemy is stunned or frozen"""


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

