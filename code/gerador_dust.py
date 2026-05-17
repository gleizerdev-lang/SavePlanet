import pygame
import random
import math

WIN_WIDTH = 917
WIN_HEIGHT = 514

pygame.init()

imagem_poeira = pygame.Surface(
    (WIN_WIDTH, WIN_HEIGHT),
    pygame.SRCALPHA
)

DENSIDADE = 0.70

# margem vertical
MARGEM_TOPO = 28
MARGEM_BAIXO = 28

def qtd(valor):
    return max(1, int(valor * DENSIDADE))



def criar_nuvem(
    raio,
    cor,
    alpha_max,
    expoente=3
):

    surf = pygame.Surface(
        (raio * 2, raio * 2),
        pygame.SRCALPHA
    )

    centro = raio

    for x in range(raio * 2):
        for y in range(raio * 2):

            dx = x - centro
            dy = y - centro

            distancia = math.sqrt(dx * dx + dy * dy)

            if distancia < raio:

                d = distancia / raio

                fade = (1 - d) ** expoente

                fade *= 0.98

                alpha = int(alpha_max * fade)

                surf.set_at(
                    (x, y),
                    (*cor, alpha)
                )

    return surf

def gerar_y_seguro(raio):

    return random.randint(
        MARGEM_TOPO + raio // 3,
        WIN_HEIGHT - MARGEM_BAIXO - raio // 3
    )


for _ in range(qtd(18)):

    raio = random.randint(150, 320)

    x = random.randint(0, WIN_WIDTH)

    y = gerar_y_seguro(raio)

    tom = random.randint(100, 170)

    cor = (
        tom,
        tom,
        tom + 15
    )

    alpha = random.randint(5, 14)

    nuvem = criar_nuvem(
        raio,
        cor,
        alpha,
        expoente=4.8
    )

    imagem_poeira.blit(
        nuvem,
        (x - raio, y - raio),
        special_flags=pygame.BLEND_ALPHA_SDL2
    )


for _ in range(qtd(24)):

    centro_x = random.randint(0, WIN_WIDTH)

    centro_y = gerar_y_seguro(140)

    for _ in range(qtd(7)):

        raio = random.randint(90, 220)

        x = centro_x + random.randint(-150, 150)

        y = centro_y + random.randint(-120, 120)

        tom = random.randint(150, 210)

        cor = (
            tom,
            tom,
            tom + 5
        )

        alpha = random.randint(10, 30)

        nuvem = criar_nuvem(
            raio,
            cor,
            alpha,
            expoente=3.7
        )

        imagem_poeira.blit(
            nuvem,
            (x - raio, y - raio),
            special_flags=pygame.BLEND_ALPHA_SDL2
        )


for _ in range(qtd(40)):

    centro_x = random.randint(0, WIN_WIDTH)

    centro_y = gerar_y_seguro(90)

    for _ in range(qtd(8)):

        raio = random.randint(50, 140)

        x = centro_x + random.randint(-100, 100)

        y = centro_y + random.randint(-100, 100)

        tom = random.randint(180, 240)

        cor = (
            tom,
            tom,
            tom
        )

        alpha = random.randint(18, 42)

        nuvem = criar_nuvem(
            raio,
            cor,
            alpha,
            expoente=3
        )

        imagem_poeira.blit(
            nuvem,
            (x - raio, y - raio),
            special_flags=pygame.BLEND_ALPHA_SDL2
        )


for _ in range(qtd(90)):

    raio = random.randint(20, 70)

    x = random.randint(0, WIN_WIDTH)

    y = gerar_y_seguro(raio)

    tom = random.randint(220, 255)

    cor = (
        tom,
        tom,
        tom
    )

    alpha = random.randint(25, 60)

    nuvem = criar_nuvem(
        raio,
        cor,
        alpha,
        expoente=2.3
    )

    imagem_poeira.blit(
        nuvem,
        (x - raio, y - raio),
        special_flags=pygame.BLEND_ALPHA_SDL2
    )


for _ in range(qtd(220)):

    raio = random.randint(8, 26)

    x = random.randint(0, WIN_WIDTH)

    y = gerar_y_seguro(raio)

    tom = random.randint(220, 255)

    alpha = random.randint(12, 45)

    nuvem = criar_nuvem(
        raio,
        (tom, tom, tom),
        alpha,
        expoente=2
    )

    imagem_poeira.blit(
        nuvem,
        (x - raio, y - raio),
        special_flags=pygame.BLEND_ALPHA_SDL2
    )


for _ in range(qtd(1200)):

    x = random.randint(0, WIN_WIDTH)

    y = random.randint(
        6,
        WIN_HEIGHT - 6
    )

    brilho = random.randint(180, 255)

    tamanho = random.randint(1, 2)

    alpha = random.randint(8, 70)

    pygame.draw.circle(
        imagem_poeira,
        (
            brilho,
            brilho,
            brilho,
            alpha
        ),
        (x, y),
        tamanho
    )


for _ in range(qtd(50)):

    x = random.randint(0, WIN_WIDTH)

    y = random.randint(
        30,
        WIN_HEIGHT - 30
    )

    largura = random.randint(120, 280)

    altura = random.randint(20, 60)

    surf = pygame.Surface(
        (largura, altura),
        pygame.SRCALPHA
    )

    for i in range(altura):

        fade = (
            1 -
            abs(i - altura / 2) / (altura / 2)
        )

        alpha = int(22 * fade)

        pygame.draw.line(
            surf,
            (255, 255, 255, alpha),
            (0, i),
            (largura, i)
        )

    angulo = random.randint(-35, 35)

    surf = pygame.transform.rotate(
        surf,
        angulo
    )

    imagem_poeira.blit(
        surf,
        (
            x - surf.get_width() // 2,
            y - surf.get_height() // 2
        ),
        special_flags=pygame.BLEND_ALPHA_SDL2
    )


mini = pygame.transform.smoothscale(
    imagem_poeira,
    (WIN_WIDTH // 2, WIN_HEIGHT // 2)
)

blur = pygame.transform.smoothscale(
    mini,
    (WIN_WIDTH, WIN_HEIGHT)
)

imagem_poeira.blit(
    blur,
    (0, 0),
    special_flags=pygame.BLEND_ALPHA_SDL2
)


fade_surface = pygame.Surface(
    (WIN_WIDTH, WIN_HEIGHT),
    pygame.SRCALPHA
)

for y in range(WIN_HEIGHT):

    alpha = 255

    if y < MARGEM_TOPO:

        alpha = int(
            255 * (y / MARGEM_TOPO)
        )

    elif y > WIN_HEIGHT - MARGEM_BAIXO:

        distancia = WIN_HEIGHT - y

        alpha = int(
            255 * (distancia / MARGEM_BAIXO)
        )

    pygame.draw.line(
        fade_surface,
        (255, 255, 255, alpha),
        (0, y),
        (WIN_WIDTH, y)
    )

imagem_poeira.blit(
    fade_surface,
    (0, 0),
    special_flags=pygame.BLEND_RGBA_MULT
)

pygame.image.save(
    imagem_poeira,
    "../asset/Dust.png"
)

print(f"Dust.png gerado com densidade {DENSIDADE * 100:.0f}%")

pygame.quit()