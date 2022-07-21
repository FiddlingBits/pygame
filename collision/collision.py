####################################################################################################
# Import
####################################################################################################

import getopt
import pygame
import sys

####################################################################################################
# Constant
####################################################################################################

COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
SURFACE_HEIGHT = 500
SURFACE_WIDTH = 500

####################################################################################################
# Function
####################################################################################################

####################################################################################################
# Function
####################################################################################################

def print_usage():
    print("Usage: {} [OPTION]" .format(sys.argv[0]), flush=True)
    print("  -c[MODEL], --collision=[MODEL]", flush=True)
    print("  -h, --help", flush=True)

def run(collision, surface):
    # Set Up
    if collision == 0:
        rectangle = pygame.Rect(surface.get_rect().center, (0, 0)).inflate(100, 100)
    elif collision == 1:
        rectangle_1 = pygame.Rect(surface.get_rect().center, (0, 0)).inflate(100, 100)
        rectangle_2 = pygame.Rect((0, 0), (0, 0)).inflate(100, 100)
    elif collision == 2:
        monkey = pygame.sprite.Sprite()
        monkey.image = pygame.image.load("monkey.png")
        monkey.rect = monkey.image.get_rect()
        bear = pygame.sprite.Sprite()
        bear.image = pygame.image.load("bear.png")
        bear.rect = pygame.Rect(surface.get_rect().center, (0, 0)).inflate(bear.image.get_rect().width, bear.image.get_rect().height)

    # Infinite Loop
    while True:
        # Check For Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill Surface
        surface.fill(COLOR_BLACK)
        
        # Draw
        if collision == 0:
            if rectangle.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(surface, COLOR_RED, rectangle)
            else:
                pygame.draw.rect(surface, COLOR_WHITE, rectangle)
        elif collision == 1:
            rectangle_2.center = pygame.mouse.get_pos()
            if rectangle_1.colliderect(rectangle_2):
                pygame.draw.rect(surface, COLOR_RED, rectangle_1)
            else:
                pygame.draw.rect(surface, COLOR_WHITE, rectangle_1)
            pygame.draw.rect(surface, COLOR_GREEN, rectangle_2, 5, 1)
        elif collision == 2:
            monkey.rect.center = pygame.mouse.get_pos()
            if bear.rect.colliderect(monkey.rect):
                pygame.draw.rect(surface, COLOR_RED, bear.rect)
            else:
                pygame.draw.rect(surface, COLOR_WHITE, bear.rect)
            surface.blit(bear.image, bear.rect)
            surface.blit(monkey.image, monkey.rect)
        
        # Flip Display
        pygame.display.flip()

####################################################################################################
# Program Start
####################################################################################################

# Check For Arguments
opts, args = getopt.getopt(sys.argv[1:], "c:h", ["collision=", "help"])

# Set Defaults
collision = None

# Parse Arguments
for option, argument in opts:
    if option in ("-c", "--collision"):
        collision = int(argument)
    elif option in ("-h", "--help"):
        print_usage()
        sys.exit()

# Initialize
pygame.init()
pygame.display.set_caption("Collision")
surface = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))

# Run
run(collision, surface)

# Quit
pygame.quit()
