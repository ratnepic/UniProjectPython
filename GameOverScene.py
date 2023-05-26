import pygame as pg


class GameOverScene:
    def __init__(self, screen):
        self.screen = screen
        self.code = 0
        self.running = True

    def open(self):
        font = pg.font.SysFont('Comic Sans MS', 60)

        game_over_text = font.render('GAME OVER!', False, (0, 0, 0))
        game_over_rect = pg.Rect(
            (self.screen.get_width() - game_over_text.get_width())/2, 200,
            *game_over_text.get_size()
        )

        quit_text = font.render('QUIT', False, (255, 0, 0))
        quit_text_rect = pg.Rect(
            (self.screen.get_width() - quit_text.get_width())/2, 300,
            *quit_text.get_size()
        )

        while self.running:
            self.screen.fill((255, 255, 255))

            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(quit_text, quit_text_rect)

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        if quit_text_rect.collidepoint(event.pos):
                            self.quit_to_menu()

    def quit_to_menu(self):
        self.code = 1
        self.running = False

    def quit(self):
        self.code = 0
        self.running = False
