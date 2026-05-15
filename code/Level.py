#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        # Puxa as 4 imagens da Factory de uma vez só
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # Limpa a tela com a cor preta antes de desenhar o frame atual
            self.window.fill((0, 0, 0))

            # Desenha as entidades e faz o movimento
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            clock.tick(60)