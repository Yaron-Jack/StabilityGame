import pygame
import sys
from Classes import Menu, Button

pygame.init()

# Screen dimensions

screen_width, screen_height = 1024, 565

screen = pygame.display.set_mode((screen_width, screen_height))

# Load icon image
icon = pygame.image.load("Assests\Graphics\icons\icon32.png")

# Set icon
pygame.display.set_icon(icon)


# Title of of the window

pygame.display.set_caption('Stability: tense horizons')

# Main menu background image load
title_menu_image = pygame.image.load("Assests\Graphics\Menu\TitleMenuEmpty1024.png")


# Game states
TITLE_MENU, GAME_PLAY, SETTINGS_MENU = range(3)

# Current game states
game_state = TITLE_MENU

# Main loop flag

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == TITLE_MENU: # If the player in the Title menu
        # Title menu functionality

        screen.blit(title_menu_image, (0, 0)) # Drawing background image




    if game_state == GAME_PLAY: # If the player is in the Game play state
        screen.blit(title_menu_image, (0,0))
        #TODO: This is where the gameplay functionality will come in




    # Update display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()