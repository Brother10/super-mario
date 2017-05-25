import pygame, os
from pygame.locals import *

import data, menu

def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("bowser1.gif")))
    pygame.display.set_caption("Super Washington")
    screen = pygame.display.set_mode((640, 480))
    menu.Menu(screen)
    pygame.display.flip()

while True:
	main()