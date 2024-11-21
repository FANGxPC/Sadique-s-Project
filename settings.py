class custom_sett:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255,255,255)
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=30
        self.alien_speed=1.0
        self.fleet_drop=50
        self.ship_limit=3
        self.fleet_direction=1
        self.speedup_scale=1.5
        self.initialize_dynamic_settings1()
        self.initialize_dynamic_settings2()
        self.initialize_dynamic_settings3()

    def initialize_dynamic_settings1(self):
        self.ship_speed=1.5
        self.bullet_speed=5.0
        self.alien_speed=1.0
        self.fleet_direction=1

    def initialize_dynamic_settings2(self):
        self.ship_speed=2
        self.bullet_speed=5.0
        self.alien_speed=2.0
        self.fleet_direction=1

    def initialize_dynamic_settings3(self):
        self.ship_speed=2.2
        self.bullet_speed=5.0
        self.alien_speed=2.5
        self.fleet_direction=1

        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed*= self.speedup_scale



