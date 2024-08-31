import pygame


pygame.init()


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = True

    def draw(self, screen):
        action = False
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()

        #check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, self.rect)

        return action

    def clickTrue(self):
        self.clicked = True
