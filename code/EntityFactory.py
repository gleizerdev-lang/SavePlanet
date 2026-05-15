#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []

                # 1. Desenha o fundo normal
                for i in range(2):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))

                # 2. Desenha a Poeira Cósmica em loop
                list_bg.append(Background('Dust', (0, 0)))
                list_bg.append(Background('Dust', (0, WIN_HEIGHT)))

                # 3. Desenha o Planeta por cima de tudo
                list_bg.append(Background('Planet', (130, 245)))

                return list_bg