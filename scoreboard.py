import pygame.font
class ScoreBoard:
    """A class reporting the scoring information."""

    def __init__(self, rpi_game):
        """Initialize scorekeeping attributes."""
        self.screen = rpi_game.screen
        self.screen_rect = rpi_game.screen.get_rect()
        self.settings = rpi_game.settings
        self.stats = rpi_game.stats

        # Font settings for scoring information.
        self.text_color = (230, 75, 43)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare to initialize score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)