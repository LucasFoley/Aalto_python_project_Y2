from Basic_unit import *
from GUI import *


def main():
    ally_positions = []
    enemy_positions = []

    wizard = Wizard()
    healer = Healer()
    warrior = Warrior()

    ally_positions.append(wizard)
    ally_positions.append(healer)
    ally_positions.append(warrior)

    print(ally_positions)

    gui = run_gui()
    gui()


if __name__ == '__main__':
    main()
