#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            print(menu_return)

            # MENU OPTIONS
            if (
                    menu_return == MENU_OPTION[0] or  # NEW GAME 1P
                    menu_return == MENU_OPTION[1] or  # NEW GAME 2P COOPERATIVE
                    menu_return == MENU_OPTION[2]):  # NEW GAME 2P COMPETITIVE

                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)


            elif menu_return == MENU_OPTION[3]:  # SCORE
                pass

            elif menu_return == MENU_OPTION[4]:  # QUIT
                pygame.quit()
                quit()

            else:
                print("Invalid option")
