import time
import sys
import random

# ----------------------------
# Generator for download chunks
# ----------------------------
def download_file(file_size_mb, chunk_size_mb):
    downloaded = 0
    while downloaded < file_size_mb:
        yield chunk_size_mb  # Har baar ek chunk bhej do
        downloaded += chunk_size_mb
        time.sleep(random.uniform(0.2, 0.5))  # Random net speed ka delay

# ----------------------------
# Progress bar function
# ----------------------------
def show_progress(downloaded, total_size):
    bar_length = 30
    filled_length = int(bar_length * downloaded // total_size)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    percent = (downloaded / total_size) * 100
    sys.stdout.write(f"\rDownloading: |{bar}| {percent:.0f}% "
                     f"({downloaded}/{total_size} MB)")
    sys.stdout.flush()

# ----------------------------
# Simulating file download
# ----------------------------
file_size = 100  # 100 MB ka file
chunk_size = 5   # Har baar 5 MB download hoga

print("📡 Starting download...\n")
downloaded_mb = 0

for chunk in download_file(file_size, chunk_size):
    downloaded_mb += chunk
    if downloaded_mb > file_size:  # Extra MB adjust
        downloaded_mb = file_size
    show_progress(downloaded_mb, file_size)

print("\n✅ Download complete!")
