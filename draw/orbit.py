####################################################################################################
# Imports
####################################################################################################

import math
import pygame
import sys

####################################################################################################
# Constants
####################################################################################################

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display
DISPLAY_HEIGHT = 500
DISPLAY_MARGIN = 25
DISPLAY_WIDTH = 500

# Font
FONT = "arial"
FONT_SIZE = 18

# Orbit
ORBIT_CENTER_X = DISPLAY_WIDTH / 2
ORBIT_CENTER_Y = DISPLAY_HEIGHT / 2
ORBIT_FREQUENCY = 0.25
ORBIT_OBJECT_RADIUS = 10
if DISPLAY_HEIGHT <= DISPLAY_WIDTH:
    ORBIT_RADIUS = (DISPLAY_HEIGHT - (2 * DISPLAY_MARGIN)) / 2
else:
    ORBIT_RADIUS = (DISPLAY_WIDTH - (2 * DISPLAY_MARGIN)) / 2

####################################################################################################
# Functions
####################################################################################################

def get_cosine_point(amplitude, frequency, time):
    return amplitude * math.cos(2 * math.pi * frequency * time)

def get_sine_point(amplitude, frequency, time):
    return amplitude * math.sin(2 * math.pi * frequency * time)

def round_to_integer(number):
    return int(round(number, 0))

####################################################################################################
# Program Start
####################################################################################################

# Set Up
color = ["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"]
color_index = 0
frequency = ORBIT_FREQUENCY
hue = [i for i in range(256)]
radius = []
for i in range(256):
    radius.append(int(round(ORBIT_OBJECT_RADIUS * i / 255, 0)))
time_seconds = 0.0

# Initialize PyGame
pygame.init()

# Initialize Display
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Orbit")

# Initialize Clock
clock = pygame.time.Clock()

# Initialize Font
font = pygame.font.SysFont(FONT, FONT_SIZE)

# Run Game
while True:
    # Check For Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Uninitialize PyGame
            pygame.quit()
            
            # Exit
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                color_index -= 1
                if color_index < 0:
                    color_index = len(color) - 1
            if event.key == pygame.K_RIGHT:
                color_index = (color_index + 1) % len(color)
            if event.key == pygame.K_UP:
                frequency += ORBIT_FREQUENCY
            if event.key == pygame.K_DOWN:
                frequency -= ORBIT_FREQUENCY
    
    # Fill Display
    display.fill(BLACK)
    
    # Draw Text (Antialias = True)
    text = font.render("Frequency: {} Hz".format(frequency), True, WHITE)
    display.blit(text, (0, (0 * FONT_SIZE)))
    text = font.render("Color: {}".format(color[color_index]), True, WHITE)
    display.blit(text, (0, (1 * FONT_SIZE)))
    
    # Get Time
    time_seconds += clock.tick() / 1000.0
    
    # Get Orbit
    orbit = []
    for i in range(256):
        time_offset = (255 - i) / 1000
        x = round_to_integer(get_cosine_point(ORBIT_RADIUS, frequency, time_seconds - time_offset) + ORBIT_CENTER_X)
        y = round_to_integer(ORBIT_CENTER_Y - get_sine_point(ORBIT_RADIUS, frequency, time_seconds - time_offset))
        orbit.append((x, y))
    
    # Get Working Color
    working_color = []
    for i in range(256):
        if color[color_index] == "Red":
            working_color.append((hue[i], 0, 0))
        elif color[color_index] == "Yellow":
            working_color.append((hue[i], hue[i], 0))
        elif color[color_index] == "Green":
            working_color.append((0, hue[i], 0))
        elif color[color_index] == "Cyan":
            working_color.append((0, hue[i], hue[i]))
        elif color[color_index] == "Blue":
            working_color.append((0, 0, hue[i]))
        elif color[color_index] == "Magenta":
            working_color.append((hue[i], 0, hue[i]))
    
    # Lock Display
    display.lock() # Lock Display So PyGame Doesn't Have To Inefficiently Lock And Unlock Display With Each Call To pygame.draw.circle(...)
    
    # Draw Orbit Object And Tail
    for i in range(256):
        pygame.draw.circle(display, working_color[i], orbit[i], radius[i])
    
    # Unlock Display
    display.unlock()
    
    # Update Display
    pygame.display.update()
