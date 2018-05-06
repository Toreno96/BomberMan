import pygame

class Bomb(object):

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy
        self.rect = pygame.Rect(self.xx, self.yy, 30, 30)
        self.start_timer = pygame.time.get_ticks()
        self.desc = "bomb"
        print(self.start_timer)

    def blow(self):
        print("Wybuchaa!!!")

    def get_bomb(self):
        return self
