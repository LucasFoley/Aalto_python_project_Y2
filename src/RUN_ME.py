from basic_unit import *
from GUI import *
from posistions import *


def main():

    wizard = Wizard()
    healer = Healer()
    warrior = Warrior()

    gui = run_gui()
    gui()


if __name__ == '__main__':
    main()
