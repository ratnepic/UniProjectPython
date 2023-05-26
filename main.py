from MainMenuScene import MainMenuScene
from GameScene import GameScene
from GameOverScene import GameOverScene
import pygame as pg


def main():
    pg.init()
    screen_width = 1280
    screen_height = 720
    screen = pg.display.set_mode((screen_width, screen_height))

    running = True
    while running:
        main_menu = MainMenuScene(screen)
        game_scene = GameScene(screen)
        game_over_screen = GameOverScene(screen)

        main_menu.open()

        if main_menu.code == 1:
            game_scene.open()
        elif main_menu.code == 0:
            running = False

        if game_scene.code == 2:
            continue
        elif game_scene.code == 1:
            game_over_screen.open()
        elif game_scene.code == 0:
            running = False

        if game_over_screen.code == 1:
            continue
        elif game_over_screen.code == 0:
            running = False

    pg.quit()


if __name__ == '__main__':
    main()
