import pygame


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pygame.init()
window = pygame.display.set_mode((800, 600))


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, up, down):
        super(Paddle, self).__init__()
        self.height = 75
        self.width = 20
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y - (self.height / 2)
        self.up = up
        self.down = down


    def update(self, keys_pressed):
        if(keys_pressed[self.up]):
            self.y -= 1
        if(keys_pressed[self.down]):
            self.y += 1
        if(self.y <= 0):
            self.y = 0
        if(self.y + self.height >= SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT - self.height


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.height = 20
        self.width = 20
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = SCREEN_WIDTH / 2 - (self.width / 2)
        self.y = SCREEN_HEIGHT / 2 - (self.height / 2)
        self.velX = 1
        self.velY = 1

    def update(self, keys_pressed):
        if(self.x <= 0):
            self.velX = 1
        if(self.x + self.width >= SCREEN_WIDTH):
            self.velX = -1
        if(self.y <= 0):
            self.velY = 1
        if(self.y + self.height >= SCREEN_HEIGHT):
            self.velY = -1

        self.x += self.velX
        self.y += self.velY
        

gameObjects = {}
gameObjects["player1"] = Paddle(10, SCREEN_HEIGHT/2, pygame.K_q, pygame.K_a)
gameObjects["player2"] = Paddle(770, SCREEN_HEIGHT/2, pygame.K_UP, pygame.K_DOWN)
gameObjects["ball"] = Ball()

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

