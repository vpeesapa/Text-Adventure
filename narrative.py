#!usr/bin/python3.6

import pygame
from colors import Colors

pygame.init()

# --Global variables--
primary_font = pygame.font.SysFont("ubuntu mono",40)
secondary_font = pygame.font.SysFont("ubuntu mono",20)
special_font_italics = pygame.font.SysFont("ubuntu mono",20,bold = False,italic = True)
player_name = ""

# Contains the contents of the narrative
verse1 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "This is a story from a long, long time ago... idk what to write here, my vocabulary is very limited, i'm sorry for being a failure.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "A time where nothing and everything existed at the same time. Making this a longer sentence for testing and if this passes, I can sleep peacefully. Ok, not peacefully, but I'll be able to sleep off for a while (maybe).",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Simply adding a third sentence for testing.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "Testing out the italics and a different text speed to see if there is some change.",
            "option": False,
            "font": special_font_italics,
            "text_speed": 75,
            "EOP": True
        }
    ]
}

verse2 = {
    "bg-color": Colors["white"],
    "font-color": Colors["black"],
    "lines": [
        {
            "text": "This is the beginning of a new verse, which erases everything in the previous verse and renders the new text on a new screen.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Another line to see if everything works the way it does for the first verse.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Checking if we can add the player's name (" + player_name + ") seamlessly to the narrative.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verse3 = {
    "bg-color": Colors["violet"],
    "font-color": Colors["yellow"],
    "lines": [
        {
            "text": "Testing various options and seeing that they fit seamlessly with the rest of the narrative.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Kill the rebels",
            "option": True,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Spare the rebels",
            "option": True,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verse4 = {
    "bg-color": Colors["white"],
    "font-color": Colors["black"],
    "lines": [
        {
            "text": "",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "All of a sudden, the ground beneath his feet started rumbling.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "Cracks began to appear before it began collapsing.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verse5 = {
    "bg-color": Colors["white"],
    "font-color": Colors["black"],
    "lines": [
        {
            "text": "Oh no, another stupid, pointless choice appeared!",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Option A",
            "option": True,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Option B",
            "option": True,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verse6 = {
    "bg-color": Colors["white"],
    "font-color": Colors["black"],
    "lines": [
        {
            "text": "Boo yah, asshole!",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Oh, you're approaching me! Instead of running away, you're coming towards me.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verses = [verse1,verse2,verse3,verse4,verse5,verse6]