#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame  # importa o pygame

from code.CreditsMenu import CreditsMenu
from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.OptionsGame import OptionsGame


class Game:
    def __init__(self):
        pygame.init()  # inicia o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[1]:
                options_menu = OptionsGame(self.window)
                estado_atual = options_menu.run()

            elif menu_return == MENU_OPTION[2]:
                credits_menu = CreditsMenu(self.window)  # Cria o objeto com a janela
                estado_atual = credits_menu.run()  # CHAME COM c MINÚSCULO AQUI


            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # close window
                quit()  # end pygame

            else:
                pass




