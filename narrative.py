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
            "text": "The three snowmobiles that were in front continuously rocked left and right in an effort to confuse and get rid of its pursuer.",
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
            "EOP": True
        },
        {
            "text": "Realizing that he could not shake his pursuer off any longer, the pursued rider slowed himself down to surprise his enemy with a gun that was hidden underneath his jacket.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
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
            "EOP": True
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
            "text_speed": 5,
            "EOP": True
        }
    ]
}

verse6 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "Just as they were about to lose their enemy, one of the riders rode off a cliff that had seemingly appeared out of nowhere and plummeted into the deep, dark abyss down below.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Watching his partner plunge to his death, the remaining rider quickly reacted by jumping off of his snowmobile at the last minute.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "As he picked himself up, he watched his ride, which was now out-of-control, follow in his partner's footsteps and dive into the sea of darkness that was waiting below.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "His eyes were filled with fear.",
            "option": False,
            "font": secondary_font,
            "text_speed": 20,
            "EOP": False
        },
        {
            "text": "His body was overcome by the naturalistic fear of death.",
            "option": False,
            "font": secondary_font,
            "text_speed": 15,
            "EOP": False
        },
        {
            "text": "His body remained paralyzed at that spot.",
            "option": False,
            "font": secondary_font,
            "text_speed": 10,
            "EOP": False
        },
        {
            "text": "Time around him began to slow down to a crawl. His breathing became heavier with each breath he took. His vision became blurry each time he blinked his eyes.",
            "option": False,
            "font": secondary_font,
            "text_speed": 5,
            "EOP": True
        },
        {
            "text": "The man was slowly, but surely, losing his grasp on reality.",
            "option": False,
            "font": secondary_font,
            "text_speed": 2,
            "EOP": True
        }
    ]
}

verse7 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "Letting go of the final shred of sanity that he had left, the man burst out in manic laughter.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "The fear of death broke him like a glass jar, forcing him to realize that his end was imminent and fast-approaching.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "While he continued laughing like a maniac, he watched the blurry vision of his pursuer tread slowly through the now knee-deep snow and towards him to deal one final blow.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "As a last resort to protect himself, he lashed out at the man, who was approaching him with his bloodthirsty crimson blade in tow.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "\"You... you... you Imperial kissing asshole! The Rebellion will chase the likes of you to the depths of hell and make sure that you regret crossing our paths!\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 45,
            "EOP": False
        },
        {
            "text": "\"You may be a legendary warrior, Gladio Anders, but even YOU cannot resist change! NOBODY can resist the change that we're ushering in.\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 10,
            "EOP": True
        }
    ]
}

verse8 = {
    "bg-color": Colors["black"],
    "font-color": Colors["white"],
    "lines": [
        {
            "text": "Gladio did not bat an eye towards his enemy's taunts.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "His cold, empty black eyes remained transfixed on his enemy's hapless face while he dragged his blade along the snow to deal the final blow.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "\"Wise words coming from rebel scum,\" he replied calmly. \"You might believe that the Rebellion has your back... but they are merely a pebble in our path.\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": True
        },
        {
            "text": "Seeing that there was no other alternative left, the rebel once again tried taunting his fast-approaching enemy.",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "\"You may have earned the people's trust through your exploits against the Monsters, Gladio. But... that's only because they do not know who you really are!\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 25,
            "EOP": False
        },
        {
            "text": "\"You had mindlessly slaughtered innocents...\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 20,
            "EOP": False
        },
        {
            "text": "\"You killed hordes of women...\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 15,
            "EOP": False
        },
        {
            "text": "\"You were even merciless against children...\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 10,
            "EOP": False
        },
        {
            "text": "\"You are no hero, Gladio... you're a MONSTER, just like the ones you had massacred for all these years.\"",
            "option": False,
            "font": secondary_font,
            "text_speed": 5,
            "EOP": True
        }
    ]
}

verses = [verse1,verse2,verse3,verse4,verse5,verse6,verse7,verse8]