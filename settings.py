import pygame
class Settings:
    """A class to store all the settings for Red Planet Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (156, 46, 53)
        #self.bg = pygame.image.load("images/Space_Background1.png")
        self.ship_speed = 2.0
        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = (255, 43, 0)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1