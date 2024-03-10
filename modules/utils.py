from __future__ import annotations

import math
from collections import namedtuple

import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageColor, PngImagePlugin

import modules.script_callbacks as script_callbacks

def image_grid(imgs, rows=None):
    if rows is None:
        rows = math.sqrt(len(imgs))
        rows = round(rows)
    if rows > len(imgs):
        rows = len(imgs)

    cols = math.ceil(len(imgs) / rows)

    params = script_callbacks.ImageGridLoopParams(imgs, cols, rows)
    script_callbacks.image_grid_callback(params)

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(params.cols * w, params.rows * h), color='black')

    for i, img in enumerate(params.imgs):
        grid.paste(img, box=(i % params.cols * w, i // params.cols * h))

    return grid

