import os
import shutil 
from PIL import Image

from utils import program_name_to_filename

# NOTE: This disables "too large image" error from PIL
# You can set this "None" if you trust the images you are handling
Image.MAX_IMAGE_PIXELS = 10001*10001

IMG_SOURCE_DIR = "./img_downloads"
IMG_CONVERT_DIR = "./img_converted"
IMG_TMB_DIR = os.path.join(IMG_CONVERT_DIR, "thumb")
IMG_CONVERT_TO_SIZE = 900 # pixels
IMG_TMB_SIZE = 176


def show_warnings(im):
    sizestr = str(im.size[0])+"x"+str(im.size[1])
    if im.size[0] != im.size[1]:
        print("WARNING, image not 1:1, "+sizestr)
    if im.size[0] < 2048:
        print("WARNING, image less than 2048px wide: "+sizestr)


def convert_image(path):
    head, filename = os.path.split(path)
    filename_noext, ext = os.path.splitext(filename)
    # Run the name-conversion in case we're processing manually returned files
    filename_noext = program_name_to_filename(filename_noext)
    path_noext = os.path.join(IMG_CONVERT_DIR, filename_noext)
    tmb_path_noext = os.path.join(IMG_TMB_DIR, filename_noext)
    with Image.open(path).convert('RGBA') as im:
        show_warnings(im)
        im = im.resize((IMG_CONVERT_TO_SIZE, IMG_CONVERT_TO_SIZE))
        im.convert('RGB').save(path_noext + '.jpg', "JPEG", quality=100)
        tmb = im.resize((IMG_TMB_SIZE, IMG_TMB_SIZE))
        tmb.convert('RGB').save(tmb_path_noext + '.jpg', "JPEG", quality=100)


def main():
    if not os.path.exists(IMG_CONVERT_DIR):
        os.makedirs(IMG_CONVERT_DIR)
    if not os.path.exists(IMG_TMB_DIR):
        os.makedirs(IMG_TMB_DIR)
    
    for file in os.listdir(IMG_SOURCE_DIR):
        path = os.path.join(IMG_SOURCE_DIR, file)
        try:
            print("Processing: " + file)
            convert_image(path)
        except Exception as e:
            print("Path: "+path+" encountered error:")
            print(e)


if __name__ == '__main__':
    main()