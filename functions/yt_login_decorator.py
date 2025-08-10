# ----------------------------
# Global login status
# ----------------------------
user_logged_in = False  # Initially, user is not logged in

# ----------------------------
# Decorator to check login
# ----------------------------
def login_required(func):
    def wrapper():
        if user_logged_in:
            func()
        else:
            print("❌ Please login first!")
    return wrapper

# ----------------------------
# Functions that need login
# ----------------------------
@login_required
def watch_video():
    print("🎥 Playing your video...")

@login_required
def upload_video():
    print("📤 Uploading your video...")

# ----------------------------
# Example flow
# ----------------------------
print("Trying to watch without login:")
watch_video()

print("\nLogging in now...")
user_logged_in = True

print("\nTrying again after login:")
watch_video()
upload_video()
