import random
import pygame

import constants
from bullet import Bullet


class Ship:

    def __init__(self, position, width, height, img, health):
        self.position = position
        self.width = width
        self.height = height
        self.img = img
        self.health = health
        self.bullets = []
        self.mask = None

    def control(self):
        """Odpowiada za sterowanie obiektami"""
        pass

    def shooting(self, position, bullet_sped: float, up_or_down: bool):
        """Generownie pocisków"""
        bullet = Bullet(position, bullet_sped, up_or_down)
        self.bullets.append(bullet)

    def remove_bullet(self, bullet):
        if bullet.out_of_screen():
            self.bullets.remove(bullet)

    def out_off_screen(self) -> bool:
        pass


class Player(Ship):

    def __init__(self, position, width, height, img, health):
        super().__init__(position, width, height, img, health)
        self.mask = pygame.mask.from_surface(self.img)
        self.score = 0
        self.pressed = False
        self.velocity = [0, 0]

    def control(self):
        acceleration = 0.35

        # control the ship with arrows
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP] and self.velocity[1] >= -constants.PLAYER_MAX_VELOCITY:
            self.velocity[1] += -acceleration

        if pressed_key[pygame.K_DOWN] and self.velocity[1] <= constants.PLAYER_MAX_VELOCITY:
            self.velocity[1] += acceleration

        if pressed_key[pygame.K_LEFT] and self.velocity[0] >= -constants.PLAYER_MAX_VELOCITY:
            self.velocity[0] += -acceleration
            if self.position[0] + self.velocity[0] < 0:
                self.velocity[0] = 0

        if pressed_key[pygame.K_RIGHT] and self.velocity[0] <= constants.PLAYER_MAX_VELOCITY:
            self.velocity[0] += acceleration
            if self.position[0] + self.velocity[0] > constants.SCREEN_WIDTH - constants.PLAYER_WIDTH:
                self.velocity[0] = 0

        if pressed_key[pygame.K_z] and len(self.bullets) < 5 and not self.pressed:
            self.shooting([self.position[0], self.position[1]], 5, True)
            self.pressed = True

        if not pressed_key[pygame.K_z]:
            self.pressed = False

        # gravity
        if not pressed_key[pygame.K_UP] and self.velocity[1] <= constants.PLAYER_MAX_VELOCITY:
            self.velocity[1] += 0.2

        self.velocity[0] *= 0.95

        if self.position[1] + self.velocity[1] < 0:
            self.velocity[1] = 0

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def out_off_screen(self) -> bool:
        if self.position[1] > constants.SCREEN_WIDTH + constants.PLAYER_HEIGHT + 30:
            return True
        return False


class Alien(Ship):
    def __init__(self, position, width, height, img, health):
        super().__init__(position, width, height, img, health)
        self.mask = pygame.mask.from_surface(self.img)

    def control(self):
        self.position[1] += 1
        if random.randrange(0, 120) == 50:
            self.shooting([self.position[0], self.position[1] + 15], 5, False)

    def out_off_screen(self) -> bool:
        if self.position[1] > constants.SCREEN_HEIGHT:
            return True
        return False
