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
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT / 2
DISPLAY_MARGIN = 25
DISPLAY_WIDTH = 1000

# Font
FONT = "arial"
FONT_SIZE = 18

# Sine Wave
SINE_WAVE_AMPLITUDE = DISPLAY_HEIGHT_CENTER - DISPLAY_MARGIN
SINE_WAVE_FREQUENCY = 1.0
SINE_WAVE_OBJECT_RADIUS = 10
SINE_WAVE_X_RANGE = DISPLAY_WIDTH - (2 * DISPLAY_MARGIN)
SINE_WAVE_X_TIME_OFFSET = 1.0 / SINE_WAVE_X_RANGE # 1.0 (One Second)

####################################################################################################
# Functions
####################################################################################################

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
frequency = SINE_WAVE_FREQUENCY
hue = []
radius = []
for i in range(SINE_WAVE_X_RANGE):
    hue.append(round_to_integer(255 * i / (SINE_WAVE_X_RANGE - 1)))
    radius.append(round_to_integer(SINE_WAVE_OBJECT_RADIUS * i / (SINE_WAVE_X_RANGE - 1)))
time_seconds = 0.0

# Initialize PyGame
pygame.init()

# Initialize Display
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Sine Wave 1")

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
                frequency += SINE_WAVE_FREQUENCY
            if event.key == pygame.K_DOWN:
                frequency -= SINE_WAVE_FREQUENCY
    
    # Fill Display
    display.fill(BLACK)
    
    # Get Time
    time_seconds += clock.tick() / 1000.0
    
    # Get Sine Wave
    sine_wave = []
    for i in range(SINE_WAVE_X_RANGE):
        time_offset = ((SINE_WAVE_X_RANGE - 1) - i) * SINE_WAVE_X_TIME_OFFSET
        x = round_to_integer(DISPLAY_MARGIN + i)
        y = round_to_integer(DISPLAY_HEIGHT_CENTER - get_sine_point(SINE_WAVE_AMPLITUDE, frequency, time_seconds - time_offset))
        sine_wave.append((x, y))
    
    # Get Working Color
    working_color = []
    for i in range(SINE_WAVE_X_RANGE):
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
    
    # Draw Sine Wave Object And Tail
    for i in range(SINE_WAVE_X_RANGE):
        pygame.draw.circle(display, working_color[i], sine_wave[i], radius[i])
    
    # Unlock Display
    display.unlock()
    
    # Draw Text (Antialias = True)
    text = font.render("Frequency: {} Hz".format(frequency), True, WHITE)
    display.blit(text, (0, (0 * FONT_SIZE)))
    text = font.render("Color: {}".format(color[color_index]), True, WHITE)
    display.blit(text, (0, (1 * FONT_SIZE)))
    
    # Update Display
    pygame.display.update()
