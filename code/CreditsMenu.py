import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_DARK_BLUE, COLOR_WHITE, CREDITS, CREDITS_POSITIONS


class CreditsMenu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/CreditsBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)
        self.clock = pygame.time.Clock()

    def run(self, back_selected=True, pos_botao=(782, 462)):

        while True:

            self.clock.tick(60)
            self.window.blit(source=self.surf, dest=self.rect)
            self.credits_text(26, "Save Planet:", COLOR_DARK_BLUE, ((767), 63))
            self.credits_text(26, "Defence Force", COLOR_DARK_BLUE, ((765), 90 ))

            self.credits_text(20, "Credits", COLOR_WHITE, ((767), 163))


            for i in range(len(CREDITS)):
                pos_x, pos_y, text_size = CREDITS_POSITIONS[i]
                self.credits_text(text_size, CREDITS[i], COLOR_WHITE, (pos_x, pos_y))

            if back_selected:
                self.credits_text(23, "Back", COLOR_DARK_BLUE, pos_botao)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        return "menu_principal"  # Retorna o próximo estado do jogo

            pygame.display.flip()


    def credits_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple ):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
