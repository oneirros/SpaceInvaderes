import random
import sys
import pygame

import constants
from ship import Player
from ship import Alien
from menu import Menu
import collisions
import levels


class Game:

    def __init__(self):

        self.run = True
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tick = 0
        self.tps_delta = 0.0
        self.tps_delta_green_alien = 0.0
        self.tps_delta_red_alien = 0.0
        self.player = Player(
            constants.PLAYER_START_PLACE,
            constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT,
            constants.PLAYER_IMG,
            constants.PLAYER_HEALTH
        )
        self.menu = Menu(self)
        self.aliens = []
        self.game_over_msg = ""

        pygame.init()
        pygame.font.init()

        pygame.display.set_caption("SpaceInvaders")

        while self.run:
            self.menu.main_loop(self.game_over_msg)
            self.menu.pause_loop("")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.menu.pause_run = True

            self.tick = self.clock.tick() / 1000.0
            self.tps_delta += self.tick
            self.tps_delta_green_alien += self.tick

            if self.tps_delta_green_alien >= levels.tps_max_green_alien(self.player.score):
                self.aliens.append(Alien(
                    [random.randint(15, constants.SCREEN_WIDTH - 30), -30],
                    30,
                    30,
                    constants.GREEN_ALIEN_IMG,
                    1
                    )
                )
                self.tps_delta_green_alien = 0

            self.tps_delta_red_alien += self.tick
            if self.tps_delta_red_alien >= levels.tps_max_red_alien(self.player.score) and self.player.score > 500:
                self.aliens.append(Alien(
                    [random.randint(15, constants.SCREEN_WIDTH - 30), -30],
                    30,
                    30,
                    constants.RED_ALIEN_IMG,
                    2
                )
                )
                self.tps_delta_red_alien = 0

            if self.tps_delta > 1 / constants.TPS_MAX:
                self.ticking()
                self.tps_delta = 0.0

            self.drawing()
            self.check_collisions()

            pygame.display.flip()

    def drawing(self) -> None:
        self.screen.blit(constants.BG, (0, 0))
        self.screen.blit(self.player.img, (self.player.position[0], self.player.position[1]))
        self.health_bar()
        self.score()

        for alien in self.aliens:
            self.screen.blit(alien.img, (alien.position[0], alien.position[1]))

            for bullet in alien.bullets:
                self.screen.blit(bullet.image, (bullet.position[0], bullet.position[1]))

        for bullet in self.player.bullets:
            self.screen.blit(bullet.image, (bullet.position[0], bullet.position[1]))

    def ticking(self) -> None:
        self.player.control()

        for bullet in self.player.bullets:
            bullet.movement()

        for alien in self.aliens:
            alien.control()
            for bullet in alien.bullets:
                bullet.movement()

    def health_bar(self):
        """Tworzy pasek życia"""
        pygame.draw.rect(
            self.screen, (255, 0, 0),
            (self.player.position[0] - 15, self.player.position[1] + self.player.height + 2, 60, 7))
        pygame.draw.rect(
            self.screen, (0, 255, 0), (
                self.player.position[0] - 15, self.player.position[1] + self.player.height + 2,
                (60 * self.player.health) / 100, 7))

    def score(self):
        score_label, _ = constants.Fonts.INFO_FONT.render(
            text="score {}".format(self.player.score), fgcolor=constants.Colors.WHITE)
        score_label = score_label.convert_alpha()
        pos = score_label.get_rect(center=(65, 10))
        self.screen.blit(score_label, pos)

    def check_collisions(self):

        for alien in self.aliens:
            if alien.out_off_screen():
                self.aliens.remove(alien)
            if collisions.collide(alien, self.player):
                self.aliens.remove(alien)
                self.player.health -= 25

            for bullet in alien.bullets:
                alien.remove_bullet(bullet)

            for bullet in alien.bullets:
                if collisions.collide(bullet, self.player):
                    self.player.health -= 10
                    alien.bullets.remove(bullet)

            for bullet in self.player.bullets:
                if collisions.collide(alien, bullet):
                    alien.health -= 1
                    self.player.bullets.remove(bullet)
                    self.player.score += 40
                    if alien.health <= 0:
                        self.aliens.remove(alien)

        for bullet in self.player.bullets:
            self.player.remove_bullet(bullet)

        if self.player.health <= 0 or self.player.out_off_screen():
            self.game_over_msg = "GAME OVER"
            self.game_over()
            self.menu.main_run = True

    def game_over(self):
        self.player.score = 0
        self.player.health = 100
        self.player.bullets.clear()
        self.player.position = [320, 400]

        self.aliens.clear()
        self.tps_delta = 0
        self.tps_delta_red_alien = 0
        self.tps_delta_green_alien = 0


if __name__ == "__main__":
    Game()
