from HandTrack import HandTracker
from HandSprite import HandSprite
from NoteSprite import NoteSprite
from TimerSprite import TimerSprite
import pygame as pg
from random import randint


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.ht = HandTracker()
        self.code = 0
        self.score = 0
        self.running = True

    def open(self):
        self.score = 0
        clock = pg.time.Clock()
        timer_sprite = TimerSprite((self.screen.get_width(), 20))
        hand_status_p = [False, False]

        all_sprites_group = pg.sprite.Group()
        all_sprites_group.add(timer_sprite)
        hands_group = pg.sprite.Group()
        notes_group = pg.sprite.Group()

        add_note_event = pg.USEREVENT + 1
        pg.time.set_timer(add_note_event, 1500)

        font = pg.font.SysFont('Comic Sans MS', 45)

        while self.running:
            self.screen.fill((255, 255, 255))

            score_text = font.render(str(self.score), False, (0, 0, 0))
            score_x = self.screen.get_width() - score_text.get_width() - 20
            score_y = 60
            self.screen.blit(score_text,  (score_x, score_y))

            hands = self.ht.get_hand_coords()
            if hands:
                for i, hand in enumerate(hands):
                    x, y, status = hand
                    x *= self.screen.get_size()[0]
                    y *= self.screen.get_size()[1]
                    color = (0, 255, 0) if status else (255, 0, 0)

                    if status and not hand_status_p[i]:
                        hand_sprite = HandSprite((x, y), 10)
                        all_sprites_group.add(hand_sprite)
                        hands_group.add(hand_sprite)
                        hand_status_p[i] = True

                    elif not status:
                        hand_status_p[i] = False

                    pg.draw.circle(self.screen, color, (x, y), 50, 3)

            if timer_sprite.timer <= 0:
                self.game_over()

            for note in notes_group:
                if pg.sprite.spritecollideany(note, hands_group):
                    print("collision")
                    note.kill()
                    self.score += 10
                    timer_sprite.add_time(1.6)

            for sprite in all_sprites_group:
                self.screen.blit(sprite.serf, sprite.rect)
                sprite.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit_to_menu()

                elif event.type == pg.QUIT:
                    self.quit()

                elif event.type == add_note_event:
                    x = randint(150, self.screen.get_width()-150)
                    y = randint(100, self.screen.get_height()-100)
                    note_sprite = NoteSprite((x, y), 50, 3)
                    all_sprites_group.add(note_sprite)
                    notes_group.add(note_sprite)

            pg.display.flip()
            clock.tick(60)

    def quit_to_menu(self):
        self.code = 2
        self.running = False

    def quit(self):
        self.code = 0
        self.running = False

    def game_over(self):
        self.code = 1
        self.running = False
