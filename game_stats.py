class GameStats:
    """Track statistics for Red Planet Invasion."""

    def __init__(self, rpi_game):
        """Initialize statistics."""
        self.settings = rpi_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0
        

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1