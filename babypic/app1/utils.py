from __future__ import division
import os
import Image

def make_thumb(path, size = 480):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf
