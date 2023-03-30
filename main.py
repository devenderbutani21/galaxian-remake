import sys
import os
import pygame as pg

pg.init() # initialize pygame

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

clock = pg.time.Clock()

screenwidth, screenheight = (480, 600)

screen = pg.display.set_mode((screenwidth,screenheight))

# Set the framerate
framerate = 60

# Set the background scrolling speed
bg_speed = 100


# Load the background image here. Make sure the file exists!
# bg = pg.image.load(os.path.join("./", "background.jpg"))

StarField = ScrollingBackground(screenheight, "background.jpg")

pg.mouse.set_visible(0)

pg.display.set_caption('Galaxian Remake')

while True:
    time = clock.tick(framerate)/1000.0

    x,y = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    StarField.UpdateCoords(bg_speed, time)

    StarField.Show(screen)
    pg.display.update()
