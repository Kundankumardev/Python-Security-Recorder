🛡 Security Snapshot System (Python)

A lightweight background security tool that captures webcam + screen snapshots at regular intervals and always keeps the last 15 minutes of images, even if the computer shuts down unexpectedly.

Unlike video recording, this system saves individual images, making it much more reliable during sudden power loss.

🎯 Features

📸 Captures webcam images

🖥 Captures full screen images

🧩 Combines camera + screen side-by-side

⏱ Takes snapshots every 1 second (configurable)

🕒 Keeps only the last 15 minutes of images

♻ Automatically deletes old snapshots

🕵 Can run silently in the background

🚀 Can start automatically with Windows

🗓 Timestamp printed on every image

📦 Requirements

Install Python 3.9+ and run:

pip install opencv-python mss numpy pyinstaller

▶ Run Manually
python security_snapshot.py


Snapshots will be saved in the snapshots/ folder.

📁 Output Structure
project_folder/
│
├── security_snapshot.py
├── snapshots/
│   ├── 2026-01-29_21-10-01.jpg
│   ├── 2026-01-29_21-10-02.jpg
│   └── (only last 15 minutes kept)


Each image contains:

Webcam view

Screen capture

Timestamp

⚙ How It Works

Captures webcam frame

Captures current screen

Merges both into one image

Saves as JPG with timestamp

Deletes images older than 15 minutes

Because each image is saved instantly, no data is lost if the system shuts down suddenly.

🕵 Run Silently in Background
Build Hidden EXE
pyinstaller --noconsole --onefile security_snapshot.py


The executable will be created in:

dist/security_snapshot.exe


This version runs with no terminal window.

🚀 Start Automatically on Windows Boot
Method 1 — Startup Folder

Press Win + R

Type: shell:startup

Copy security_snapshot.exe into that folder

Method 2 — Task Scheduler (Recommended)

Open Task Scheduler

Click Create Task

Name it: System Snapshot Service

Trigger: At log on

Action: Start a program → select the EXE

Enable:

✔ Run whether user is logged in or not

✔ Run with highest privileges

🛠 Configurable Settings (Inside Script)
INTERVAL = 1          # seconds between snapshots
KEEP_MINUTES = 15     # how long to keep images

CAM_WIDTH = 640
CAM_HEIGHT = 480

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

💾 Storage Note

If capturing every second:

~60 images per minute

~900 images for 15 minutes

Make sure you have enough disk space.

🚧 Possible Future Upgrades

Motion-based snapshots only when movement is detected

Automatic cloud backup

Send alerts with snapshot to phone/email

Blur screen area for privacy

Multiple camera support

⚠ Disclaimer

This project is for educational and personal security use only.
Recording people or screens without permission may be illegal in some areas. Always follow local laws and privacy regulations.