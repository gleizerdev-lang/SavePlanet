import pygame.constants

# C
COLOR_WHITE = (255, 255, 255)
COLOR_DARK_BLUE = (33, 57, 74)
COLOR_LIGHT_BLUE = (173, 216, 230)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

CREDITS = [
    "Autor e Desenvolvedor Principal:", " Gleizer Damasceno",
    "Engenharia de Software e Roteiro:", " Gleizer Damasceno",
    "Direção de Arte (Gerada por IA):", " Gleizer Damasceno",
    "Design de Áudio:", " [Indicar Fonte da Música/Efeitos]",
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

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Dust': 0,
    'Planet': 999,
    'Player': 1,
    'PlayerShot': 30,
    'Enemy1': 1,
    'Enemy2': 1,
}

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0.1,
    'Level1Bg1': 0.1,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Dust': 0.7,
    'Planet': 0,
    'Enemy1': 3,
    'Enemy2': 2,
    'Player': 5,
    'PlayerShot': 10
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Dust': 999,
    'Planet': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
}

ENTITY_SHOT_DELAY = {
    'Player': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Planet': 0,
    'Player': 0,
    'Dust': 0,
    'PlayerShot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
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

# P
PLAYER_KEY_SHOOT = {
    'Player': pygame.K_UP
}
PLAYER_HIT_DAMAGE = 100
PLANET_HIT_DAMAGE = 30

# S
SPAWN_TIME = 4000

# T
TIMEOUT_LEVEL = 20000
TIMEOUT_STEP = 100


# W
WIN_WIDTH = 917
WIN_HEIGHT = 514

CURRENT_DIFFICULTY = "Medium"

CURRENT_DIFFICULTY = "Medium"

def update_difficulty(difficulty_level: str):
    global SPAWN_TIME, PLAYER_HIT_DAMAGE, PLANET_HIT_DAMAGE
    global ENTITY_HEALTH, ENTITY_SPEED, ENTITY_SHOT_DELAY, CURRENT_DIFFICULTY

    CURRENT_DIFFICULTY = difficulty_level

    if difficulty_level == "Easy":
        SPAWN_TIME = 4000
        PLAYER_HIT_DAMAGE = 50
        PLANET_HIT_DAMAGE = 10
        ENTITY_HEALTH['Enemy1'] = 30
        ENTITY_HEALTH['Enemy2'] = 40
        ENTITY_SPEED['Enemy1'] = 2
        ENTITY_SPEED['Enemy2'] = 1
        ENTITY_SPEED['Player'] = 5
        ENTITY_SHOT_DELAY['Player'] = 15

    elif difficulty_level == "Medium":
        SPAWN_TIME = 2500
        PLAYER_HIT_DAMAGE = 100
        PLANET_HIT_DAMAGE = 30
        ENTITY_HEALTH['Enemy1'] = 50
        ENTITY_HEALTH['Enemy2'] = 60
        ENTITY_SPEED['Enemy1'] = 3
        ENTITY_SPEED['Enemy2'] = 2
        ENTITY_SPEED['Player'] = 6
        ENTITY_SHOT_DELAY['Player'] = 12

    elif difficulty_level == "Hard":
        SPAWN_TIME = 1000
        PLAYER_HIT_DAMAGE = 150
        PLANET_HIT_DAMAGE = 50
        ENTITY_HEALTH['Enemy1'] = 100
        ENTITY_HEALTH['Enemy2'] = 120
        ENTITY_SPEED['Enemy1'] = 5
        ENTITY_SPEED['Enemy2'] = 4
        ENTITY_SPEED['Player'] = 8
        ENTITY_SHOT_DELAY['Player'] = 9

    elif difficulty_level == "Very Hard":
        SPAWN_TIME = 500
        PLAYER_HIT_DAMAGE = 300
        PLANET_HIT_DAMAGE = 100
        ENTITY_HEALTH['Enemy1'] = 150
        ENTITY_HEALTH['Enemy2'] = 200
        ENTITY_SPEED['Enemy1'] = 7
        ENTITY_SPEED['Enemy2'] = 6
        ENTITY_SPEED['Player'] = 10
        ENTITY_SHOT_DELAY['Player'] = 6
