import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(2): #level1Bg-images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
                list_bg.append(Background('Dust', (0, 0)))
                list_bg.append(Background('Dust', (0, WIN_HEIGHT)))
                list_bg.append(Background('Planet', (146, 225)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(2): #level2Bg-images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (0, WIN_HEIGHT)))
                list_bg.append(Background('Dust', (0, 0)))
                list_bg.append(Background('Dust', (0, WIN_HEIGHT)))
                list_bg.append(Background('Planet', (146, 225)))
                return list_bg


            case 'Enemy1':
                enemy = Enemy('Enemy1', (random.randint(60, WIN_WIDTH - 60), -60))
                return enemy

            case 'Enemy2':
                enemy = Enemy('Enemy2', (random.randint(60, WIN_WIDTH - 60), -60))
                return enemy

            case 'Player':
                return Player('Player', (419, 374))

            case _:
                raise ValueError(f'Entidade não encontrada: {entity_name}')
