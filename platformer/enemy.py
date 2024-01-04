from pygame.sprite import Sprite
from constants import *

class Enemy(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("")