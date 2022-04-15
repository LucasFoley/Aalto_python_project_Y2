from basic_unit import *

wizard = Wizard()
shaman = Shaman()
warrior = Warrior()

minion = EnemyMinion()
minion2 = EnemyMinion()
brute = EnemyBrute()

# test basic combat and hp
while wizard.is_alive() and minion.is_alive():
    wizard.combat(minion)
    if minion.hp > 0:
        print("enemy hp:", minion.hp)
        minion.combat(wizard)
        print("wizard hp:", wizard.hp)
print("enemy is dead")

# test special

while not brute.status:
    shaman.use_special(brute)
    print(brute.get_status())


while not minion.status:
    wizard.use_special(minion)
    print(minion.get_status())




