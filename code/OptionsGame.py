import pygame
import sys  # Import necessário para fechar o programa de forma limpa

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_DARK_BLUE, COLOR_WHITE, CREDITS, OPTION_GAME, OPTION_GAME_POSITIONS, COLOR_LIGHT_BLUE


class OptionsGame:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/OptionsBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)
        self.clock = pygame.time.Clock()  # Cria o controlador de FPS

    def run(self):
        option_game = 0
        while True:

            # 1. Limita o loop a 60 frames por segundo (evita gastar CPU)
            self.clock.tick(60)
            self.window.blit(source=self.surf, dest=self.rect)
            self.options_game_text(26, "Save Planet:", COLOR_DARK_BLUE, ((767), 63))
            self.options_game_text(26, "Defence Force", COLOR_DARK_BLUE, ((765), 90 ))

            self.options_game_text(22, "SELECT DIFFICULTY", COLOR_LIGHT_BLUE, ((768), 165))

            # O laço agora desempacota três valores e passa para a sua função
            for i in range(len(OPTION_GAME)):
                pos_x, pos_y, text_size = OPTION_GAME_POSITIONS[i]
                self.options_game_text(text_size, OPTION_GAME[i], COLOR_WHITE, (pos_x, pos_y))


            for i in range(len(OPTION_GAME)):
                posicao = OPTION_GAME[i]

                if i == option_game:
                    pos_x, pos_y, text_size = OPTION_GAME_POSITIONS[i]
                    self.options_game_text(text_size, OPTION_GAME[i], COLOR_DARK_BLUE, (pos_x, pos_y))

                else:
                    pos_x, pos_y, text_size = OPTION_GAME_POSITIONS[i]
                    self.options_game_text(text_size, OPTION_GAME[i], COLOR_WHITE, (pos_x, pos_y))




            # 4. Atualiza a tela de fato para o jogador ver
            pygame.display.flip()

            # 2. Captura de eventos do teclado/mouse/janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if option_game < len(OPTION_GAME) -1:
                            option_game += 1
                        else:
                            option_game = 0

                    if event.key == pygame.K_UP:
                        if option_game > 0:
                            option_game -= 1
                        else:
                            option_game = len(OPTION_GAME) -1

                        if event.key == pygame.K_RETURN:
                            pass







    def options_game_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple ):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



