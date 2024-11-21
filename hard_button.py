import pygame.font

class Hard:
    def __init__(self, ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()

        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.right=self.screen_rect.right
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.right=self.rect.right



    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

