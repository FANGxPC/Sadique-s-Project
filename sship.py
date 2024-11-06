import pygame

class Ship:
    def  __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.image=pygame.image.load('images/UFO.bmp')
        self.image = pygame.transform.scale(self.image, (100,170))  
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right:
            self.rect.x+=1
        elif self.moving_left:
            self.rect.x-=1