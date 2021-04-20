import pygame

width = 500
height = 500

# Define the game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
    

    # Draws the player to the display
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    

    def move(self):
        # Gets pressed key
        keys = pygame.key.get_pressed()

        # Movement keys and changes velocity
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)

# Updates the window which stuff is drawn on
def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


# Main game loop which everything runs in
def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT
        
        p.move()
        redrawWindow(win, p)


main()