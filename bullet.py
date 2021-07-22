"""Moduł odpowiedzialny za pociski"""
import copy
import pygame
import constants


class Bullet:

    """Klasa odpowiedzialna za tworzenie pocisku"""
    def __init__(self, position, speed, direction: bool):
        self.position = copy.copy(position)
        self.speed = speed
        self.direction = direction
        self.image = constants.BULLET_IMG
        self.mask = pygame.mask.from_surface(self.image)

    def movement(self):
        """Metoda odpowiedzialna za ruch pocisku"""
        if self.direction is True:
            self.position[1] += -self.speed
        if self.direction is False:
            self.position[1] += self.speed

    def out_of_screen(self) -> bool:
        if self.position[1] > constants.SCREEN_HEIGHT or self.position[1] < -30:
            return True
        return False
