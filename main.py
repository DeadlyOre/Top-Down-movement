import pygame


#Constants or initial values
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GAME_SPEED = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW = None

run = True

#=======================
#    Player class
#=======================

class Player:
    
    def __init__(self, x, y, w, h):
        #position and size
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #initial velocity
        self.velX = 0
        self.velY = 0
        #Constants
        self.ACCEL = 0.5
        self.FRIC = 0.1
        #Movement key handling
        self.upKey = False
        self.downKey = False
        self.leftKey = False
        self.rightKey = False

    def handleInput(self, e):
        #movement on keydown
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                self.upKey = True
            if e.key == pygame.K_s:
                self.downKey = True
            if e.key == pygame.K_a:
                self.leftKey = True
            if e.key == pygame.K_d:
                self.rightKey = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                self.upKey = False
            if e.key == pygame.K_s:
                self.downKey = False
            if e.key == pygame.K_a:
                self.leftKey = False
            if e.key == pygame.K_d:
                self.rightKey = False
        
    def render(self):
        pygame.draw.rect(WINDOW, WHITE, pygame.Rect(self.x, self.y, self.w, self.h))
    
    def update(self):
        #Updating velocity based on inputs
        if self.upKey:
            self.velY -= self.ACCEL
        if self.downKey:
            self.velY += self.ACCEL
        if self.leftKey:
            self.velX -= self.ACCEL
        if self.rightKey:
            self.velX += self.ACCEL
        
        #calculations and movement
        self.velY *= 1.0 - self.FRIC
        self.velX *= 1.0 - self.FRIC

        self.x += self.velX
        self.y += self.velY

#player object

player = Player(0, 0, 50, 50)

#==============================
#            Methods
#==============================
def main():

    global WINDOW

    pygame.init()
    WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Top Down Movement')


    gameLoop()

def draw():

    player.render()
    

def update():

    player.update()


def gameLoop():

    global run

    while run:
        #Looks through all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                player.handleInput(event)
        
        update()

        WINDOW.fill(BLACK)
        draw()
        pygame.display.update()

        pygame.time.wait(int(GAME_SPEED))


#Player class


if __name__ == '__main__':
    main()
    pygame.quit()
