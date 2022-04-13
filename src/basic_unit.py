import random


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
        return self.status

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

    def special_ability(self, target):
        try:
            self.use_special(target)
        except:
            print("Unit has no special ability")

    def print_combat_text(self):
        pass

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

    def stun(self):
        number = random.randint(1, 100)
        if number <= 30:
            return True
        else:
            return False


# Enemy Units


class EnemyMinion(BasicUnit):

    def __init__(self):
        super().__init__()


class EnemyWarlock(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "EnemyWarlock"
        self.hp = 100
        self.atk = 15
        self.armor = 10

    def use_special(self, target):
        target.hp -= 15
        self.hp += 5


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


# Ally Units


class Wizard(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "Wizard"
        self.hp = 150
        self.atk = 25
        self.armor = 5

    def use_special(self, target):
        stun = self.stun()
        if stun:
            target.hp -= 40
            target.status.append("stun")


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
                target.hp -= 5
                target.status.append("burn")
        if 33 <= chance < 66:
            freeze = self.freeze()
            if freeze:
                target.status.append("freeze")
        else:
            absorb = self.absorb()
            if absorb:
                target.hp -= 20
                self.hp += 10
                target.status.append("absorb")


class Warrior(BasicUnit):

    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.hp = 150
        self.atk = 20
        self.armor = 10

    def use_special(self, target):
        self.atk += 5
        self.armor += 2
