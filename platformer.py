import os
import time
import pygame
from pgzero import game, loaders
from pgzero.builtins import Actor
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER, transform_anchor

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def build(filename, tile_size):
    platforms=[]
    with open(f"{DIR_PATH}/{filename}", "r") as f:
        contents = f.read().splitlines()

    # convert to int but check if valid and for negative numbers
    contents = [c.split(",") for c in contents]
    for row in range(len(contents)):
        for col in range(len(contents[0])):
            val = contents[row][col]
            if val.isdigit() or (val[0] == "-" and val[1:].isdigit()):
                val = int(val)
                if val > 0:  # Örneğin, 0'dan büyük değerler platformu temsil eder
                    tile_name = f"tile_{val:04d}.png"  # 0001, 0067 gibi isimler
                    platform_image = f"tiles/{tile_name}"
                    platform = Actor(platform_image)  # Dinamik platform görselini kullan
                    platform.x = col * tile_size  # X konumunu ayarlıyoruz
                    platform.y = row * tile_size  # Y konumunu ayarlıyoruz
                    platforms.append(platform)  # Platformu listeye ekliyoruz

    return platforms
