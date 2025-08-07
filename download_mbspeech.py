import os
import requests
import zipfile

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
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
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