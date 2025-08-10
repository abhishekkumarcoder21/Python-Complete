import time

# ----------------------------
# Video streaming generator
# ----------------------------
def stream_video(total_frames):
    for frame in range(1, total_frames + 1):
        yield f"🎞 Frame {frame}"  # Ek frame bhejo
        time.sleep(0.5)  # Thoda delay, jaise real streaming

# ----------------------------
# Watching the video
# ----------------------------
print("📡 Starting YouTube stream...\n")
for frame in stream_video(5):  # Sirf 5 frames ka example
    print(frame)

print("\n✅ Video finished!")
