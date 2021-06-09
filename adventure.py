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
def renderText(surface,font,message,color,position):
    text = font.render(message,1,color)
    textRect = text.get_rect()
    textRect.center = position
    surface.blit(text,textRect)

# Function that renders a button
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        # If the cursor hovers over the button, it is made active by appropriately changing its colors
        pygame.draw.rect(window,ac,(x,y,w,h))
        renderText(window,primary_font,msg,ic,(x + (w / 2),y + (h / 2)))

        if click[0]:
            # If the button is clicked
            return True
    else:
        pygame.draw.rect(window,ic,(x,y,w,h))
        renderText(window,primary_font,msg,ac,(x + (w / 2),y + (h / 2)))

    return False

# Function that displays the character naming screen
def enterName():
    global is_typing,player_name

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

                        confirmed = confirmName()
                        if confirmed:
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif len(player_name) < character_limit and event.key != pygame.K_RETURN:
                        player_name += event.unicode

        # --Game logic goes here--
        if not is_typing:
            break

        # --Drawing all the compontents on the screen--
        window.fill(Colors["black"])

        renderText(window,primary_font,"Enter your name",Colors["white"],(window_width / 2,window_height / 2 - 60))

        renderText(window,primary_font,player_name,Colors["green"],(window_width / 2,window_height / 2))

        limit_text = str(len(player_name)) + "/" + str(character_limit)
        renderText(window,secondary_font,limit_text,Colors["white"],(window_width / 2,window_height / 2 + 30))

        if len(player_name) > 0:
            renderText(window,secondary_font,"Press \'ENTER\' to proceed",Colors["white"],(window_width / 2,window_height / 2 + 60))

        # --Updating the screen with whatever has been drawn so far--
        pygame.display.update()

        # Limit the clock to 60 frames per second
        clock.tick(60)

# Function that confirms the name entered
def confirmName():
    global is_typing,player_name

    option1 = False
    option2 = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user voluntarily closes the window
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                if event.key == pygame.K_n:
                    is_typing = True
                    player_name = ""
                    return False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if option1:
            # If the player confirms their name
            return True

        if option2:
            # If the player denies their name
            is_typing = True
            player_name = ""
            return False

        window.fill(Colors["black"])

        text = "Is your name \'" + player_name + "\'?"
        renderText(window,primary_font,text,Colors["white"],(window_width / 2,window_height / 2 - 60))

        option1 = button("[Y]es",window_width / 2 - 225,window_height / 2,150,80,Colors["black"],Colors["white"])

        option2 = button("[N]o",window_width / 2 + 100,window_height / 2,150,80,Colors["black"],Colors["white"])

        pygame.display.update()

        clock.tick(60)

    return False

# Function that wraps and renders text if it goes beyond the allowed width
def wrapText(screen,texts,font,color,x,y,allowed_width):

    for text in texts:
        # Split the text into words
        words = text.split()

        # Constructing lines out of these words
        lines = []
        while len(words) > 0:
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                font_width,font_height = font.size(" ".join(line_words + words[:1]))
                if font_width > allowed_width:
                    break

            # Adding a line only consisting of those words
            line = " ".join(line_words)
            lines.append(line)

        # Rendering the text with the typewriter effect
        y_offset = 0
        for line in lines:
            font_width,font_height = font.size(line)

            top = y + y_offset

            for i in range(len(line)):
                renderedText = font.render(line[i],1,color)
                screen.blit(renderedText,(x + (font.size(line[:i])[0]),top))
                pygame.display.update()
                clock.tick(25)

            y_offset += font_height

        y = top + 75

enterName()

# The lines that will be displayed
lines = [
    "This is a story from a long, long time ago... idk what to write here, my vocabulary is very limited, i'm sorry for being a failure",
    "A time where nothing and everything existed at the same time. Making this a longer sentence for testing and if this passes, I can sleep peacefully. Ok, not peacefully, but I'll be able to sleep off for a while (maybe).",
    "Simply adding a third sentence for testing."
]

first_time = True

window.fill(Colors["black"])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user voluntarily closes the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and not first_time:
        # Breaks from the loop after displaying everything on the screen
        break

    if first_time:
        # for i in range(len(lines)):
        wrapText(window,lines,secondary_font,Colors["white"],50,50,700)

        first_time = False
    else:
        text = secondary_font.render("Press \'Enter\' to continue",1,Colors["white"])
        window.blit(text,(window_width / 2 + 100,window_height - 50))

    pygame.display.update()
    clock.tick(60)

# Stops the game engine after the user has completed the story
pygame.quit()