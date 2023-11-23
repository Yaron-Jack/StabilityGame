import pygame
import sys

pygame.init()

# Screen dimensions

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

# Load icon image
icon = pygame.image.load("Assests\Graphics\icons\icon32.png")

# Set icon
pygame.display.set_icon(icon)


# Title of of the window

pygame.display.set_caption('Stability: tense horizons')

# Main menu background image load
background_image = pygame.image.load("Assests\Graphics\Menu\BackgroundSoilders.png")

# Main loop flag

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Displaying background image:

    screen.blit(background_image, (0, 0))

    # Update display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()