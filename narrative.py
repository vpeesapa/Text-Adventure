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
            "text": "A wild snowstorm brewed in the frigid Rand Mountains.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "The viciously cold and dark evening was accompanied by howling winds which sounded like the wailing of the spirits of the dead.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "The winds drowned out all the other noises and visibility was atrocious, making the already terrible landscape inaccessible for the few that dared to go near it.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "The evergreen, coniferous trees which canopied the gradients were draped in a thick blanket of snow, covering the lush greenery underneath never-melting ice.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Amidst the increasing intensity of the storm, the sound of multiple motors revved loudly, each making their distinctive sounds.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "They were then closely followed by the restless rustling of trees and its branches.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        }
    ]
}

verse2 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "As the noises echoed throughout the mountain ranges, four snowmobiles burst out of the forested area, leaving behind neat, straight trails of snow parted by its tracks.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "Three in the front followed by the remaining one that was vehemently pursuing the other three.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "The three motorboats that were in front continuously rocked left and right in an effort to confuse and get rid of its pursuer.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "But... it was all for a lost cause.",
            "option": False,
            "font": secondary_font,
            "text_speed": 5,
            "EOP": True
        }
    ]
}

verse3 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "Without wasting much time, the pursuing rider quickly managed to catch up to one of them who was lagging behind his companions by a few inches.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "Realizing that he could not shake his pursuer off any longer, the pursued rider slowed himself down to surprise his enemy with a gun that was hidden underneath his jacket.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "But, before he could react, the pursuing rider quickly unsheated his sword and swiftly decapacitated his enemy.",
            "option": False,
            "font": secondary_font,
            "text_speed": 120,
            "EOP": True
        }
    ]
}

verse4 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "The man's head oozed a copious amount of blood which stained the white blanket of snow as it slid off the body.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "The body which was still firmly holding onto the snowmobile slowly began to lean to its right, causing the vehicle to lose balance and violently sway back and forth before crashing into a nearby rock and exploding in flames, made only bigger by the oil leaking from it.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        }
    ]
}

verse5 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "The smell of oil lingered in the air as the other two riders desperately accelerated down the slope, hoping to quickly escape from the clutches of their pursuer.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "They immediately understood that they were the prey and the man chasing them was their predator. Their only means of escape was to outspeed the man before their heads are lopped off as well.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "All they had to do was go faster...",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "And faster...",
            "option": False,
            "font": secondary_font,
            "text_speed": 45,
            "EOP": False
        },
        {
            "text": "And faster.",
            "option": False,
            "font": secondary_font,
            "text_speed": 65,
            "EOP": True
        },
        {
            "text": "But... was it really that easy?",
            "option": False,
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