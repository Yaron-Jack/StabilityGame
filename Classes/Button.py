import pygame


class Button:
    def __init__(self, x, y, image_path, width=None, height=None, hover_image_path=None, callback=None):
        # Load the image
        self.original_image = pygame.image.load(image_path)

        # Resize if width and height are provided
        if width and height:
            self.image = pygame.transform.scale(self.original_image, (width, height))
        else:
            self.image = self.original_image

        # Do the same for the hover image if provided
        self.hover_image = None
        if hover_image_path:
            self.original_hover_image = pygame.image.load(hover_image_path)
            if width and height:
                self.hover_image = pygame.transform.scale(self.original_hover_image, (width, height))
            else:
                self.hover_image = self.original_hover_image

        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback
        self.hovered = False

    def draw(self, screen):
        if self.hovered and self.hover_image:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and self.callback:
                self.callback()
                return True
        return False
