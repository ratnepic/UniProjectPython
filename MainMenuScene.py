import pygame as pg


class MainMenuScene:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.code = 0

    def open(self):
        screen = self.screen
        screen_width, screen_height = screen.get_size()
        font = pg.font.SysFont('Comic Sans MS', 60)

        title = font.render("SUPER GAME!!!", False, (0, 0, 0))

        play_text = font.render("PLAY", False, (0, 255, 0))
        play_text_rect = pg.Rect((screen_width - play_text.get_width()) / 2, 300,
                                 *play_text.get_rect().size)

        quit_text = font.render("QUIT", False, (255, 0, 0))
        quit_text_rect = pg.Rect((screen_width - quit_text.get_width()) / 2, 400,
                                 *quit_text.get_size())

        while self.running:
            screen.fill((255, 255, 255))

            screen.blit(title, ((screen_width - title.get_width())/2, 70))
            screen.blit(play_text, play_text_rect)
            screen.blit(quit_text, quit_text_rect)

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        if play_text_rect.collidepoint(event.pos):
                            self.move_to_game()
                        elif quit_text_rect.collidepoint(event.pos):
                            self.quit()

    def quit(self):
        self.code = 0
        self.running = False

    def move_to_game(self):
        self.code = 1
        self.running = False
