
from tkinter import Tk, Label, BOTH, YES
from PIL import ImageTk, Image
from TkImageSupplier import *


class DeciderImageView(Label):
    def __init__(self, decider, show_transform=None):
        super().__init__(decider)
        self.show_transform = show_transform
        self.img_showing = None
        # Resize the picture when we resize
        self.bind('<Configure>', self.on_resize)
        self.pack(fill=BOTH, expand=YES)

    def on_resize(self, event):
        self.show_image(event.width, event.height)

    def show_image(self, width=-1, height=-1):
        if self.img_showing is None:
            self.config(image = "", text="No image available...")
            self.image = None
            return
        if width  == -1: width  = self.winfo_width()
        if height == -1: height = self.winfo_height()
        toshow = self.img_showing.copy()
        toshow.thumbnail((width, height), Image.ANTIALIAS)
        if self.show_transform:
            toshow = self.show_transform(toshow)
        photo = ImageTk.PhotoImage(toshow)
        self.config(image = photo)
        self.image = photo

    def set_image(self, image):
        self.set_img_data = image
        img_loaded = Image.open(image) if\
            isinstance(image, str) else image
        self.img_showing = img_loaded
        self.show_image()


class TkImageDecider(Tk):
    def __init__(self, image_supplier, set_defaults=True,
        show_transform=None, on_next_image=None):
        super().__init__()
        self.diview = DeciderImageView(self, show_transform)
        self.on_next_image  = on_next_image
        self.image_supplier = TkFolderSupplier(image_supplier) if\
            isinstance(image_supplier, str) else image_supplier
        if set_defaults: self.set_defaults()
        self.show_next_image()

    def show_next_image(self, amount=1):
        # Quick hack to make this work with events
        if not isinstance(amount, int): amount = 1
        img = self.image_supplier.get_image_d(amount)
        if self.on_next_image:
            self.on_next_image(self.diview.img_showing, img)
        self.diview.set_image(img)

    def set_defaults(self, keys_too=True):
        self.resizable(width=True, height=True)
        self.geometry("600x600")
        if not keys_too: return
        self.bind('<Return>', self.show_next_image)
        self.bind('<Right>', self.show_next_image)
        self.bind('<Left>', lambda e: self.show_next_image(-1))
