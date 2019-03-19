#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os
import blocks
import monsters

MOVE_SPEED = 7
MOVE_EXTRA_SPEED = 3
WIDTH = 110
HEIGHT = 115
COLOR =  "#888888"
JUMP_POWER = 10
JUMP_EXTRA_POWER = 1 #резерв так сказать
GRAVITY = 0.35 
ANIMATION_DELAY = 0.05 # вот про что говорил
ANIMATION_SUPER_SPEED_DELAY = 0.0005 # это уже какой-то gear second
ICON_DIR = os.path.dirname(__file__) #  на это не смотри

ANIMATION_RIGHT = [('%s/D/walk0001.png' % ICON_DIR),
            ('%s/D/walk0002.png' % ICON_DIR),
            ('%s/D/walk0003.png' % ICON_DIR),
            ('%s/D/walk0004.png' % ICON_DIR),
            ('%s/D/walk0005.png' % ICON_DIR),
            ('%s/D/walk0006.png' % ICON_DIR),
            ('%s/D/walk0007.png' % ICON_DIR),
            ('%s/D/walk0008.png' % ICON_DIR),
            ('%s/D/walk0009.png' % ICON_DIR),
            ('%s/D/walk0010.png' % ICON_DIR),
            ('%s/D/walk0011.png' % ICON_DIR),
            ('%s/D/walk0012.png' % ICON_DIR),
            ('%s/D/walk0013.png' % ICON_DIR),
            ('%s/D/walk0014.png' % ICON_DIR),
            ('%s/D/walk0015.png' % ICON_DIR),
            ('%s/D/walk0016.png' % ICON_DIR),
            ('%s/D/walk0017.png' % ICON_DIR),
            ('%s/D/walk0018.png' % ICON_DIR),
            ('%s/D/walk0019.png' % ICON_DIR),
            ('%s/D/walk0020.png' % ICON_DIR),
            ('%s/D/walk0021.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/D/walkR0001.png' % ICON_DIR),
                  ('%s/D/walkR0002.png' % ICON_DIR),
                  ('%s/D/walkR0003.png' % ICON_DIR),
                  ('%s/D/walkR0004.png' % ICON_DIR),
                  ('%s/D/walkR0005.png' % ICON_DIR),
                  ('%s/D/walkR0006.png' % ICON_DIR),
                  ('%s/D/walkR0007.png' % ICON_DIR),
                  ('%s/D/walkR0008.png' % ICON_DIR),
                  ('%s/D/walkR0009.png' % ICON_DIR),
                  ('%s/D/walkR0010.png' % ICON_DIR),
                  ('%s/D/walkR0011.png' % ICON_DIR),
                  ('%s/D/walkR0012.png' % ICON_DIR),
                  ('%s/D/walkR0013.png' % ICON_DIR),
                  ('%s/D/walkR0014.png' % ICON_DIR),
                  ('%s/D/walkR0015.png' % ICON_DIR),
                  ('%s/D/walkR0016.png' % ICON_DIR),
                  ('%s/D/walkR0017.png' % ICON_DIR),
                  ('%s/D/walkR0018.png' % ICON_DIR),
                  ('%s/D/walkR0019.png' % ICON_DIR),
                  ('%s/D/walkR0020.png' % ICON_DIR),
                  ('%s/D/walkR0021.png' % ICON_DIR)]
ANIMATION_JUMP_RIGHT = [('%s/D/JNF0001.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0002.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0003.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0004.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0005.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0006.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0007.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0008.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0009.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0010.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0011.png' % ICON_DIR, 0.1),
                       ('%s/D/JNF0012.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_LEFT = [('%s/D/JNFR0001.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0002.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0003.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0004.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0005.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0006.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0007.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0008.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0009.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0010.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0011.png' % ICON_DIR, 0.1),
                        ('%s/D/JNFR0012.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/D/walk0001.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/D/stand0001.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0002.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0003.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0004.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0005.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0006.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0007.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0008.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0009.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0010.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0011.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0012.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0013.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0014.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0015.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0016.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0017.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0018.png' % ICON_DIR, 0.1),
                  ('%s/D/stand0020.png' % ICON_DIR, 0.1)]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость движа
        self.startX = x 
        self.startY = y
        self.yvel = 0 # потом скажу
        self.onGround = False # тут понятно
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) 
        self.image.set_colorkey(Color(COLOR)) # прозрачный фон

        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimRightSuperSpeed.play()       
        boltAnim = []
        boltAnimSuperSpeed = [] 
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimLeftSuperSpeed.play()
        
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим
        
        self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        
        self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        self.winner = False
        

    def update(self, left, right, up, running, platforms):
        
        if up:
            if self.onGround: #если мы на земле, то прыг
                self.yvel = -JUMP_POWER
                if running and (left or right): # понятно
                       self.yvel -= JUMP_EXTRA_POWER 
                self.image.fill(Color(COLOR))
                self.boltAnimJump.blit(self.image, (0, 0))
                       
        if left:
            self.xvel = -MOVE_SPEED 
            self.image.fill(Color(COLOR))
            if running: 
                self.xvel-=MOVE_EXTRA_SPEED 
                if not up:
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))
            else: 
                if not up: 
                    self.boltAnimLeft.blit(self.image, (0, 0)) 
            if up:
                    self.boltAnimJumpLeft.blit(self.image, (0, 0)) 
 
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if running:
                self.xvel+=MOVE_EXTRA_SPEED
                if not up:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimRight.blit(self.image, (0, 0)) 
            if up:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
 
         
        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
            
        if not self.onGround:
            self.yvel +=  GRAVITY
            
        self.onGround = False; # Мы не знаем, когда мы на земле((   
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): 
                if isinstance(p, blocks.BlockDie) or isinstance(p, monsters.Monster): 
                       self.die()# умираем
                elif isinstance(p, blocks.BlockTeleport):
                       self.teleporting(p.goX, p.goY)
                elif isinstance(p, blocks.Princess): # если коснулись принцессы
                       self.winner = True # победили!!!
                else:
                    if xvel > 0:                      # если движется вправо
                        self.rect.right = p.rect.left # то не движется вправо

                    if xvel < 0:                      # если движется влево
                        self.rect.left = p.rect.right # то не движется влево

                    if yvel > 0:                      # если падает вниз
                        self.rect.bottom = p.rect.top # то не падает вниз
                        self.onGround = True          # и становится на что-то твердое
                        self.yvel = 0                 # и энергия падения пропадает

                    if yvel < 0:                      # если движется вверх
                        self.rect.top = p.rect.bottom # то не движется вверх
                        self.yvel = 0                 # и энергия прыжка пропадает

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
        
    def die(self):
        time.wait(500)
        self.teleporting(self.startX, self.startY) # перемещаемся в начало