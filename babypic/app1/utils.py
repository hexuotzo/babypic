from __future__ import division
import Image

def make_thumb(path, size = 480):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf
def make_thumb_small(path,size=65):
    pixbuf = Image.open(path)
    width, height = pixbuf.size
    if width > height:
        temp = height/2
    else:
        temp = width/2
    left= 0.5 * width - temp
    up= 0.5 * height -temp
    right= 0.5 * width + temp
    down= 0.5 * height +temp
    cutpic=pixbuf.crop((left,up,right,down))
    cutpic.thumbnail((size,size), Image.ANTIALIAS)
    return cutpic