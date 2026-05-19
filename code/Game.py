import pygame

from code.CreditsMenu import CreditsMenu
from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.OptionsGame import OptionsGame
from code.ScoreScreen import ScoreScreen


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player_score = [0]

                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                # Se level_return for True, ele passou pro Level 2
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    # Após terminar o Level 2 (seja ganhando ou morrendo), mostra a tela de resumo final
                    score_screen = ScoreScreen(self.window, is_victory=level_return, final_score=player_score[0])
                    score_screen.run()
                else:
                    # Se ele perdeu já no Level 1, mostra a tela de Game Over imediatamente
                    score_screen = ScoreScreen(self.window, is_victory=False, final_score=player_score[0])
                    score_screen.run()

            elif menu_return == MENU_OPTION[1]:
                options_menu = OptionsGame(self.window)
                estado_atual = options_menu.run()

            elif menu_return == MENU_OPTION[2]:
                credits_menu = CreditsMenu(self.window)
                estado_atual = credits_menu.run()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()

            else:
                pass