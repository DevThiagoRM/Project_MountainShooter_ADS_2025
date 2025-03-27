#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from typing import List

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000 # 20 seconds
        self.window = window
        self.name = name
        self.game_Mode = game_mode
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, ):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans TypeWriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        # LOAD LEVEL 1 MUSIC
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer.music.play(-1)  # Param to Loop music

        # Refresh Rate
        clock = pygame.time.Clock()

        while True:
            clock.tick(60) # FPS

            # Refresh display
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Quit Game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Printed text
            self.level_text(14, f'{self.name} Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()