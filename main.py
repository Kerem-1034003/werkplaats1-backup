import pygame
from settings import *
from level import Level
from sys import exit
from screens import Screen
import status
import score

pygame.init()
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SlimePy")
clock = pygame.time.Clock()

start_screen = Screen(screen, "start_screen", "SlimePy", "Play", "Quit")
game_over_screen = Screen(screen, "game_over_screen", "Game Over", "Retry", "Give up")
#finish_screen = Screen(screen, "finish_screen", "Finished!", "Replay", "Quit")
current_screen = start_screen

level_1 = Level(level_1_data, screen)
level_2 = Level(level_2_data, screen)
level_3 = Level(level_3_data, screen)

while True:
    level_status = status.level_status
    current_score = status.current_score

    screen.fill('white')
    pygame.mouse.get_pos()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen.play_button.collidepoint(pygame.mouse.get_pos()):
                status.level_status = 1
                status.current_score = 0
                current_screen = start_screen
                del level_1
                del level_2
                del level_3
                try:
                    del finish_screen
                except:
                    pass
                level_1 = Level(level_1_data, screen)
                level_2 = Level(level_2_data, screen)
                level_3 = Level(level_3_data, screen)
                #print(f"Pressed the Start button. Screen: {current_screen}")
                # if current_screen.screen_type == "start_screen":
                #     print("Play: Start scherm")
                #     status.level_status = 1
                # elif current_screen.screen_type == "game_over_screen":
                #     print("Play: Game Over scherm")
                    # del level_1
                    # level_1 = Level(level_1_data, screen)
                    # status.level_status = 1
            elif current_screen.quit_button.collidepoint(pygame.mouse.get_pos()):
                #print(f"Pressed the Quit button. Screen: {current_screen}")
                pygame.quit()
                exit()
                # if current_screen.screen_type == "start_screen":
                #     print("Quit: Start scherm")
                # elif current_screen.screen_type == "game_over_screen":
                #     print("Quit: Game Over scherm")
           

    if status.level_status == 0:
        current_screen = start_screen
        start_screen.run()
    elif status.level_status == 1:
        level_1.run()
    elif status.level_status == 2:
        level_2.run()
    elif status.level_status == 3:
        level_3.run()
    elif status.level_status == 4:
        try:
            finish_screen.run()
        except:
            data = score.load_json_data('scores.json')
            score.update_scores(status.current_score, data)
            high_score = score.get_high_score(data)
            finish_screen = Screen(screen, "finish_screen", f'HS: {high_score}, YS: {status.current_score}', "Replay", "Quit")
            current_screen = finish_screen

    elif status.level_status == -1:
        current_screen = game_over_screen
        game_over_screen.run()

    pygame.display.update()
    clock.tick(fps)