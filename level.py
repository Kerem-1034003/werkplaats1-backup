import pygame
from tiles import Terrain, Tile, Door
from player import Player
from settings import tile_size, screen_height, screen_width
import status


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()
        self.bad_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 40)

        # Maak een tile aan en plaats deze op de plekken buiten het scherm. Deze functioneren
        # als borders waardoor de speler niet buiten het veld kan komen.
        left_border = Tile((-tile_size, 0), tile_size, screen_height)
        self.tiles.add(left_border)
        top_border = Tile((0, -tile_size), screen_width, tile_size)
        self.tiles.add(top_border)
        right_border = Tile((screen_width, 0), tile_size, screen_height)
        self.tiles.add(right_border)
        bottom_border = Tile((0, screen_height), screen_width, tile_size)
        self.tiles.add(bottom_border)

        # Hier worden tiles aangemaakt, en vervolgens in de tilegroup genaamd tiles gezet
        # inplaats van elke tile op het scherm tekenen, teken je de groep in 1 keer.
        for row_index, row_content in enumerate(layout):
            for col_index, col_item in enumerate(row_content):
                x = col_index * tile_size
                y = row_index * tile_size
                if col_item == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif col_item == "1":
                    door_sprite = Door((x, y), tile_size*2, tile_size*2)
                    self.door.add(door_sprite)
                elif col_item == "A":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/A.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "B":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/B.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "C":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/C.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "D":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/D.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "E":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/E.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "F":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/F.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "G":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/G.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "H":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/H.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "I":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/I.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "K":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/K.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "L":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/L.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "M":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/M.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "X":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/X.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "Y":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/Y.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "Z":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/Z.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "0":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/0.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == 'R':
                    terrain_sprite = Terrain((x, y), tile_size, tile_size, 'graphics/crate/crate.png')
                    self.tiles.add(terrain_sprite)
                elif col_item == "S":
                    spike_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/spike/spike.png')
                    self.bad_sprites.add(spike_sprite)
                elif col_item == "2":
                    coin_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/other/coin.png')
                    self.coins.add(coin_sprite)
                elif col_item == "3":
                    terrain_sprite = Terrain(
                        (x, y), tile_size, tile_size, 'graphics/terrain/3.jpg')
                    self.tiles.add(terrain_sprite)
                elif col_item == 'N':
                    terrain_sprite = Terrain((x, y), tile_size, tile_size*2, 'graphics/palm/palm.png')
                    self.tiles.add(terrain_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True


    def door_collision(self):
        player = self.player.sprite
        for door in self.door.sprites():
            if door.rect.colliderect(player.rect):
                status.level_status = status.level_status + 1

    def bad_sprite_collision(self):
        player = self.player.sprite
        for sprite in self.bad_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                player.rect.x = 30
                player.rect.y = 700
                status.level_status = -1

    def coin_collision(self):
        player = self.player.sprite
        for coin in self.coins.sprites():
            if coin.rect.colliderect(player.rect):
                status.current_score = status.current_score + 1
                coin.kill()

    def run(self):
        self.tiles.update()
        self.tiles.draw(self.display_surface)

        self.coin_collision()
        self.coins.draw(self.display_surface)
        self.display_surface.blit(self.font.render(f'Score: {status.current_score}', False, 'Green'), (0, 0))

        self.door_collision()
        self.door.draw(self.display_surface)

        self.bad_sprite_collision()
        self.bad_sprites.draw(self.display_surface)

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
