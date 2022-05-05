import random

""" This file handles all basic units and interactions between their resources
    Combat and special abilities are handled and calculated on the playable characters side
    Each unit is a subclass of the BasicUnit class and they have adjusted and individual stats and abilities"""


class BasicUnit:

    def __init__(self):
        self.name = "EnemyMinion"
        self.hp = 50
        self.atk = 10
        self.armor = 3
        self.status = []

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_armor(self):
        return self.armor

    def get_status(self):
        status_str = ""
        for status in self.status:
            string = str(status)
            status_str += string
        if status_str == "":
            return "No status"
        else:
            return status_str

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def combat(self, attacker):
        if self.armor < attacker.atk:
            self.hp -= (attacker.atk - self.armor)
        else:
            self.hp -= 1
        return self.is_alive()

    def burn(self):
        number = random.randint(1, 100)
        if number <= 50:
            return True
        else:
            return False

    def freeze(self):
        number = random.randint(1, 100)
        if number <= 50:
            return True
        else:
            return False

    def absorb(self):
        number = random.randint(1, 100)
        if number <= 50:
            return True
        else:
            return False

    def giga_absorb(self):
        number = random.randint(1, 100)
        if number <= 15:
            return True
        else:
            return False

    def stun(self):
        number = random.randint(1, 100)
        if number <= 50:
            return True
        else:
            return False

    def stun_death(self):
        number = random.randint(1, 100)
        if number <= 20:
            return True
        else:
            return False


""" Enemy Units are handled in this part of the program
    Only the bosses special ability is handled in this file inorder to keep the enemy_combat_AI file cleaner"""


class EnemyMinion(BasicUnit):

    def __init__(self):
        super().__init__()


class EnemySlime(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "EnemySlime"
        self.hp = 25
        self.atk = 15
        self.armor = 10


class EnemyWarlock(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "EnemyWarlock"
        self.hp = 100
        self.atk = 15
        self.armor = 10


class EnemyBrute(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "EnemyBrute"
        self.hp = 80
        self.atk = 15
        self.armor = 6


class EnemyBoss(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "EnemyBoss"
        self.hp = 200
        self.atk = 20
        self.armor = 10

    def use_special(self, target):
        armor_shred = 2
        if target.armor > 0:
            if target.armor == 1:
                target.armor = 2
            target.armor -= armor_shred
            self.hp += 10
        else:
            self.hp += 10


""" All playable units and their abilities are in this part of the file"""


class Wizard(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "Wizard"
        self.hp = 150
        self.atk = 25
        self.armor = 5

    def use_special(self, target):
        stun = self.stun()
        stun_death = self.stun_death()
        if stun:
            if "Stun, " not in target.status:
                target.hp -= 40
                target.status.append("Stun, ")
            else:
                if stun_death:
                    target.hp -= 999
                else:
                    target.hp -= 20


class Shaman(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "Shaman"
        self.hp = 150
        self.atk = 15
        self.armor = 5

    def use_special(self, target):
        chance = random.randint(1, 100)
        if chance < 33:
            burn = self.burn()
            if burn:
                if "Burn, " not in target.status:
                    target.hp -= 20
                    target.status.append("Burn, ")
        elif 33 <= chance < 66:
            freeze = self.freeze()
            if freeze:
                if "Freeze, " not in target.status:
                    target.status.append("Freeze, ")
        else:
            absorb = self.absorb()
            giga_absorb = self.giga_absorb()
            if absorb:
                if "Absorb, " not in target.status:
                    if giga_absorb:
                        self.hp += 40
                        target.hp -= 40
                    target.hp -= 20
                    self.hp += 20
                    target.status.append("Absorb, ")


class Warrior(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.hp = 150
        self.atk = 20
        self.armor = 10

    def use_special(self, target):
        if self.atk < 40:
            self.atk += 3
            if self.atk > 40:
                self.atk = 40
            self.armor += 2
        else:
            self.atk = 40
