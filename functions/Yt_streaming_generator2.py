import time
import sys

# ----------------------------
# Generator for download
# ----------------------------
def youtube_download(total_parts):
    for part in range(1, total_parts + 1):
        yield part  # Ek part download hone ke baad bhej do
        time.sleep(0.3)  # Download time ka delay

# ----------------------------
# Show progress bar
# ----------------------------
def show_progress(current, total):
    bar_length = 20  # Progress bar ka size
    filled_length = int(bar_length * current // total)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    percent = (current / total) * 100
    sys.stdout.write(f"\rDownloading: |{bar}| {percent:.0f}%")
    sys.stdout.flush()

# ----------------------------
# Simulating YouTube video download
# ----------------------------
total_parts = 30
print("📡 Starting YouTube video download...\n")

for part in youtube_download(total_parts):
    show_progress(part, total_parts)

print("\n✅ Download complete!")
