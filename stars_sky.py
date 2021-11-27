import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/star_50.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def stars_sky(self):
        pygame.init()

        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen_rect = screen.get_rect()
        screen_width = screen.get_rect().width
        screen_height = screen.get_rect().height
        pygame.display.set_caption("Звездное небо")
        screen.fill('black')
        #image = pygame.image.load('images/star_50.png')
        #rect = image.get_rect()
        #rect.x = rect.width
        #rect.y = rect.height
        stars = pygame.sprite.Group()

        star = Star()
        star_width, star_height = star.rect.size
        available_space_x = screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)

        available_space_y = (screen_height - star_height)
        number_rows = available_space_y // (2 * star_width)

        for row_number in range(randint(0, number_rows)):
            for star_number in range(randint(0, number_star_x)):
                star = Star()
                star_width, star_height = star.rect.size
                star.x = (star_width + 2 * star_width * star_number)
                #star.x = randint(0, screen_rect.right - star_width)
                star.rect.x = star.x
                #star.rect.y = randint(0, screen_rect.bottom - star_height)
                star.rect.y = (star.rect.height + 2 * star.rect.height * row_number)
                stars.add(star)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            screen.blit(self.image, self.rect)
            stars.draw(screen)
            pygame.display.flip()


game = Star()
game.stars_sky()
