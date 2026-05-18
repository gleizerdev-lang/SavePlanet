import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.y_f = float(self.rect.y)

        if self.name == 'Planet':
            # --- CORREÇÃO 1: Preparação da Imagem (Initialization) ---

            # É crucial chamar .convert_alpha() na imagem base.
            # Isso prepara a transparência do PNG para trabalhar corretamente
            # com os algoritmos matemáticos de rotação e suavização do Pygame.
            # Sem isso, as bordas ficam terríveis ao girar.
            try:
                self.original_surf = self.surf.convert_alpha()
            except pygame.error:
                # Caso o display ainda não tenha sido inicializado (incomum aqui)
                self.original_surf = self.surf
                print("Aviso: Não foi possível converter a imagem do Planeta para Alpha.")

            self.angle = 0.0
            self.center_x_f = float(self.rect.centerx)
            self.center_y_f = float(self.rect.centery)

    def move(self):

        if self.name != 'Planet':
            self.y_f -= ENTITY_SPEED[self.name]
            self.rect.y = int(self.y_f)
            if self.rect.bottom <= 0:
                self.rect.y = WIN_HEIGHT
                self.y_f = float(WIN_HEIGHT)

        else:
            # Movimento vertical sutil
            self.center_y_f -= ENTITY_SPEED[self.name]
            if self.rect.bottom <= 0:
                self.center_y_f = WIN_HEIGHT + (self.rect.height / 2)

            # Rotação sutil
            self.angle += 0.05
            if self.angle >= 360.0:
                self.angle = 0.0

            if self.angle < 0.01:
                self.surf = self.original_surf
            else:
                self.surf = pygame.transform.rotozoom(self.original_surf, self.angle, 1.0)

            self.rect = self.surf.get_rect(center=(self.center_x_f, self.center_y_f))
