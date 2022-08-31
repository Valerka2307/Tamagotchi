import pygame
import src.pet
import src.character
import src.button

pygame.init()


WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверх4ности
bg = pygame.image.load("./images/im1.jpg")

screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
pygame.display.set_caption("TAMAGOTCHIK")  # Пишем в шапку


start_img = pygame.image.load('button/start_btn.png').convert_alpha()
exit_img = pygame.image.load('button/exit_btn.png').convert_alpha()

liliac_img = pygame.image.load('button/liliac.png').convert_alpha()
purple_img = pygame.image.load('button/purple.png').convert_alpha()
pink_img = pygame.image.load('button/pink.png').convert_alpha()

start_button = src.button.Button(WIN_WIDTH // 2 - 130,
                             WIN_HEIGHT // 2 - 100,
                             start_img, 1)

exit_button = src.button.Button(WIN_WIDTH // 2 - 110,
                            WIN_HEIGHT // 2 + 100,
                            exit_img, 1)

liliac_button = src.button.Button(330,
                              50,
                             liliac_img, 0.8)

purple_button = src.button.Button(0,
                             50,
                             purple_img, 0.8)

pink_button = src.button.Button(640,
                             50,
                             pink_img, 0.8)

ANIMATION_DELAY = 1000  # скорость смены кадров

FULL = 100
EMPTY = 0

COLOR = "black"

EAT = False
MOOD = False
LEARN = False
DEAD = False


you = src.pet.Pet()
tam = src.character.Player(100, 300)
tam_dead = src.character.PlayerDead(100, 300)
GAME_START = False
run = True
CHOOSE = False
