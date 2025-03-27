#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        movement = [0, 0]  # [x, y]

        # PLAYERS MOVE
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: # MOVE UP
            movement[1] -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: # MOVE DOWN
            movement[1] += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: # MOVE LEFT
            movement[0] -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: # MOVE RIGHT
            movement[0] += ENTITY_SPEED[self.name]

        self.rect.move_ip(movement)