#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib2to3.pytree import convert
from pydoc import source_synopsis
from xml.dom.expatbuilder import TEXT_NODE

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_DARK_BLUE, MENU_POSITIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        if not pygame.mixer_music.get_busy():
            pygame.mixer_music.load("./asset/menu.mp3")
            pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(26, "Save Planet:", COLOR_DARK_BLUE, ((767), 63))
            self.menu_text(26, "Defence Force", COLOR_DARK_BLUE, ((765), 90 ))

            for i in range(len(MENU_OPTION)):
                pos_x, pos_y = MENU_POSITIONS[i]
                self.menu_text(23, MENU_OPTION[i], COLOR_WHITE, (pos_x, pos_y))

            self.menu_text(16, "MISSION BRIEFING", COLOR_WHITE, ((767), 436))
            self.menu_text(11, "Destroy incoming alien waves. Do not", COLOR_WHITE, ((769), 455))
            self.menu_text(11, "let them breach the atmosphere.", COLOR_WHITE, ((769), 468))

            for i in range(len(MENU_OPTION)):
                # Obtém a posição (x, y) pré-definida para este índice
                posicao = MENU_POSITIONS[i]

                if i == menu_option:
                    # Texto em destaque (selecionado)
                    self.menu_text(23, MENU_OPTION[i], COLOR_DARK_BLUE, posicao)
                else:
                    # Texto normal
                    self.menu_text(23, MENU_OPTION[i], COLOR_WHITE, posicao)


            pygame.display.flip()

            # # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()  # close window
                     quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY - PARA BAIXO
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY - PARA cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple ):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
