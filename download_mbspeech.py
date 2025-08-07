import os
import requests
import zipfile
import shutil

from tqdm import tqdm
from pathlib import Path

DOWNLOAD_URL = "https://audio.dbs.org/KHKMUBS_DAVR_FB_N.zip"
# DOWNLOAD_URL = "https://audio.dbs.org/KHKMUBS_DAVR_FB_N.zip?download=true"
ZIP_FILENAME = "KHKMUBS_DAVR_FB_N.zip"
EXTRACT_DIR = "KHKMUBS_DAVR_FB_N"


def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


def get_bible_book_to_folder(extract_dir, book, folder_name):
    folder = Path(folder_name)
    folder.mkdir(exist_ok=True)
    extract_dir = Path(extract_dir)
    for file in extract_dir.glob(f"{book}*.mp3"):
        shutil.move(file, folder / file.name)

    print(f"Successfully moved {book} files into {folder_name} folder.")


def main():
    if not os.path.exists(ZIP_FILENAME):
        print(f"Downloading {ZIP_FILENAME}...")
        download_file(DOWNLOAD_URL, ZIP_FILENAME)
    else:
        print(f"{ZIP_FILENAME} already exists. Skipping download.")

    if not os.path.exists(EXTRACT_DIR):
        print(f"Extracting {ZIP_FILENAME} to {EXTRACT_DIR}...")
        unzip_file(ZIP_FILENAME, EXTRACT_DIR)
    else:
        print(f"{EXTRACT_DIR} already exists. Skipping extraction.")

    # same as `dl_and_preprop_dataset.py` in https://github.com/tugstugi/pytorch-dc-tts/blob/master/dl_and_preprop_dataset.py
    bible_books = ["01_Genesis", "02_Exodus", "03_Leviticus"]
    for bible_book in bible_books:
        get_bible_book_to_folder(
            extract_dir=EXTRACT_DIR, book=bible_book, folder_name=bible_book
        )

    # Now zip it.
    for bible_book in bible_books:
        shutil.make_archive(bible_book, "zip", bible_book)
        print(f"Zipped {bible_book} folder.")


if __name__ == "__main__":
    main()
