import pygame

BG = pygame.image.load("graphics/wallpaper.jpg")

def get_font(size):
        return pygame.font.Font("graphics/MIDNSBRG.ttf", size)

class Screen():
    def __init__(self, surface, screen_type, title_text, play_button_text, quit_button_text):
        self.screen_type = screen_type
        self.display_surface = surface
        self.menu_text = get_font(size=100).render(title_text, True, "Black")
        self.menu_rect = self.menu_text.get_rect(center=(720, 100))

        self.play_button_content = get_font(size=100).render(play_button_text, True, "Black")
        self.play_button = self.play_button_content.get_rect(center=(720, 300))

        self.quit_button_content = get_font(size=100).render(quit_button_text, True, "Black")
        self.quit_button = self.quit_button_content.get_rect(center=(720, 500))


    def run(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.display_surface.blit(BG, (0, 0))
        self.display_surface.blit(self.menu_text, self.menu_rect)
        self.display_surface.blit(self.play_button_content, self.play_button)
        self.display_surface.blit(self.quit_button_content, self.quit_button)