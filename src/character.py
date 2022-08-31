import pygame

import src.glbl_nms
import pyganim


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.start_x = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.start_y = y
        self.image = pygame.Surface((200, 200))
        self.image.fill(pygame.Color("dark orange"))
        self.rect = pygame.Rect(x, y, 200, 200)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color("dark orange"))  # делаем фон прозрачным

    #Загрузка анимаций покоя и конструктор этих анимаций
    def set_anim(self, name):

        animation = [('character/' + name + '/present/0.png'),
                     ('character/' + name + '/present/1.png'),
                     ('character/' + name + '/present/2.png'),
                     ('character/' + name + '/present/3.png'),
                     ('character/' + name + '/present/4.png'),
                     ('character/' + name + '/present/5.png'),
                     ('character/' + name + '/present/6.png')]

        bolt_anim = []
        for anim in animation:
            bolt_anim.append((anim, src.glbl_nms.ANIMATION_DELAY))
        self.bolt_anim = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim.play()

    #Загрузка анимаций приёма пищи и конструктор этих анимаций
    def set_anim_eat(self, name):

        animation_eat = [('character/' + name + '/eating/0.png'),
                         ('character/' + name + '/eating/1.png')]

        bolt_anim_1 = []
        for anim in animation_eat:
            bolt_anim_1.append((anim, src.glbl_nms.ANIMATION_DELAY))
        self.bolt_anim_eat = pyganim.PygAnimation(bolt_anim_1)
        self.bolt_anim_eat.play()

    #Загрузка анимаций развлечения и конструктор этих анимаций
    def set_anim_mood(self, name):

        animation_mood = [('character/' + name + '/mood/0.png'),
                          ('character/' + name + '/mood/1.png'),
                          ('character/' + name + '/mood/2.png'),
                          ('character/' + name + '/mood/3.png')]

        bolt_anim_2 = []
        for anim in animation_mood:
            bolt_anim_2.append((anim, src.glbl_nms.ANIMATION_DELAY))
        self.bolt_anim_mood = pyganim.PygAnimation(bolt_anim_2)
        self.bolt_anim_mood.play()

    #Загрузка анимаций учёбы и конструктор этих анимаций
    def set_anim_learn(self, name):

        animation_learn = [('character/' + name + '/learn/0.png'),
                           ('character/' + name + '/learn/1.png'),
                           ('character/' + name + '/learn/2.png')]

        bolt_anim_3 = []
        for anim in animation_learn:
            bolt_anim_3.append((anim, src.glbl_nms.ANIMATION_DELAY))
        self.bolt_anim_learn = pyganim.PygAnimation(bolt_anim_3)
        self.bolt_anim_learn.play()

    #Загрузка анимаций ничего-нехотенья и конструктор этих анимаций
    def set_anim_disgust(self, name):

        animation_disgust = [('character/' + name + '/disgust/0.png')]

        bolt_anim_5 = []
        for anim in animation_disgust:
            bolt_anim_5.append((anim, src.glbl_nms.ANIMATION_DELAY))
        self.bolt_anim_disgust = pyganim.PygAnimation(bolt_anim_5)
        self.bolt_anim_disgust.play()

    #Анимация состояния покоя
    def update(self, screen):  # Выводим себя на экран

        if src.glbl_nms.EAT is False:
            if src.glbl_nms.LEARN is False:
                if src.glbl_nms.MOOD is False:
                    self.image.fill(("dark orange"))
                    self.bolt_anim.blit(self.image, (0, 0))
                    screen.blit(self.image, (self.start_x, self.start_y))

    #Анимация состояния приёма пищи, если у питомца онарексия, то обыгрывается анимация нехочухи
    def eat(self, screen):

        if src.glbl_nms.EAT is True:
            if src.glbl_nms.LEARN is False:
                if src.glbl_nms.MOOD is False:
                    if src.glbl_nms.you.eat == src.glbl_nms.EMPTY:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_disgust.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))
                    else:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_eat.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))

    #Анимация состояния развлечения, если у питомца депрессия, то обыгрывается анимация нехочухи
    def mood(self, screen):

        if src.glbl_nms.EAT is False:
            if src.glbl_nms.LEARN is False:
                if src.glbl_nms.MOOD is True:
                    if src.glbl_nms.you.mood == src.glbl_nms.EMPTY:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_disgust.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))
                    else:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_mood.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))

    #Анимация состояния учёбы, если питомец стал неучем, то обыгрывается анимация нехочухи
    def learn(self, screen):

        if src.glbl_nms.EAT is False:
            if src.glbl_nms.LEARN is True:
                if src.glbl_nms.MOOD is False:
                    if src.glbl_nms.you.learn == src.glbl_nms.EMPTY:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_disgust.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))
                    else:
                        self.image.fill(("dark orange"))
                        self.bolt_anim_learn.blit(self.image, (0, 0))
                        screen.blit(self.image, (self.start_x, self.start_y))


class PlayerDead(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.start_x = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.start_y = y
        self.image = pygame.Surface((200, 200))
        self.image.fill(pygame.Color("white"))
        self.rect = pygame.Rect(x, y, 200, 200)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color("white"))  # делаем фон прозрачным

    #Обыгрывается смерть питомца
    def dead(self, screen):
        if src.glbl_nms.DEAD is True:
            pygame.init()
            screen = pygame.display.set_mode(src.glbl_nms.DISPLAY)
            self.image = pygame.image.load(
                'character/dead/0.png').convert()
            self.image.set_colorkey((255, 255, 255))
            screen.blit(src.glbl_nms.bg, (0, 0))
            screen.blit(self.image, (self.start_x, self.start_y))
