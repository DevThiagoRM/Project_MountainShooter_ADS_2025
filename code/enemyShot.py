#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.entity import Entity


class EnemyShot(Entity):
    pass

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]