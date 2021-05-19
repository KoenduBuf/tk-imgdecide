# tk-imgdecide

A python library for very quickly prototyping an application that classifies images (not in the ML way), crops them, filters out images etc etc.
This package has only 1 dependency: Pillow, appart from that it uses standard python 3, and the built-in tkinter gui framework.
Any contributions to this library are appreciated, this library is meant to be make editing a large amount of images manually a little easier.

## Use cases + Examples

Some use cases, that I have used (/use) this for, each of these can be found in the 'examples' folder
 - Classify images into a bunch of different folders (if you have 10000 old whatsapp images, and you want to sort them into folders)
 - Change the names of images to something based on image contents (for example if you want to label people in your pictures)
 - Crop images to a specific size, maybe first resizing, maybe not (for example if you want NxN images to train a CNN or something)
