import pygame


def draw(screen):
    screen.fill('white')
    for col in range(200 // 15):
        for row in range(300 // 30):
            if col % 2 == 0:
                pygame.draw.rect(screen, 'red', (a * row + row * 2, b * col + col * 2, a, b))
            else:
                pygame.draw.rect(screen, 'red', (a * row + row * 2 - 15, b * col + col * 2, a, b))


if __name__ == '__main__':
    try:
        a, b = 30, 15
        pygame.init()
        size = width, height = 300, 200
        pygame.display.set_caption('Кирпичи')
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
