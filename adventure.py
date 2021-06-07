#!usr/bin/python3.6

import pygame
import sys
from colors import Colors

# Initializing the game environment
pygame.init()

# Open a new window
window_width = 800
window_height = 600
window_size = (window_width,window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Text Adventure")

# Creating the clock that controls the rate at which the window updates itself
clock = pygame.time.Clock()

# --Global variables--
primary_font = pygame.font.Font(None,60)
secondary_font = pygame.font.Font(None,30)
player_name = ""
is_typing = True
character_limit = 10

# --Functions--
# Function that renders text based on the specifications provided
def renderText(font,message,color,position):
    text = font.render(message,1,color)
    textRect = text.get_rect()
    textRect.center = position
    window.blit(text,textRect)

# Loop that runs until the player enters a name and presses enter
while True:
    # --Main event loop--
    for event in pygame.event.get():
        # If the user did something
        if event.type == pygame.QUIT:
            # If the user voluntarily closes the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # The user can also quit by pressing the ESC key
                pygame.quit()
                sys.exit()
            if is_typing:
                if event.key == pygame.K_RETURN and player_name != "":
                    is_typing = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif len(player_name) < character_limit and event.key != pygame.K_RETURN:
                    player_name += event.unicode

    # --Game logic goes here--

    # --Drawing all the compontents on the screen--
    window.fill(Colors["black"])

    renderText(primary_font,"Enter your name",Colors["white"],(window_width / 2,window_height / 2 - 60))

    renderText(primary_font,player_name,Colors["green"],(window_width / 2,window_height / 2))

    limit_text = str(len(player_name)) + "/" + str(character_limit)
    renderText(secondary_font,limit_text,Colors["white"],(window_width / 2,window_height / 2 + 30))

    # --Updating the screen with whatever has been drawn so far--
    pygame.display.update()

    # Limit the clock to 60 frames per second
    clock.tick(60)

# Stops the game engine after the user has completed the story
pygame.quit()