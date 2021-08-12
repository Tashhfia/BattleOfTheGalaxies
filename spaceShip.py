import pygame


class SpaceShip:
    """"A class to manage the behaviour of the player's space-ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # loading image of spaceship
        self.image = pygame.image.load('Images/4.bmp')
        self.rect = self.image.get_rect()

        # setting the starting point of the spaceship
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """"Function to draw the spaceship at its current location"""
        self.screen.blit(self.image, self.rect)