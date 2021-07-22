"""Moduł odpowiedzialny za menu gry."""
import sys
import pygame
import pygame.freetype


import constants


class Menu:
    """Klasa menu oraz pauzy"""

    def __init__(self, game):
        self.play_button = None
        self.pause_button = None

        self.game = game

        self.main_run = True
        self.pause_run = False

        self.center_position = (350, 250)
        self.font_size = 30
        self.mouse_over = False

    def main_loop(self, message):
        """Pętla głównego menu."""
        while self.main_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.game.screen.blit(constants.BG, (0, 0))
            self.drawing(message)
            self.mouse_colide(self.play_button)

            if self.button_pressed(self.play_button):
                self.main_run = False

            pygame.display.flip()

    def pause_loop(self, message):
        """Pętla pauzy."""
        while self.pause_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.pause_run = False

            self.game.screen.blit(constants.BG, (0, 0))
            self.drawing(message)

            pygame.display.flip()

    def create_button(self, text, text_color, font):
        """Tworzenie przycisku"""
        button, _ = font.render(text=text, fgcolor=text_color)
        button = button.convert_alpha()
        button_rect = button.get_rect(center=self.center_position)

        return button, button_rect

    def high_light_button(self, text, text_color):
        """Podświetla przycisk po najechaniu kursorem."""
        button = self.create_button(text, text_color, constants.Fonts.MENU_FONT)
        highlight_button = self.create_button(text, text_color, constants.Fonts.MENU_FONT_HIGHLIGHT)

        return (highlight_button[0], highlight_button[1]) if \
            self.mouse_over else (button[0], button[1])

    def mouse_colide(self, button):
        """Sprawdza czy kursor koliduje z przyciskiem."""
        if button[1].collidepoint(pygame.mouse.get_pos()):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def button_pressed(self, button) -> bool:
        """Sprawdza czy przycisk został wcisnięty."""
        if button[1].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        return False

    def drawing(self, message):
        """Rysowanie elementów mennu"""
        if self.main_run:
            self.play_button = self.high_light_button("play", constants.Colors.WHITE)
            self.game.screen.blit(self.play_button[0], self.play_button[1])

        self.instruction(message)

        if self.pause_run:
            self.pause_button = self.high_light_button("PAUSE", constants.Colors.WHITE)
            self.game.screen.blit(self.pause_button[0], self.pause_button[1])

    def instruction(self, message):
        msg_label, _ = constants.Fonts.INFO_FONT.render(
            text=message, fgcolor=constants.Colors.WHITE)

        msg_label = msg_label.convert_alpha()
        pos = msg_label.get_rect(center=(350, 200))
        self.game.screen.blit(msg_label, pos)

        label, _ = constants.Fonts.INFO_FONT.render(
            text="move your ship using the arrow", fgcolor=constants.Colors.WHITE)

        label = label.convert_alpha()
        pos = label.get_rect(center=(350, 400))
        self.game.screen.blit(label, pos)

        label, _ = constants.Fonts.INFO_FONT.render(
            text="stop game using p key          ", fgcolor=constants.Colors.WHITE)

        label = label.convert_alpha()
        pos = label.get_rect(center=(350, 420))
        self.game.screen.blit(label, pos)

        label, _ = constants.Fonts.INFO_FONT.render(
            text="shooting bullets using z key  ", fgcolor=constants.Colors.WHITE)

        label = label.convert_alpha()
        pos = label.get_rect(center=(350, 440))
        self.game.screen.blit(label, pos)



