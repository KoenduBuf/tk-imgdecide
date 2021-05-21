
from PIL import ImageDraw, ImageEnhance
from imgdecide import *
import os

crop_to_size       = 512                                # How big to make the images
images_from_folder = "originals"                        # Where the images are
images_to_folder   = f"{crop_to_size}x{crop_to_size}"   # Where to store the cropped ones


def square_area(image, at_fraction):
    square_size = min(image.width, image.height)
    x_start_at  = int((image.width  - square_size) * at_fraction)
    y_start_at  = int((image.height - square_size) * at_fraction)
    return (x_start_at, y_start_at, x_start_at
        + square_size, y_start_at + square_size)


def get_cropped(image, at_fraction):
    area = square_area(image, at_fraction)
    return image.crop(area), area


def highlight_area(image, at_fraction):
    cropped, region = get_cropped(image, at_fraction)
    brightner = ImageEnhance.Brightness(cropped)
    cropped = brightner.enhance(1.4)
    image.paste(cropped, region)
    return image


def save_cropped(image, at_fraction):
    if image is None: return
    cropped, region = get_cropped(image, at_fraction)
    filename = str(os.path.basename(image.filename))
    print("Saving", filename)
    cropped.thumbnail((crop_to_size, crop_to_size), Image.ANTIALIAS)
    if cropped.width != crop_to_size or cropped.height != crop_to_size:
        raise Exception("Images should become 512x512")
    cropped.save(os.path.join(images_to_folder, filename))


at_frac = 0
def change_at_frac(d):
    global at_frac
    at_frac = min(1, max(0, at_frac + d))
    decider.diview.show_image()


decider = TkImageDecider(
    images_from_folder,
    show_transform = lambda img: highlight_area(img, at_frac),
    on_next_image  = lambda prev, new: save_cropped(prev, at_frac)
)
decider.bind("<s>", lambda e: change_at_frac(0.25))
decider.bind("<d>", lambda e: change_at_frac(0.25))
decider.bind("<a>", lambda e: change_at_frac(-0.25))
decider.bind("<w>", lambda e: change_at_frac(-0.25))
decider.mainloop()
