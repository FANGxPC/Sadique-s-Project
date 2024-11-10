import pygame

class Ship:
    def  __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.sett
        self.screen_rect=ai_game.screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.image=pygame.image.load('images/UFO.bmp')
        self.image = pygame.transform.scale(self.image, (100,100))  
        self.rect=self.image.get_rect()
        
        # print(f"Screen rect: {self.screen_rect}") 
        # print(f"Ship rect before positioning: {self.rect}")
        self.rect.midbottom=self.screen_rect.midbottom
       
        self.x=float(self.rect.x)



    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        if self.moving_up and self.rect.top>0:
            self.rect.y-=1
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y+=1
        
        self.rect.x=self.x