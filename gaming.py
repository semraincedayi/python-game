import pgzrun
import os
import time
import pygame
from pgzero import game,loaders
from pgzero.builtins import Actor
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER, transform_anchor

from platformer import build



TILE_SIZE=18
ROWS=30
COLS=20

WIDTH=TILE_SIZE*ROWS
HEIGHT=TILE_SIZE*COLS
TITLE="Ruin Game"

platforms=build("platformer_platformers.csv",TILE_SIZE)
obstacles=build("platformer_obstacles.csv",TILE_SIZE)
mushrooms=build("platformer_mushrooms.csv",TILE_SIZE)
diamonds=build("platformer_diamonds.csv",TILE_SIZE)

player=Actor("actor/tile_0000")
player.alive=True

player.bottomleft=(0, HEIGHT - TILE_SIZE)


player.velocity_x=3
player.velocity_y=0
player.jumping=False

gravity=1
jump_velocity=-10
over=False



def draw():
    screen.clear()
    screen.fill("skyblue")
    for platform in platforms:
        platform.draw()

    for obstacle in obstacles:
        obstacle.draw()

    for mushroom in mushrooms:
        mushroom.draw()

    for diamond in diamonds:
        diamond.draw()

    if player.alive:
       player.draw()
       
    if over:screen.draw.text("GAME OVER", center=(WIDTH/2+HEIGHT/2))






def update():
    global over
    
    if keyboard.LEFT and player.midleft[0]>0:
        player.x -=player.velocity_x
        player.image="actor/tile_0000"
        platform_hit = player.collidelist(platforms)
        if platform_hit != -1:
            platform = platforms[platform_hit]
            player.x=platform.x+(platform.width/2+player.width/2)

    elif keyboard.RIGHT and player.midright[0]<WIDTH:
        player.x +=player.velocity_x
        player.image="actor/tileright_0000"
        platform_hit = player.collidelist(platforms)
        if platform_hit != -1:
            platform = platforms[platform_hit]
            player.x=platform.x-(platform.width/2+player.width/2)

    
    player.y +=player.velocity_y
    player.velocity_y +=gravity 

    platform_hit = player.collidelist(platforms)
    if platform_hit != -1:
        platform = platforms[platform_hit]
        if player.velocity_y>=0:
            player.y=platform.y -(platform.height/2+player.height/2)
        else:
            player.y=platform.y +(platform.height/2+player.height/2)

        player.velocity_y=0

    if player.collidelist(obstacles)!=-1:
        player.alive=False
        over=True

    for mushroom in mushrooms:
        if player.colliderect(mushroom):
            mushrooms.remove(mushroom)

    for diamond in diamonds:
        if player.colliderect(diamond):
            diamonds.remove(diamond)
        

def on_key_down(key):
    if key==keys.UP and not player.jumping:
        player.velocity_y=jump_velocity
        player.jumping=True

    player.y +=player.velocity_y
    player.velocity_y +=gravity


