class Speed:
    def __init__(self):
        self.speed = 0.1

    def increase_game_speed(self):
        self.speed *= 0.9
        return self.speed

    def restart_speed(self):
        self.speed = 0.1
