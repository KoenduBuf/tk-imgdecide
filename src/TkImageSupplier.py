
import os, sys


def img_file_extension(filename):
    ext = os.path.splitext(filename)[1].decode('utf-8')
    return ext.lower() in { '.jpg', '.jpeg', '.png' }


class TkImageSupplier:
    def __init__(self):
        self.at_index = -1

    # Get an image, using index, (i.e. 1 gets second image)
    def get_image_i(self, index):
        change = index - self.at_index
        self.at_index = index
        return self._get_image(self.at_index, change)

    # Get an image, using change (i.e. 1 goes to next image)
    def get_image_d(self, change):
        self.at_index = self.at_index + change
        return self._get_image(self.at_index, change)

    # The thing that people have to implement,
    # should return a string or pillow image
    def _get_image(self, index, change):
        raise Exception("Supplier did not implement _get_image")


class TkFolderSupplier(TkImageSupplier):
    def __init__(self, from_folder, file_filter=img_file_extension):
        super().__init__()
        if not os.path.isdir(from_folder):
            print("The given directory does not exist...")
            sys.exit(1)
        self.folder = from_folder
        self.filter = file_filter
        self.files  = [ ]
        self.get_folder_content()

    def get_folder_content(self):
        foldere = os.fsencode(self.folder)
        files   = os.listdir(foldere)
        filterd = list(filter(self.filter, files))
        print(f"[ Supplier ] Using {len(filterd)}/{len(files)} files")
        self.files = list(map(os.fsdecode, filterd))

    def _get_image(self, index, change):
        if index >= len(self.files): return None
        filename = self.files[index]
        return os.path.join(self.folder, filename)
