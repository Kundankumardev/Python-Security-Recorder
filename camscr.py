import cv2
import numpy as np
import os
import time
from datetime import datetime, timedelta
import mss

# ========== SETTINGS ==========
SAVE_FOLDER = "snapshots"
INTERVAL = 1                # seconds between snapshots
KEEP_MINUTES = 15           # keep last 15 minutes
CAMERA_INDEX = 0

CAM_WIDTH = 640
CAM_HEIGHT = 480

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# ==============================

os.makedirs(SAVE_FOLDER, exist_ok=True)
sct = mss.mss()

def delete_old_images():
    cutoff_time = datetime.now() - timedelta(minutes=KEEP_MINUTES)

    for filename in os.listdir(SAVE_FOLDER):
        if filename.endswith(".jpg"):
            filepath = os.path.join(SAVE_FOLDER, filename)
            file_time = datetime.fromtimestamp(os.path.getctime(filepath))
            if file_time < cutoff_time:
                os.remove(filepath)
                print(f"Deleted old snapshot: {filename}")

def capture_screen():
    monitor = sct.monitors[1]
    img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return cv2.resize(frame, (SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

    if not cap.isOpened():
        print("Camera not accessible")
        return

    print("Security snapshot system running...")

    try:
        while True:
            start_time = time.time()

            # Capture camera
            ret, cam_frame = cap.read()
            if not ret:
                print("Camera read failed")
                break
            cam_frame = cv2.resize(cam_frame, (CAM_WIDTH, CAM_HEIGHT))

            # Capture screen
            screen_frame = capture_screen()

            # Combine images side-by-side
            combined = np.hstack((cam_frame, screen_frame))

            # Timestamp
            timestamp_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(combined, timestamp_text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Save image
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
            filepath = os.path.join(SAVE_FOLDER, filename)
            cv2.imwrite(filepath, combined)

            delete_old_images()

            # Wait until next interval
            elapsed = time.time() - start_time
            time.sleep(max(0, INTERVAL - elapsed))

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        cap.release()

if __name__ == "__main__":
    main()
