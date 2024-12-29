import sys
import pygame
from random import randint
from star import Star
# from ship import Ship
class Starry:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Starry Sky')
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.sett_rect=self.screen.get_rect()
        self.sett_screen_width=self.sett_rect.width
        self.sett_screen_height=self.sett_rect.height
        self.color=(0,0, 0)
        # self.ship=Ship(self)
        self.stars=pygame.sprite.Group()
        self._create_stars()
        
    def run_game(self):
        while True:
            
            self._check_events()
            self.screen.fill(self.color)
            self.stars.draw(self.screen)
            self._change_stars_direction()
            self._update_stars()
            # self._the_loop()
            # self.ship.blit()
            pygame.display.flip()

    def _create_stars(self):
          star=Star(self)
          star_width,star_height=star.rect.size
          available_space_x=self.sett_screen_width-(2*star_width)
        #   ship_height=self.star.rect.height
          available_space_y=(self.sett_screen_height-(3*star_height))
          number_rows=available_space_y//(2*star_height)
          number_stars_x=available_space_x//(2*star_width)
          for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self.random_number=randint(1,100)
                if self.random_number in [6,8] :
                     self.flag=True
                else:
                    self.flag=False
                if self.flag:
                    self._create_star(star_number,row_number)
    
    # def _the_loop(self):
    #       while len(self.stars)==0:
    #             self._create_fleet()
                

    def _update_stars(self):
            self.stars.update()
            for bullet in self.stars.copy():
                  if bullet.rect.bottom >= self.sett_rect.bottom:
                        bullet.rect.top=self.sett_rect.top

                        # print(len(self.stars))

    def _create_star(self,star_number,row_number):
                star=Star(self)
                star_width,star_height=star.rect.size
                star.x=star_width+2*star_width*star_number
                star.rect.x=star.x
                star.rect.y=star.rect.height+2*star.rect.height*row_number
                self.stars.add(star)

    def _change_stars_direction(self):
        #   self.ship.rect.y-=1
          for star in self.stars.sprites():
                star.rect.y += (1)

    def _check_events(self):
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                         sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        sys.exit()








if __name__=='__main__':
    Starry().run_game()
            