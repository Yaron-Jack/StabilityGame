import pygame
from .Button import Button
'''
This class is for creating a dynamic menu. This class
will be used to create various menus through out the project
'''

class Menu:
    def __init__(self, screen, background, button_data, text_elements=None):
        self.screen = screen
        self.background = background
        self.buttons = self.create_buttons(button_data)
        self.text_elements = text_elements or []

    def create_buttons(self, button_data):
        buttons = []
        for data in button_data:
            image = pygame.image.load(data['image_path'])
            button = Button(image, data['position'], data['action'])
            buttons.append(button)
        return buttons

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    button.action()

    def draw(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        # Draw buttons
        for button in self.buttons:
            button.draw(self.screen)

        # Draw text on button
        for text_on_button in self.text_elements:
            # Render and draw text elements
            pass

'''
Example usage:

pygame.init()
screen = pygame.display.set_mode((800, 600))

background_image = pygame.image.load('path/background.png')

main_menu_button_data = [
    {'image_path': 'path/folder/startButton.png', 'position':(100,100), 'action': some_start_function}
    {'image_path': 'path/to/exit_button.png', 'position': (100, 200), 'action': some_exit_function}
    ]

main_menu = Menu(screen, background_image, button_data)
'''



