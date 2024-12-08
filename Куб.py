import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    color = pygame.Color(250, 0, 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] - Hue, hsv[3])
    pygame.draw.polygon(screen, color, [(300 / 3 + W / 2, 300 / 2 - W / 2), (300 / 3 + W + W / 2, 300 / 2 - W / 2),
                                           (300 / 3 + W, 300 / 2), (300 / 3, 300 / 2)])
    color.hsva = (hsv[0], hsv[1], (hsv[2] - Hue) * 0.75, hsv[3])
    screen.fill(pygame.Color(color), pygame.Rect(300 / 3, 300 / 2, W, W))
    color.hsva = (hsv[0], hsv[1], (hsv[2] - Hue) * 0.5, hsv[3])
    pygame.draw.polygon(screen, color, [(300 / 3 + W, 300 / 2), (300 / 3 + W + W / 2, 300 / 2 - W / 2),
                                           (300 / 3 + W + W / 2, 300 / 2 + W / 2), (300 / 3 + W, 300 / 2 + W)])


if __name__ == '__main__':
    try:
        W, Hue = map(int, input().split())
        pygame.init()
        size = width, height = 300, 300
        pygame.display.set_caption('Куб')
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
