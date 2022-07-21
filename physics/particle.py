####################################################################################################
# Import
####################################################################################################

import getopt
import math
import pygame
import random
import sys

####################################################################################################
# Constant
####################################################################################################

# Cluster
MOVE_MAXIMUM = 2
PARTICLES_START = 10000
PIXELS_PER_METER = 0.1
SPEED_MAXIMUM = 0.25
SPEED_MINIMUM = 0.01

# Common
FONT = "arial"
FONT_SIZE = 18
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

####################################################################################################
# Class
####################################################################################################

class BasicParticle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def bounds_check(self, max_x, min_x, max_y, min_y):
        if min_x <= self.x < max_x and min_y <= self.y < max_y:
            return True
        else:
            return False

    def draw(self):
        pygame.draw.circle(self.screen, rgb("white"), (self.x, self.y), 1)

    def move(self, x, y):
        self.x += x
        self.y += y

class AdvancedParticle(BasicParticle):
    def __init__(self, angle, screen, speed, x, y):
        super().__init__(screen, x, y)
        self.angle = angle
        self.speed = speed

    def move(self):
        x = self.speed * math.sin(math.radians(self.angle))
        y = self.speed * math.cos(math.radians(self.angle))
        super().move(x, y)

class FallingParticle(BasicParticle):
    def __init__(self, screen, start_time, x):
        super().__init__(screen, x, 0)
        self.speed = 0.0
        self.start_time = start_time
        self.starting_velocity = 0.0

    def bounds_check(self, max_y):
        if self.y <= max_y:
            return True
        else:
            return False

    def change_velocity(self, new_y, start_time, velocity):
        self.y = new_y
        self.start_time = start_time
        self.starting_velocity = velocity

    def get_velocity(self, time):
        v = (self.starting_velocity * (time - self.start_time)) + (0.5 * 9.8 * math.pow(time - self.start_time, 2.0)) # g = 9.8 m/s^2
        return v

    def move(self, time):
        velocity = self.get_velocity(time)
        self.y += velocity

####################################################################################################
# Function
####################################################################################################

def print_usage():
    print("Usage: {} [OPTION]" .format(sys.argv[0]), flush=True)
    print("  -c[MODEL], --cluster=[MODEL]", flush=True)
    print("  -h, --help", flush=True)

def rgb(color):
    color.lower()
    if color == "black":
        color = (0, 0, 0)
    elif color == "red":
        color = (255, 0, 0)
    elif color == "white":
        color = (255, 255, 255)
    else:
        color = None

    return color

def run_cluster(clock, font, screen, cluster):
    # Set Up
    lost = 0
    particle_list = []
    pygame.display.set_caption("Cluster ({})".format(cluster))
    time = 0.0

    # Cluster Specific
    if cluster == 0:
        for _ in range(PARTICLES_START):
            particle_list.append(BasicParticle(screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    elif cluster == 1:
        for _ in range(PARTICLES_START):
            angle = random.uniform(0.0, 359.9)
            speed = random.uniform(SPEED_MINIMUM, SPEED_MAXIMUM)
            particle_list.append(AdvancedParticle(angle, screen, speed, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # Infinite Loop
    while True:
        # Check For Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill Screen
        screen.fill(rgb("black"))

        # Print
        time += clock.tick() / 1000.0 # Convert To Seconds
        text = font.render("Time: {:.3f}".format(time), True, rgb("red"))
        screen.blit(text, (0, (0 * FONT_SIZE)))
        text = font.render("FPS: {}".format(int(clock.get_fps())), True, rgb("red"))
        screen.blit(text, (0, (1 * FONT_SIZE)))
        text = font.render("On-Screen: {}".format(len(particle_list)), True, rgb("red"))
        screen.blit(text, (0, (2 * FONT_SIZE)))
        text = font.render("Lost: {}".format(lost), True, rgb("red"))
        screen.blit(text, (0, (3 * FONT_SIZE)))

        # Cluster Specific
        if cluster == 0:
            # Add New Particle
            particle_list.append(BasicParticle(screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

            # Move Particles
            for particle in particle_list:
                x = random.randint(-MOVE_MAXIMUM, MOVE_MAXIMUM)
                y = random.randint(-MOVE_MAXIMUM, MOVE_MAXIMUM)
                particle.move(x, y)
        elif cluster == 1:
            # Add New Particle
            angle = random.uniform(0.0, 359.9)
            speed = random.uniform(SPEED_MINIMUM, SPEED_MAXIMUM)
            particle_list.append(AdvancedParticle(angle, screen, speed, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

            # Move Particles
            for particle in particle_list:
                particle.move()
        elif cluster == 2:
            # Add New Particle
            x = random.randint(0, SCREEN_WIDTH - 1)
            particle_list.append(FallingParticle(screen, time, x))

            # Move Particles
            for particle in particle_list:
                particle.move(time)

        # Bounds Check Particles
        updated_particle_list = []
        for particle in particle_list:
            if cluster == 0 or cluster == 1:
                if particle.bounds_check(SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1, 0):
                    updated_particle_list.append(particle) # Still On Screen
            elif cluster == 2:
                if particle.bounds_check(SCREEN_HEIGHT - 1):
                    updated_particle_list.append(particle)  # Still On Screen
                else:
                    velocity = -particle.get_velocity(time) * 5.0 / 8.0
                    if velocity < -0.1:
                        particle.change_velocity(SCREEN_HEIGHT - 1, time, velocity) # Not On Screen; Reverse Direction
                        updated_particle_list.append(particle)
        lost += len(particle_list) - len(updated_particle_list)
        particle_list = updated_particle_list

        # Draw Particles
        screen.lock()
        for particle in particle_list:
            particle.draw()
        screen.unlock()

        # Update Display
        pygame.display.update()

####################################################################################################
# Program Start
####################################################################################################

# Check For Arguments
opts, args = getopt.getopt(sys.argv[1:], "c:h", ["cluster=", "help"])

# Set Defaults
cluster = None

# Parse Arguments
for option, argument in opts:
    if option in ("-c", "--cluster"):
        cluster = int(argument)
    elif option in ("-h", "--help"):
        print_usage()
        sys.exit()

# Initialize
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(FONT, FONT_SIZE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Handle Arguments
if cluster != None:
    run_cluster(clock, font, screen, cluster)

# Quit
pygame.quit()
