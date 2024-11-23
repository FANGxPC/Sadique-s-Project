import sys
import pygame
from settings import custom_sett
from sship import Ship
from time import sleep
from game_stats import GameStats
from bullet import Bullet
from button import Button
from alien import Alien
from easy_button import Easy
from hard_button import Hard
from med_button import Med

class AI:
    def __init__(self):
        pygame.init()
        self.sett=custom_sett()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.sett.screen_width=self.screen.get_rect().width
        self.sett.screen_height=self.screen.get_rect().height
        pygame.display.set_caption('Alien Attacker')
        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self,"Play")
        self.easy_button=Easy(self,"Easy")
        self.med_button=Med(self,"Medium")
        self.hard_button=Hard(self,"Hard")
        self.noob=pygame.image.load('images/images.jpeg')
        self.noob = pygame.transform.scale(self.noob, (1200,800))  
        self.noob_rect=self.noob.get_rect()
        self.lvl_flag=False
        self.bullet_firing_rate = 2
        self.last_bullet_time =0
        

          

    def run_game(self):
        while  True:
            self._check_events()
            self._close_game()
            if not self.stats.game_active and self.lvl_flag==False:
                  self.play_button.draw_button()
            if not self.stats.game_active and self.lvl_flag==True:
                  self.easy_button.draw_button()
                  self.med_button.draw_button()
                  self.hard_button.draw_button()
            if self.stats.game_active:
                  self.ship.update()
                  self._update_aliens()
                  self._fire_bullet()
                  self._update_bullets()
                  self.screen.fill(self.sett.bg_color)
                  self.ship.blitme()
                  for bullet in self.bullets.sprites():
                        bullet.draw_bullet()
                  self.aliens.draw(self.screen)
                  
            pygame.display.flip()

    def _update_bullets(self):
            self.bullets.update()
            for bullet in self.bullets.copy():
                  if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
            collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
            if not self.aliens:
                  self.bullets.empty()
                  self._create_fleet()
                  self.sett.increase_speed()
                  

    def _update_aliens(self):    
          self._check_fleet_edges()
          self.aliens.update()
          self._check_aliens_bottom()
          if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            
            # print(self.stats.ships_left)

    def _check_fleet_edges(self):
          for alien in self.aliens.sprites():
                if alien.check_edges():
                      self._change_fleet_direction()
                      break
                
    def _change_fleet_direction(self):
          for alien in self.aliens.sprites():
                alien.rect.y += (self.sett.fleet_drop)
          self.sett.fleet_direction*=-1


    def _check_aliens_bottom(self):
          screen_rect=self.screen.get_rect()
          for alien in self.aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                      self._ship_hit()
                      break


    def _ship_hit(self):
      if self.stats.ships_left>0:
          self.stats.ships_left-=1
          self.aliens.empty()
          self.bullets.empty()
          self._create_fleet()
          self.ship.center_ship()
          sleep(0.5)
      else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
    
    def _close_game(self):
          if self.stats.ships_left<=0:
                self.stats.game_active=False
                self.lvl_flag=False
                pygame.mouse.set_visible(True)
                self.screen.blit(self.noob,self.noob_rect)
                


    def _create_fleet(self):
          alien=Alien(self)
          alien_width,alien_height=alien.rect.size
          available_space_x=self.sett.screen_width-(2*alien_width)
          ship_height=self.ship.rect.height
          available_space_y=(self.sett.screen_height-(3*alien_height)-ship_height)
          number_rows=available_space_y//(2*alien_height)
          number_aliens_x=available_space_x//(2*alien_width)
          for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)


    def _create_alien(self,alien_number,row_number):
                alien=Alien(self)
                alien_width,alien_height=alien.rect.size
                alien.x=alien_width+2*alien_width*alien_number
                alien.rect.x=alien.x
                alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
                self.aliens.add(alien)


    def  _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type==pygame.KEYDOWN:
                self.check_keydown_events(event)
            
            elif event.type==pygame.MOUSEBUTTONDOWN:
                  mouse_pos=pygame.mouse.get_pos()
                  if self.lvl_flag:
                        self._easy_play_button(mouse_pos)
                        self._med_play_button(mouse_pos)
                        self._hard_play_button(mouse_pos)
                  self._check_play_button(mouse_pos)
            

            elif event.type==pygame.KEYUP:
                self.check_keyup_events(event)
                
    def _easy_play_button(self,mouse_pos):
            if self.easy_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                  self.stats.reset_stats()
                  self.stats.game_active=True
                  self.aliens.empty()
                  self.bullets.empty()
                  self._create_fleet()
                  self.ship.center_ship()
                  self.sett.initialize_dynamic_settings1()
                  pygame.mouse.set_visible(True)

    def _med_play_button(self,mouse_pos):
            if self.med_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                  self.stats.reset_stats()
                  self.stats.game_active=True
                  self.aliens.empty()
                  self.bullets.empty()
                  self._create_fleet()
                  self.ship.center_ship()
                  self.sett.initialize_dynamic_settings2()
                  pygame.mouse.set_visible(True)

    def _hard_play_button(self,mouse_pos):
            if self.hard_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                  self.stats.reset_stats()
                  self.stats.game_active=True
                  self.aliens.empty()
                  self.bullets.empty()
                  self._create_fleet()
                  self.ship.center_ship()
                  self.sett.initialize_dynamic_settings3()
                  pygame.mouse.set_visible(True)


    def _check_play_button(self,mouse_pos):
            if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                  self.stats.reset_stats()
                  #self.stats.game_active=True
                  self.aliens.empty()
                  self.bullets.empty()
                  self._create_fleet()
                  self.ship.center_ship()
                  #self.sett.initialize_dynamic_settings()
                  pygame.mouse.set_visible(True)
                  self.lvl_flag=True
            
                  




    def check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
        if event.key==pygame.K_LEFT:
                    self.ship.moving_left=True
        if event.key==pygame.K_UP:
               self.ship.moving_up=True
        if event.key==pygame.K_DOWN:
               self.ship.moving_down=True
        if event.key==pygame.K_q:
              sys.exit()
        if event.key==pygame.K_SPACE :  
              self._fire_bullet()


    def check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
                    self.ship.moving_left=False
        if event.key==pygame.K_UP:
               self.ship.moving_up=False
        if event.key==pygame.K_DOWN:
               self.ship.moving_down=False

    def _fire_bullet(self):
      current_time = pygame.time.get_ticks() / 1000
      print(current_time)
      if current_time - self.last_bullet_time > self.bullet_firing_rate and len(self.bullets) < self.sett.bullet_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        self.last_bullet_time = current_time
  





if __name__=='__main__':
    
    AI().run_game()


