import pygame


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pygame.init()
window = pygame.display.set_mode((800, 600))


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddle, self).__init__()
        self.height = 75
        self.width = 20
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = 10
        self.y = SCREEN_HEIGHT / 2 - (self.height/2)


    def update(self, keys_pressed):
        if(keys_pressed[pygame.K_UP]):
            self.y -= 1
        if(keys_pressed[pygame.K_DOWN]):
            self.y += 1
        if(self.y <= 0):
            self.y = 0
        if(self.y + self.height >= SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT - self.height

gameObjects = {}
gameObjects["player"] = Paddle()


# Wait for the user to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    
        

    window.fill((0, 0, 0))

    for key, gameObject in gameObjects.items():
        gameObject.update(pressed_keys)
        window.blit(gameObject.surf, (gameObject.x, gameObject.y))

    pygame.display.flip()

