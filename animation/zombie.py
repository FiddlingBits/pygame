####################################################################################################
# Import
####################################################################################################

import pygame

####################################################################################################
# Constant
####################################################################################################

COLOR_BLACK = (0, 0, 0)
FPS = 30
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1000

####################################################################################################
# Function
####################################################################################################

def run(clock, screen):
    # Zombie (Male)
    zombie_male_attack = [
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Attack (8).png"), (128, 128))
    ]
    zombie_male_attack_count = 8
    zombie_male_attack_index = 0
    zombie_male_dead = [
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (1).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (2).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (3).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (4).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (5).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (6).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (7).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (8).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (9).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (10).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (11).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Dead (12).png"), (155, 155))
    ]
    zombie_male_dead_count = 12
    zombie_male_dead_index = 0
    zombie_male_idle = [
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (8).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (9).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (10).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (11).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (12).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (13).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (14).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Idle (15).png"), (128, 128))
    ]
    zombie_male_idle_count = 15
    zombie_male_idle_index = 0
    zombie_male_walk = [
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (8).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (9).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/male/Walk (10).png"), (128, 128))
    ]
    zombie_male_walk_count = 10
    zombie_male_walk_index = 0
    
    # Zombie (Female)
    zombie_female_attack = [
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Attack (8).png"), (128, 128))
    ]
    zombie_female_attack_count = 8
    zombie_female_attack_index = 0
    zombie_female_dead = [
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (1).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (2).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (3).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (4).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (5).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (6).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (7).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (8).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (9).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (10).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (11).png"), (155, 155)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Dead (12).png"), (155, 155))
    ]
    zombie_female_dead_count = 12
    zombie_female_dead_index = 0
    zombie_female_idle = [
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (8).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (9).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (10).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (11).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (12).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (13).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (14).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Idle (15).png"), (128, 128))
    ]
    zombie_female_idle_count = 15
    zombie_female_idle_index = 0
    zombie_female_walk = [
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (1).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (2).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (3).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (4).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (5).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (6).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (7).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (8).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (9).png"), (128, 128)),
        pygame.transform.scale(pygame.image.load("./zombie/female/Walk (10).png"), (128, 128))
    ]
    zombie_female_walk_count = 10
    zombie_female_walk_index = 0

    # Infinite Loop
    while True:
        # Clock
        clock.tick(FPS)
    
        # Check For Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill Screen
        screen.fill(COLOR_BLACK)
        
        # Draw Zombie (Male)
        screen.blit(zombie_male_attack[zombie_male_attack_index], (0 * 128, 0))
        screen.blit(pygame.transform.flip(zombie_male_attack[zombie_male_attack_index], True, False), (1 * 128, 0))
        zombie_male_attack_index = (zombie_male_attack_index + 1) % zombie_male_attack_count
        screen.blit(zombie_male_dead[zombie_male_dead_index], (2 * 128, 0))
        screen.blit(pygame.transform.flip(zombie_male_dead[zombie_male_dead_index], True, False), (3 * 128, 0))
        zombie_male_dead_index = (zombie_male_dead_index + 1) % zombie_male_dead_count
        screen.blit(zombie_male_idle[zombie_male_idle_index], (4 * 128, 0))
        screen.blit(pygame.transform.flip(zombie_male_idle[zombie_male_idle_index], True, False), (5 * 128, 0))
        zombie_male_idle_index = (zombie_male_idle_index + 1) % zombie_male_idle_count
        screen.blit(zombie_male_walk[zombie_male_walk_index], (6 * 128, 0))
        screen.blit(pygame.transform.flip(zombie_male_walk[zombie_male_walk_index], True, False), (7 * 128, 0))
        zombie_male_walk_index = (zombie_male_walk_index + 1) % zombie_male_walk_count
        
        # Draw Zombie (Female)
        screen.blit(zombie_female_attack[zombie_female_attack_index], (0 * 128, 256))
        screen.blit(pygame.transform.flip(zombie_female_attack[zombie_female_attack_index], True, False), (1 * 128, 256))
        zombie_female_attack_index = (zombie_female_attack_index + 1) % zombie_female_attack_count
        screen.blit(zombie_female_dead[zombie_female_dead_index], (2 * 128, 256))
        screen.blit(pygame.transform.flip(zombie_female_dead[zombie_female_dead_index], True, False), (3 * 128, 256))
        zombie_female_dead_index = (zombie_female_dead_index + 1) % zombie_female_dead_count
        screen.blit(zombie_female_idle[zombie_female_idle_index], (4 * 128, 256))
        screen.blit(pygame.transform.flip(zombie_female_idle[zombie_female_idle_index], True, False), (5 * 128, 256))
        zombie_female_idle_index = (zombie_female_idle_index + 1) % zombie_female_idle_count
        screen.blit(zombie_female_walk[zombie_female_walk_index], (6 * 128, 256))
        screen.blit(pygame.transform.flip(zombie_female_walk[zombie_female_walk_index], True, False), (7 * 128, 256))
        zombie_female_walk_index = (zombie_female_walk_index + 1) % zombie_female_walk_count
        
        # Update Display
        pygame.display.update()

####################################################################################################
# Program Start
####################################################################################################

# Initialize
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Zombie")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Run
run(clock, screen)

# Quit
pygame.quit()
