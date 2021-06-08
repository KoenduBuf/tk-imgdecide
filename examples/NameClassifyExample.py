#!/usr/bin/env python3

from imgdecide import *
import os

images_from_folder = "path/to/the/images"   # Where the images are
images_to_folder   = "path/to/store/them"   # Where to store classified images


def save_image(toclass):
    img  = decider.diview.img_showing
    name = str(os.path.basename(img.filename))
    prts = os.path.splitext(name)
    new  = f"{prts[0]}_{toclass}{prts[1]}"
    newp = os.path.join(images_to_folder, new)
    img.save(newp)
    # Continue to next image
    decider.show_next_image()


decider = TkImageDecider(images_from_folder, set_defaults = False)
decider.bind("1", lambda e: save_image(1))
decider.bind("2", lambda e: save_image(2))
decider.bind("3", lambda e: save_image(3))
decider.bind("4", lambda e: save_image(4))
decider.mainloop()
