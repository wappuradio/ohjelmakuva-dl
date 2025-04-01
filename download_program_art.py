"""
ISSUE WITH DRIVE LINKS: gdown got ratelimited by Google and couldn't download any more
- needed to use cookies from browser as specified by https://github.com/wkentaro/gdown?tab=readme-ov-file#faq
Using "Get cookies.txt locally" Chrome addon, downloaded cookies.txt with a drive link open.
Placing cookies.txt to ~/.cache/gdown/cookies.txt allows gdown to use browser cookies and remain in
Google's good graces
"""
import shutil
import os
import gdown
import csv
from utils import program_name_to_filename

SKIP_DUPLICATES = False
IMG_DOWNLOAD_DIR = "./img_downloads"

DEFAULT_CSV_PATH = "ohjelmakuvat.csv"
DEFAULT_IMG_LINK_FORMAT = "drive"
DEFAULT_TITLE_INDEX = 1
DEFAULT_LINK_INDEX = 2


def download_img(download_link, download_dir, filename_without_ext, img_link_format):
    """
    Downloads and correctly renames image-files from links
    """
    if img_link_format != 'drive':
        raise(NotImplementedError("Only Google-drive links supported! Please implement support"))
    
    filename = gdown.download(url=download_link, fuzzy=True, quiet=False)
    name, ext = os.path.splitext(filename)
    # Rename the file
    shutil.move(filename, os.path.join(download_dir, filename_without_ext + ext))


def handle_row(row, title_index, link_index, img_link_format):
    program_name = row[title_index]
    download_link = row[link_index]

    print("Downloading program: " + row[title_index] + "\nFrom: " + row[link_index])
    filename_without_ext = program_name_to_filename(program_name)
    print("Converted name: " + filename_without_ext)

    if (SKIP_DUPLICATES and (
            os.path.exists(os.path.join(IMG_DOWNLOAD_DIR, filename_without_ext + ".jpg"))
            or os.path.exists(os.path.join(IMG_DOWNLOAD_DIR, filename_without_ext + ".png"))
            )):
        print("Already downloaded! Skipping")
        return

    file_path = download_img(download_link, IMG_DOWNLOAD_DIR, filename_without_ext, img_link_format)


def main(csv_path, title_index, link_index, img_link_format):
    # Prepare input and output directory
    if not os.path.exists(IMG_DOWNLOAD_DIR):
        os.makedirs(IMG_DOWNLOAD_DIR)

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(reader):
            if i == 0: continue # Skip header
            handle_row(row, title_index, link_index, img_link_format)

if __name__ == '__main__':
    main(DEFAULT_CSV_PATH, DEFAULT_TITLE_INDEX, DEFAULT_LINK_INDEX, DEFAULT_IMG_LINK_FORMAT)