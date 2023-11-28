import pygame

class Button:
    def __init__(self, image, pos, action=None):
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.action