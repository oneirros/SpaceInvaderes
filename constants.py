import os
import pygame.freetype


SCREEN_WIDTH, SCREEN_HEIGHT = 700, 800
TPS_MAX = 80
PLAYER_START_PLACE = [320, 400]
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 85
PLAYER_HEALTH = 100
PLAYER_MAX_VELOCITY = 9

PLAYER_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("images", "Rocket.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))

BULLET_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("images", "bullet.png")), (25, 30))

GREEN_ALIEN_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("images", "Obcy_1.png")), (30, 30))

RED_ALIEN_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("images", "Obcy_2.png")), (30, 30))

BG = pygame.transform.scale(pygame.image.load(
    os.path.join("images", "spacebg.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

class Fonts:
    """Czcionki."""
    pygame.init()
    pygame.font.init()
    INFO_FONT = pygame.freetype.SysFont("Courier", 20, bold=True)
    MENU_FONT = pygame.freetype.SysFont("Courier", 30, bold=True)
    MENU_FONT_HIGHLIGHT = pygame.freetype.SysFont("Courier", 30 * 1.20, bold=True)


class Colors:
    """Paleta barw."""
    WHITE = (255, 255, 255)
