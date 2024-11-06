import sys
import pygame
from settings import custom_sett
from sship import Ship


class AI:
    def __init__(self):
        pygame.init()
        self.sett=custom_sett()
        self.screen=pygame.display.set_mode((self.sett.screen_width,self.sett.screen_height))
        pygame.display.set_caption('Alien Attacker')
        self.ship=Ship(self)
    

    def run_game(self):
        while  True:
            self._check_events()
            self.ship.update()
            self.screen.fill(self.sett.bg_color)
            self.ship.blitme()
            pygame.display.flip()
    def  _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
                if event.key==pygame.K_LEFT:
                    self.ship.moving_left=True

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                if event.key==pygame.K_LEFT:
                    self.ship.moving_left=False


if __name__=='__main__':
    
    AI().run_game()


