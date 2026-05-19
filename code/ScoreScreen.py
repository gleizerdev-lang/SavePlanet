import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_GREEN


class ScoreScreen:
    def __init__(self, window, is_victory: bool, final_score: int):
        self.window = window
        self.is_victory = is_victory
        self.final_score = final_score
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.mixer_music.fadeout(500)

        while True:
            self.clock.tick(60)
            self.window.fill((0, 0, 0))

            if self.is_victory:
                title_text = "MISSION ACCOMPLISHED"
                title_color = COLOR_GREEN
            else:
                title_text = "GAME OVER"
                title_color = (255, 50, 50)

            # Textos da tela de pontuação final
            self.score_text(40, title_text, title_color, (WIN_WIDTH // 2, 150))
            self.score_text(28, f"Final Score: {self.final_score}", COLOR_WHITE, (WIN_WIDTH // 2, 250))
            self.score_text(16, "Press ENTER to return to Main Menu", (150, 150, 150), (WIN_WIDTH // 2, 400))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

