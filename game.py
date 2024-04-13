import pygame

pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600))

# Fill the window with white
window.fill((0, 0, 0))

# Update the display
pygame.display.flip()

# Wait for the user to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()