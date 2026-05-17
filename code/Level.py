
import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        # Puxa as 4 imagens da Factory de uma vez só
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 2000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):

        pygame.mixer_music.fadeout(500)
        pygame.mixer_music.load("./asset/Level1.mp3")
        pygame.mixer_music.play(loops=-1, fade_ms=2000)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.fill((0, 0, 0))

            # Desenha as entidades e faz o movimento
            for ent in self.entity_list:
                ent.move()

            for ent in self.entity_list:
                if ent.name != 'Player':
                    self.window.blit(source=ent.surf, dest=ent.rect)

            for ent in self.entity_list:
                if ent.name == 'Player':
                    self.window.blit(source=ent.surf, dest=ent.rect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))

                    self.entity_list.append(
                        EntityFactory.get_entity(choice)
                    )

            # printed text
            self.level_text(
                text_size=14,
                text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                text_color=COLOR_WHITE,
                text_pos=(10, 5)
            )

            self.level_text(
                text_size=14,
                text=f'fps: {clock.get_fps() :.0f}',
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 35)
            )

            self.level_text(
                text_size=14,
                text=f'entidades: {len(self.entity_list)}',
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()

    def level_text(self, text_size: int, text: str,
                   text_color: tuple, text_pos: tuple):

        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter",
            size=text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            left=text_pos[0],
            top=text_pos[1]
        )

        self.window.blit(
            source=text_surf,
            dest=text_rect
        )