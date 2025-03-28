#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect, K_DOWN
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans TypeWriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_option = 0  # START MENU POSITION

        # LOAD MENU MUSIC
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer.music.play(-1)  # Param to Loop music

        while True:
            # DRAW IMAGES

            # SHOW TITLE MENU
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            # SHOW MENU OPTIONS
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_DOWN: # KEY DOWN
                                menu_option = (menu_option + 1) % len(MENU_OPTION)

                            case pygame.K_UP: # KEY UP
                                menu_option = (menu_option - 1) % len(MENU_OPTION)

                            case pygame.K_RETURN: # KEY ENTER
                                return MENU_OPTION[menu_option] # Return menu option name





