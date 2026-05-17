import pygame.constants


# C
COLOR_WHITE =  (255,255,255)
COLOR_DARK_BLUE = (33, 57, 74)
COLOR_LIGHT_BLUE = (173, 216, 230)

CREDITS = [
    "Autor e Desenvolvedor Principal:"," Gleizer Damasceno",
    "Engenharia de Software e Roteiro:"," Gleizer Damasceno",
    "Direção de Arte (Gerada por IA):"," Gleizer Damasceno",
    "Design de Áudio:"," [Indicar Fonte da Música/Efeitos]",
    "Save Planet - 2026"
]

CREDITS_POSITIONS = [
    (770, 228, 11),
    (770, 243, 11),
    (770, 268, 11),
    (770, 283, 11),
    (770, 308, 11),
    (770, 323, 11),
    (770, 348, 11),
    (770, 363, 11),
    (770, 398, 11)
]

# E
EVENT_ENEMY = pygame.USEREVENT +1

ENTITY_SPEED = {
    'Level1Bg0': 0.1,
    'Level1Bg1': 0.1,
    'Dust': 0.7,
    'Planet': 0,
    'Enemy1': 3,
    'Enemy2': 2,
    'Player': 5
}


# M

MENU_OPTION = ('Start',
               'Options',
               'Credits',
               'Exit'
                )


MENU_POSITIONS = [
    (790, 192),
    (790, 248),
    (790, 307),
    (790, 366),
]


# O

OPTION_GAME = ["Easy",
               "Medium",
               "Hard",
               "Very Hard",
               "Back"
]

OPTION_GAME_POSITIONS = [
    (790, 225, 23),
    (790, 282, 23),
    (790, 339, 23),
    (790, 398, 23),
    (790, 455, 23)
]

SPAWN_TIME = 4000

# W
WIN_WIDTH = 917
WIN_HEIGHT = 514

