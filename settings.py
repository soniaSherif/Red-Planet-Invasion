import pygame
class Settings:
    """A class to store all the settings for Red Planet Invasion."""

    def __init__(self):
        """Initialize the game's  staticsettings."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 880
        self.bg_color = (0, 0, 0)
        #self.bg = pygame.image.load("images/Space_Background1.png")
        # Ship settings
        
        self.ships_limit = 3
        # Bullet settings
        
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = (255, 43, 0)
        self.bullets_allowed = 3
        # Alien settings
        
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.3

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    
