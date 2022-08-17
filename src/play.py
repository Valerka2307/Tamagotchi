import pygame
import src.glbl_nms
import src.actions

clock = pygame.time.Clock()


def game():
    pygame.init()  # Инициация PyGame, обязательная строчка

    src.glbl_nms.GAME_START = False

    while src.glbl_nms.run:  # Основной цикл программы
        pygame.event.pump()
        src.glbl_nms.screen.blit(src.glbl_nms.bg, (0, 0))
        if src.glbl_nms.GAME_START is False:
            src.actions.first_buttons()

        elif src.glbl_nms.CHOOSE is False:
            src.actions.choose_of_color()

        else:
            clock.tick(60)
            src.actions.exam_of_param()
            src.actions.decr_of_stats()
            src.actions.blit_stats(src.glbl_nms.screen)
            src.glbl_nms.tam.update(src.glbl_nms.screen)
            src.glbl_nms.tam.eat(src.glbl_nms.screen)
            src.glbl_nms.tam.mood(src.glbl_nms.screen)
            src.glbl_nms.tam.learn(src.glbl_nms.screen)
            src.actions.dead(src.glbl_nms.screen)

        pygame.display.update()
