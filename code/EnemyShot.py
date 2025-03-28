#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class EnemyShot(Entity):

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]