import pygame
from Game.entity import Entity
from Game.constants import *
from Game.sprites import FruitSprites

class Fruit(Entity):
    def __init__(self, node):
        Entity.__init__(self, node)
        self.name = FRUIT
        self.color = GREEN
        self.lifespan = 5
        self.timer = 0
        self.destroy = False
        self.points = 100
        self.setBetweenNodes(RIGHT)
        self.sprites = FruitSprites(self)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifespan:
            self.destroy = True