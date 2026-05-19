import sys
import random
from traceback import format_list

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Enemy import Enemy
from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        # Puxa as imagens da Factory de uma vez só
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            for ent in self.entity_list:
                if ent.name != 'Player':
                    self.window.blit(source=ent.surf, dest=ent.rect)

            for ent in self.entity_list:
                if ent.name == 'Player':
                    self.window.blit(source=ent.surf, dest=ent.rect)

            # Loop de Eventos do Sistema
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(
                        EntityFactory.get_entity(choice)
                    )

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        return True

            # Lógica de Sobrevivência (Verifica se o Player ainda existe na lista)
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player) and ent.name == 'Player':
                    found_player = True
                    # Atualiza o score constantemente para não perdê-lo ao morrer
                    player_score[0] = ent.score

            # Se o jogador sumiu da lista (morreu por falta de health), encerra a fase como Derrota
            if not found_player:
                return False

            # Renderização de textos na interface (HUD)
            for ent in self.entity_list:
                if ent.name == 'Player':
                    self.level_text(14, f'Player Heath: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))

            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))

            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # Processamento de colisões e checagem de integridade de vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

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