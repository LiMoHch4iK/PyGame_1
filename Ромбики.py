import pygame


def draw(screen):
    screen.fill('yellow')
    for col in range(n):
        for row in range(n):
            if n * (col + 1) < 300 and n * (row + 1) < 300:
                pygame.draw.polygon(screen, 'orange',
                                    [(row * n, col * n + n / 2), (row * n + (n / 2), col * n),
                                     ((row + 1) * n, col * n + n / 2),
                                     (row * n + (n / 2), (col + 1) * n)])

if __name__ == '__main__':
    try:
        n = int(input())
        pygame.init()
        size = width, height = 300, 300
        pygame.display.set_caption('Ромбики')
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
