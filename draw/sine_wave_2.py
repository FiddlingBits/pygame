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
SINE_WAVE_POINTS = 1

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
hue = []
radius = []
for i in range(256):
    hue.append(i)
    radius.append(round_to_integer(SINE_WAVE_OBJECT_RADIUS * i / 255))
sine_wave_points = SINE_WAVE_POINTS
time_seconds = 0.0

# Initialize PyGame
pygame.init()

# Initialize Display
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Sine Wave 2")

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
                sine_wave_points += SINE_WAVE_POINTS
            if event.key == pygame.K_DOWN:
                sine_wave_points -= SINE_WAVE_POINTS
                if sine_wave_points < 1:
                    sine_wave_points = 1
    
    # Fill Display
    display.fill(BLACK)
    
    # Get Time
    time_seconds += clock.tick() / 1000.0
    
    # Get Sine Waves
    separation = (DISPLAY_WIDTH - (2 * DISPLAY_MARGIN)) / (sine_wave_points + 1)
    sine_waves = []
    if sine_wave_points > 1:
        time_offet_modifier = ((1 / SINE_WAVE_FREQUENCY) / (sine_wave_points - 1)) - 1
    else:
        time_offet_modifier = 0
    for i in range(sine_wave_points):
        sine_wave = []
        for j in range(256):
            time_offset = (255 - j) * 0.001 + (-time_offet_modifier + (i * time_offet_modifier))
            x = round_to_integer((i + 1) * separation)
            y = round_to_integer(DISPLAY_HEIGHT_CENTER - get_sine_point(SINE_WAVE_AMPLITUDE, SINE_WAVE_FREQUENCY, time_seconds - time_offset))
            sine_wave.append((x, y))
        sine_waves.append(sine_wave)
    
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
    
    # Draw Sine Wave Object And Tail
    for i in range(sine_wave_points):
        for j in range(256):
            pygame.draw.circle(display, working_color[j], sine_waves[i][j], radius[j])
    
    # Unlock Display
    display.unlock()
    
    # Draw Text (Antialias = True)
    text = font.render("Points: {}".format(sine_wave_points), True, WHITE)
    display.blit(text, (0, (0 * FONT_SIZE)))
    text = font.render("Color: {}".format(color[color_index]), True, WHITE)
    display.blit(text, (0, (1 * FONT_SIZE)))
    
    # Update Display
    pygame.display.update()
