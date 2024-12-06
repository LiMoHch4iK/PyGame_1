import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    rect = 300 / (2 * n)
    for i in range(n):
        ellipse_rect_y = (0, rect * i), (300, 300 - (rect * i * 2))
        ellipse_rect_x = (rect * i, 0), (300 - (rect * i * 2), 300)
        pygame.draw.ellipse(screen, 'white', ellipse_rect_y, width=1)
        pygame.draw.ellipse(screen, 'white', ellipse_rect_x, width=1)


if __name__ == '__main__':
    n = int(input())
    pygame.init()
    size = width, height = 300, 300
    pygame.display.set_caption('Сфера')
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
# except Exception:
#     print('Неправильный формат ввода')
