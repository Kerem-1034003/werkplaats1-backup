import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=pos)


class Terrain(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, imagefile):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            imagefile).convert_alpha(), (width, height))
        self.rect = self.image.get_rect(topleft=pos)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            f'graphics/door/portal.png').convert_alpha(), (width, height))
        self.rect = self.image.get_rect(topleft=pos)