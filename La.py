import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
pg.display.set_caption("My Pygame Window")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")
    pg.display.update()

pg.quit()