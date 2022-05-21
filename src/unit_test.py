import unittest
from basic_unit import *


class TestCombat(unittest.TestCase):

    def test_combat(self):
        warrior = Warrior()
        minion = EnemyMinion()
        combat = warrior.combat(minion)
        warrior_hp = warrior.hp
        self.assertEqual(combat, warrior_hp == 149)

    def test_special(self):
        warrior = Warrior()
        minion = EnemyMinion()
        use_special = warrior.use_special(minion)
        warrior_atk = warrior.get_atk()
        self.assertEqual(warrior_atk, 23)

    def test_alive(self):
        warrior = Warrior()
        self.assertTrue(warrior.is_alive(), True)

