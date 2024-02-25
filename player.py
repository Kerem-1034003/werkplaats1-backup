import pygame
from settings import tile_size

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.idle_image = pygame.transform.scale(pygame.image.load(f'graphics/player/idle.png').convert_alpha(), (tile_size, tile_size))
        self.jump_image = pygame.transform.scale(pygame.image.load(f'graphics/player/jump.png').convert_alpha(), (tile_size, tile_size))
        self.fall_image = pygame.transform.scale(pygame.image.load(f'graphics/player/fall.png').convert_alpha(), (tile_size, tile_size))
        self.image = self.idle_image
        #self.image = pygame.Surface((tile_size, tile_size))
        #self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_height = -12
        
        self.status = 'idle'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.facing_right = True

    def animate(self):
        if self.status == 'jump' and self.facing_right == False:
            self.image =  pygame.transform.flip(self.jump_image, True, False)
        elif self.status == 'fall' and self.facing_right == False:
            self.image = pygame.transform.flip(self.fall_image, True, False)
        elif self.status == 'idle' and self.facing_right == False:
            self.image = pygame.transform.flip(self.idle_image, True, False)
        elif self.status == 'jump':
            self.image =  self.jump_image
        elif self.status == 'fall':
            self.image = self.fall_image
        elif self.status == 'idle':
            self.image = self.idle_image

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.facing_right = True
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.facing_right = False
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height

    def update(self):
       self.get_input()
       self.animate()
       self.get_status()
       