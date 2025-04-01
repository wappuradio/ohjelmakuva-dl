# Download Wappuradio cover art from Google Drive

This can be used to retrieve Wappuradio cover art pictures that have been collected to drive through Google Forms. Script to reformat and correctly rename
all the pictures to the way they should appear on the website are also included.

TESTED TO WORK ONLY ON UBUNTU 22.04

## How to use

1. Go to Google Drive > Find directory containing the cover-art pictures > set the sharing option for THAT FOLDER ONLY to "anyone with the link"
2. Find the CSV with the Forms entries on Google Drive, download it in CSV-format to this directory as "ohjelmakuvat.csv"
3. Install python requirements with `python3 -m pip install -r requirements.txt`
4. Run the download script `python3 download_program_art.py`
  * You may run into issues with the downloader getting ratelimited. See `download_program_art.py` for potential fix using your browser cookies
5. Run the converter script `python3 convert_program_art.py`

If everything went smooth, you should now have a directory containing correctly formatted and named program art and their thumbnails.
These (at the time of writing) need to be manually uploaded (scp) to sauron.

