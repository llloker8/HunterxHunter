# -*- coding: utf-8 -*-
from pygame import *
import os
import pyganim

PLATFORM_WIDTH1 = 32
PLATFORM_HEIGHT1 = 32
PLATFORM_COLOR1 = "#400030"
ICON_DIR1 = os.path.dirname(__file__)

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH1, PLATFORM_HEIGHT1))
        self.image.fill(Color(PLATFORM_COLOR1))
        self.image = image.load("%s/blocks/platform.jpg" % ICON_DIR1)
        self.image.set_colorkey(Color(PLATFORM_COLOR1))
        self.rect = Rect(x, y, PLATFORM_WIDTH1, PLATFORM_HEIGHT1)

class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("%s/blocks/dieBlock.png" % ICON_DIR1)
