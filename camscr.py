import cv2
import numpy as np
import os
import time
from datetime import datetime
import mss

# ========== SETTINGS ==========
SAVE_FOLDER = "recordings"
FPS = 15
CHUNK_DURATION = 60          # 1 minute per file
MAX_MINUTES_TO_KEEP = 15
CAMERA_INDEX = 0

CAM_WIDTH = 640
CAM_HEIGHT = 480

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# ==============================

os.makedirs(SAVE_FOLDER, exist_ok=True)
sct = mss.mss()

def delete_old_files():
    files = sorted(
        [f for f in os.listdir(SAVE_FOLDER) if f.endswith(".avi")],
        key=lambda x: os.path.getctime(os.path.join(SAVE_FOLDER, x))
    )
    while len(files) > MAX_MINUTES_TO_KEEP:
        old = files.pop(0)
        os.remove(os.path.join(SAVE_FOLDER, old))
        print(f"Deleted old file: {old}")

def get_new_writer(width, height):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_FOLDER, f"{timestamp}.avi")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(filename, fourcc, FPS, (width, height))
    print(f"Started recording: {filename}")
    return writer

def capture_screen():
    monitor = sct.monitors[1]  # Primary monitor
    img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    frame = cv2.resize(frame, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return frame

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    if not cap.isOpened():
        print("Camera not accessible")
        return

    combined_width = CAM_WIDTH + SCREEN_WIDTH
    combined_height = max(CAM_HEIGHT, SCREEN_HEIGHT)

    writer = get_new_writer(combined_width, combined_height)
    start_time = time.time()

    try:
        while True:
            loop_start = time.time()

            # Capture webcam
            ret, cam_frame = cap.read()
            if not ret:
                print("Camera frame failed")
                break
            cam_frame = cv2.resize(cam_frame, (CAM_WIDTH, CAM_HEIGHT))

            # Capture screen
            screen_frame = capture_screen()

            # Combine side-by-side
            combined = np.hstack((cam_frame, screen_frame))

            # Timestamp overlay
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(combined, timestamp, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            writer.write(combined)

            cv2.imshow("Security Recorder (Cam + Screen)", combined)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Start new chunk every minute
            if time.time() - start_time >= CHUNK_DURATION:
                writer.release()
                delete_old_files()
                writer = get_new_writer(combined_width, combined_height)
                start_time = time.time()

            # Maintain 15 FPS
            elapsed = time.time() - loop_start
            sleep_time = max(0, (1 / FPS) - elapsed)
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        writer.release()
        cap.release()
        cv2.destroyAllWindows()
        delete_old_files()

if __name__ == "__main__":
    main()
