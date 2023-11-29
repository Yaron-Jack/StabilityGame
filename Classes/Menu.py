import pygame

class Menu:
    def __init__(self, screen, items):
        self.screen = screen
        self.items = items # List of Button objects

    def draw(self):
        for item in self.items:
            item.draw(self.screen)

    def handle_event(self, event):
        for item in self.items:
            if item.handle.event(event):
                return item  # Return the button that was clicked
        return None