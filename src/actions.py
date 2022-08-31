import src.glbl_nms
import pygame
import src.condition


pygame.init()

#создание события
decrease = pygame.USEREVENT + 0
pygame.time.set_timer(decrease, 1000)

"""
Функция ограничивает параметры здоровья, сытости,
настроения и учёбы в пределах от нуля до ста.
Если здоровье равно нулю, то персонаж умирает

"""


def exam_of_param():
    src.glbl_nms.you.learn = min(src.glbl_nms.you.learn, src.glbl_nms.FULL)
    src.glbl_nms.you.eat = min(src.glbl_nms.you.eat, src.glbl_nms.FULL)
    src.glbl_nms.you.mood = min(src.glbl_nms.you.mood, src.glbl_nms.FULL)

    src.glbl_nms.you.hp += min(src.glbl_nms.you.eat, src.glbl_nms.EMPTY)
    src.glbl_nms.you.hp += min(src.glbl_nms.you.mood, src.glbl_nms.EMPTY)

    src.glbl_nms.you.learn = max(src.glbl_nms.you.learn, src.glbl_nms.EMPTY)
    src.glbl_nms.you.eat = max(src.glbl_nms.you.eat, src.glbl_nms.EMPTY)
    src.glbl_nms.you.mood = max(src.glbl_nms.you.mood, src.glbl_nms.EMPTY)

    if src.glbl_nms.you.hp <= src.glbl_nms.EMPTY:
        src.glbl_nms.you.hp = src.glbl_nms.FULL
        src.glbl_nms.you.learn = src.glbl_nms.FULL
        src.glbl_nms.you.eat = src.glbl_nms.FULL
        src.glbl_nms.you.mood = src.glbl_nms.FULL
        src.glbl_nms.DEAD = True


"""
Функция определяет, ест ли, развлекается или учится питомец.
В зависимости от действий у питомца понижаются или повышаются параметры.
Также, если все параметры равны нулю, кроме здоровья, то здоровье понижается

"""


def action_with_stats():
    if src.glbl_nms.you.eat > src.glbl_nms.EMPTY:
        if src.glbl_nms.EAT is False:
            src.glbl_nms.you.eat -= 1
        elif src.glbl_nms.EAT is True:
            src.glbl_nms.you.eat += 2
    if src.glbl_nms.you.mood > src.glbl_nms.EMPTY:
        if src.glbl_nms.MOOD is False:
            src.glbl_nms.you.mood -= 1
        elif src.glbl_nms.MOOD is True:
            src.glbl_nms.you.mood += 2
    if src.glbl_nms.you.learn > src.glbl_nms.EMPTY:
        if src.glbl_nms.LEARN is False:
            src.glbl_nms.you.learn -= 1
        elif src.glbl_nms.LEARN is True:
            src.glbl_nms.you.learn += 2
    if src.glbl_nms.you.eat == 0:
        if src.glbl_nms.you.mood == 0:
            if src.glbl_nms.you.learn == 0:
                src.glbl_nms.you.hp -= 50


"""
Функция, обрабатывающая события(прожатие клавиш и событие pygame)

"""


def decr_of_stats():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            src.glbl_nms.EAT = True
        if e.type == pygame.KEYUP and e.key == pygame.K_e:
            src.glbl_nms.EAT = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
            src.glbl_nms.MOOD = True
        if e.type == pygame.KEYUP and e.key == pygame.K_m:
            src.glbl_nms.MOOD = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_l:
            src.glbl_nms.LEARN = True
        if e.type == pygame.KEYUP and e.key == pygame.K_l:
            src.glbl_nms.LEARN = False
        if e.type == decrease and src.glbl_nms.GAME_START is True:
            action_with_stats()


"""
Функция, которая, отображает параметры питомца
"""


def blit_stats(screen):
    param1 = f"HP:   {src.glbl_nms.you.hp}"
    if src.glbl_nms.you.mood > src.glbl_nms.EMPTY:
        param2 = f"mood:{src.glbl_nms.you.mood}"
    else:
        param2 = "DEPRESSION!!!"
    if src.glbl_nms.you.eat > src.glbl_nms.EMPTY:
        param3 = f"food:  {src.glbl_nms.you.eat}"
    else:
        param3 = "ONAREXIA!!!"
    if src.glbl_nms.you.learn > src.glbl_nms.EMPTY:
        param4 = f"learn: {src.glbl_nms.you.learn}"
    else:
        param4 = "REDNECK!!!"
    src.condition.draw_text(screen, param1, 20, 60, 10)
    src.condition.draw_text(screen, param2, 20, 60, 30)
    src.condition.draw_text(screen, param3, 20, 60, 50)
    src.condition.draw_text(screen, param4, 20, 60, 70)


"""
Функция, которая, определяет, если питомец умер,
то игра окончена и игрок может начать всё сначала

"""


def dead(screen):
    if src.glbl_nms.DEAD is True:
        src.glbl_nms.tam_dead.dead(screen)
        src.condition.draw_text(screen, f"ЖАЛЬ ПАЦАНА!", 90, 400, 50)
        pygame.display.update()
        pygame.time.wait(3000)
        src.glbl_nms.GAME_START = False
        src.glbl_nms.CHOOSE = False
        src.glbl_nms.DEAD = False
        src.glbl_nms.LEARN = False
        src.glbl_nms.MOOD = False
        src.glbl_nms.EAT = False


"""
Отрисовка кнопок начала игры и выхода, а также их функционал
"""


def first_buttons():
    if src.glbl_nms.start_button.draw(src.glbl_nms.screen):
        src.glbl_nms.GAME_START = True

    if src.glbl_nms.exit_button.draw(src.glbl_nms.screen):
        src.glbl_nms.run = False


"""
Функция, отрисовывающая кнопки цвета персонажа и 
позволющая его цвет
"""


def choose_of_color():
    if src.glbl_nms.liliac_button.draw(src.glbl_nms.screen):
        src.glbl_nms.tam.set_anim("liliac")
        src.glbl_nms.tam.set_anim_eat("liliac")
        src.glbl_nms.tam.set_anim_mood("liliac")
        src.glbl_nms.tam.set_anim_learn("liliac")
        src.glbl_nms.tam.set_anim_disgust("liliac")
        src.glbl_nms.CHOOSE = True
    if src.glbl_nms.purple_button.draw(src.glbl_nms.screen):
        src.glbl_nms.tam.set_anim("purple")
        src.glbl_nms.tam.set_anim_eat("purple")
        src.glbl_nms.tam.set_anim_mood("purple")
        src.glbl_nms.tam.set_anim_learn("purple")
        src.glbl_nms.tam.set_anim_disgust("purple")
        src.glbl_nms.CHOOSE = True
    if src.glbl_nms.pink_button.draw(src.glbl_nms.screen):
        src.glbl_nms.tam.set_anim("pink")
        src.glbl_nms.tam.set_anim_eat("pink")
        src.glbl_nms.tam.set_anim_mood("pink")
        src.glbl_nms.tam.set_anim_learn("pink")
        src.glbl_nms.tam.set_anim_disgust("pink")
        src.glbl_nms.CHOOSE = True
