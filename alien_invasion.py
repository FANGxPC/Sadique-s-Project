import sys
import pygame
from settings import custom_sett
from sship import Ship
from bullet import Bullet

class AI:
    def __init__(self):
        pygame.init()
        self.sett=custom_sett()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.sett.screen_width=self.screen.get_rect().width
        self.sett.screen_height=self.screen.get_rect().height
        pygame.display.set_caption('Alien Attacker')
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()


    def run_game(self):
        while  True:
            self._check_events()
            self.ship.update()
            
            self._update_bullets()
            self.screen.fill(self.sett.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            pygame.display.flip()

    def _update_bullets(self):
            self.bullets.update()
            for bullet in self.bullets.copy():
                  if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
            # print(len(self.bullets))


    def  _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type==pygame.KEYDOWN:
                self.check_keydown_events(event)
                

            elif event.type==pygame.KEYUP:
                self.check_keyup_events(event)
                
    def check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
        if event.key==pygame.K_LEFT:
                    self.ship.moving_left=True
        if event.key==pygame.K_q:
              sys.exit()
        if event.key==pygame.K_SPACE:
              self._fire_bullet()


    def check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
                    self.ship.moving_left=False

    def _fire_bullet(self):
          if len(self.bullets)<self.sett.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)





if __name__=='__main__':
    
    AI().run_game()


