import random


class BasicUnit:

    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.atk = 10
        self.armor = 3
        self.status = []

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def check_status(self):
        if not self.status:
            return None
        elif self.status == "stun":
            return self.status
        else:
            return self.status

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


'''Enemy Units'''


class EnemyMinion(BasicUnit):

    def __init__(self):
        super.__init__()


class EnemyBrute(BasicUnit):

    def __init__(self):
        super.__init__()
        self.hp = 100
        self.atk = 20
        self.armor = 10


'''Ally Units'''


class Wizard(BasicUnit):

    def __init__(self):
        self.hp = 150
        self.atk = 25
        self.armor = 5

    def stun(self):
        number = random.randint(0, 100)
        if number >= 50:
            return True
        else:
            return False

    def use_special(self, target):
        use_stun = self.stun()
        if use_stun:
            target.status.append("stun")


class Healer(BasicUnit):

    def __init__(self):
        self.hp = 150
        self.atk = 15
        self.armor = 5


class Warrior(BasicUnit):

    def __init__(self):
        self.hp = 200
        self.atk = 30
        self.armor = 15
