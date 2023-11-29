import pygame
import sys
from Classes.Menu import Menu
from Classes.Button import Button


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

# Title menu background image load
title_menu_image = pygame.image.load("Assests\Graphics\Menu\TitleMenuEmpty1024.png")

# Title menu buttons:
titleButtonWidth = 130
titleButtonHeight = 60
start_game_button = Button(151, 480, 'Assests/Graphics/Menu/TitleMenuButtons/StartGame.png', width=titleButtonWidth, height=titleButtonHeight)
load_game_button = Button(351, 480, 'Assests/Graphics/Menu/TitleMenuButtons/LoadGame.png', width=titleButtonWidth, height=titleButtonHeight)
options_button = Button(551, 480, 'Assests/Graphics/Menu/TitleMenuButtons/Options.png', width=titleButtonWidth, height=titleButtonHeight)
exit_game_button = Button(751, 480, 'Assests/Graphics/Menu/TitleMenuButtons/ExitGame.png', width=titleButtonWidth, height=titleButtonHeight)

# Title menu Navigation
title_menu = Menu(screen, [start_game_button, load_game_button, options_button, exit_game_button])

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
        # TODO: menu functionality
        # TODO: Title navigation bar


        screen.blit(title_menu_image, (0, 0))   # Clear the screen, redraw background image
        title_menu.draw()
        pygame.display.flip()








    if game_state == GAME_PLAY: # If the player is in the Game play state
        screen.blit(title_menu_image, (0,0))
        #TODO: This is where the gameplay functionality will come in




    # Update display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()