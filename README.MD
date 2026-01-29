🛡 Python Security Recorder

A lightweight background security system that records webcam + screen continuously and always keeps the last 15 minutes of footage, even if the system shuts down unexpectedly.

🎯 Features

🎥 Records webcam video

🖥 Records full screen activity

🕒 Captures at 15 FPS

💾 Saves recordings in 1-minute chunks

♻ Automatically deletes old clips (keeps last 15 minutes only)

🧠 Works as a rolling buffer system

🕵 Runs silently in the background

🚀 Starts automatically when Windows boots

🗓 Timestamp overlay on all recordings

📦 Requirements

Install Python 3.9+ and run:

pip install opencv-python mss numpy pyinstaller

▶ How to Run Manually
python security_recorder.py


Recordings will be saved inside the recordings/ folder.

📁 Output Structure
project_folder/
│
├── security_recorder.py
├── recordings/
│   ├── 2026-01-29_21-10-00.avi
│   ├── 2026-01-29_21-11-00.avi
│   └── (only last 15 files kept)


Each file = 1 minute of recording.

⚙ How It Works

The app:

Records camera + screen side-by-side

Saves video into 1-minute files

Keeps only the most recent 15 files

Deletes older files automatically

So at any moment, you always have the last 15 minutes of activity saved.

🕵 Run Silently in Background
Build Hidden EXE
pyinstaller --noconsole --onefile security_recorder.py


The EXE will be created inside:

dist/security_recorder.exe


This version runs with no terminal window.

🚀 Start Automatically on Windows Boot
Method 1 — Startup Folder

Press Win + R

Type: shell:startup

Copy security_recorder.exe into that folder

Method 2 — Task Scheduler (Recommended)

Open Task Scheduler

Click Create Task

Name it: System Security Service

Trigger: At log on

Action: Start a program → select the EXE

Enable:

✔ Run whether user is logged in or not

✔ Run with highest privileges

🔒 Privacy & Storage Notes

Videos are stored locally on your computer

Make sure you have enough disk space

You can change resolution or FPS in the script settings

🛠 Configurable Settings (Inside Script)
FPS = 15
CHUNK_DURATION = 60        # seconds per file
MAX_MINUTES_TO_KEEP = 15
CAM_WIDTH = 640
CAM_HEIGHT = 480
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

🚧 Future Improvements (Optional)

Motion detection recording

Cloud backup (Google Drive / Dropbox)

Email or Telegram alerts

Password-protected video viewer

Multiple camera support

⚠ Disclaimer

This project is for educational and personal security use only.
Make sure you comply with local laws before recording people or screens.