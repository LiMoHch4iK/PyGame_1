import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    size = 2 * w * n
    color = {0: 'red',
             1: 'blue',
             2: 'green'
             }
    for i in range(n):
        pygame.draw.circle(screen, color[i % 3], ((size / 2), (size / 2)), w * (n - i))


if __name__ == '__main__':
    try:
        w, n = map(int, input().split())
        pygame.init()
        width = 2 * w * n
        height = 2 * w * n
        size = width, height = width, height
        pygame.display.set_caption('Мишень')
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
