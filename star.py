import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.sett
        self.image=pygame.image.load('tara.jpeg')
        self.image = pygame.transform.scale(self.image, (100,100)) 
        self.image=pygame.transform.scale(self.image,(10,10))
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        
    def blit(self):    
        self.screen.blit(self.image,self.rect)