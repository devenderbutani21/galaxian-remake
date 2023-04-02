import sys
import os
import pygame as pg
from pygame.locals import *

pg.init() # initialize pygame

pg.mixer.init() # initialize mixer for music


class ScrollingBackground:
    def __init__(self, screenheight, imagefile):
        self.img = pg.image.load(imagefile)
        self.coord = [0,0]
        self.coord2 = [0,-screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]
    
    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

    def UpdateCoords(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y
        if self.coord2[1] >= 0:
            self.coord[1] = self.y_original
            self.coord2[1] = self.y2_original

class HeroShip:
    def __init__(self, screenheight, screenwidth, imagefile):
        self.shape = pg.image.load(imagefile)
        self.top = screenheight - self.shape.get_height()
        self.left = screenwidth/2 - self.shape.get_width()/2
    
    def Show(self,surface):
        surface.blit(self.shape, (self.left, self.top))
    
    def UpdateCoords(self,x):
        self.left = x - self.shape.get_width()/2

class Laser(pg.sprite.Sprite):
    def __init__(self, imagefile, x, y):
        super().__init__()
        self.image = pg.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = 800 # adjust laser speed as needed

    def UpdateCoords(self, time):
        distance_y = self.speed_y * time
        self.rect.y -= distance_y
        if self.rect.bottom < 0:
            self.kill()

    def Show(self, surface):
        surface.blit(self.image, self.rect)

class LaserGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()

    def UpdateCoords(self, time):
        for laser in self.sprites():
            laser.UpdateCoords(time)

    def Show(self, surface):
        for laser in self.sprites():
            laser.Show(surface)

clock = pg.time.Clock()

screenwidth, screenheight = (480, 600)

screen = pg.display.set_mode((screenwidth,screenheight))

# Set the framerate
framerate = 60

# Set the background scrolling speed
bg_speed = 100


# Load the background image here. Make sure the file exists!
# bg = pg.image.load(os.path.join("./", "background.jpg"))

pg.mixer.music.load('space.mp3')

pg.mixer.music.play(-1)

StarField = ScrollingBackground(screenheight, "background.jpg")

pg.mouse.set_visible(0)

pg.display.set_caption('Galaxian Remake')

Hero = HeroShip(screenheight, screenwidth, "ship.png")

laser_group = LaserGroup()

while True:
    time = clock.tick(framerate)/1000.0

    x,y = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # left mouse button
                # Create laser sprite and add to sprite group
                laser = Laser("laser.png", Hero.left + Hero.shape.get_width() / 2, Hero.top)
                laser_group.add(laser)

    StarField.UpdateCoords(bg_speed, time)
    Hero.UpdateCoords(x)
    StarField.Show(screen)
    Hero.Show(screen)
    laser_group.Show(screen)
    pg.display.update()
