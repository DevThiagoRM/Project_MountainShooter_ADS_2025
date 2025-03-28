#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class PlayerShot(Entity, ABC):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]