import sys
import os
import pygame as pg

pg.init() # initialize pygame

clock = pg.time.Clock()

screen = pg.display.set_mode((600, 480))

# Load the background image here. Make sure the file exists!
bg = pg.image.load(os.path.join("./", "background.jpg"))

pg.mouse.set_visible(0)

pg.display.set_caption('Galaxian Remake')

while True:
    clock.tick(60)

    screen.blit(bg,(0,0))

    x,y = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()



