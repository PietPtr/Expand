import pygame, sys, os
from pygame.locals import *

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 40)

windowSurface = pygame.display.set_mode((1800, 980), 0, 32)
pygame.display.set_caption('CLICK!')
basicFont = pygame.font.SysFont(None, 23)
mainClock = pygame.time.Clock()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

TIMEDIFFERENCE = 100
SPEED = 0.4

lastClick = pygame.time.get_ticks()
ringList = []
transmitterList = []

def distance(speed, frameTime):
    distance = speed * frameTime
    return distance

class Ring(object):
    def __init__(self, position):
        self.position = position
        self.size = 1
    def render(self):
        pygame.draw.circle(windowSurface, BLUE, (self.position[0], self.position[1]), int(self.size), 1)
        #pygame.draw.rect(windowSurface, RED, (self.position[0], self.position[1], int(self.size), int(self.size)), 1)
        self.size = self.size + distance(SPEED, frameTime)

class Transmitter(object):
    def __init__(self, position):
        self.position = position
        self.lastSpawn = pygame.time.get_ticks()
    def spawn(self):
        if pygame.time.get_ticks() - self.lastSpawn >= TIMEDIFFERENCE:
            ringList.append(Ring([self.position[0], self.position[1]]))
            self.lastSpawn = pygame.time.get_ticks()



while True:
    frameTime = mainClock.tick(1000)
    FPS = mainClock.get_fps()
    currentTime = pygame.time.get_ticks()
    mousePosition = pygame.mouse.get_pos()

    windowSurface.fill(BLACK)

    if pygame.mouse.get_pressed()[0] == True and pygame.time.get_ticks() - lastClick >= TIMEDIFFERENCE:
        ringList.append(Ring([mousePosition[0], mousePosition[1]]))
        lastClick = pygame.time.get_ticks()

    for ring in ringList:
        ring.render()
        if ring.size > 2000:
            ringList.remove(ring)

    for transmitter in transmitterList:
        transmitter.spawn()
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            if event.button == 3:
                transmitterList.append(Transmitter([mousePosition[0], mousePosition[1]]))
        if event.type == KEYUP:
            if event.key == 293:
                for x in range(0, 4294967):
                    if os.path.exists("screenshot" + str(x) + ".jpeg") == True:
                        next
                    elif os.path.exists("screenshot" + str(x) + ".jpeg") == False:
                        pygame.image.save(windowSurface, "screenshot" + str(x) + ".jpeg")
                        break           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()