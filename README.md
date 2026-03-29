# Auto-File-Organizer
An event-driven file automation API that monitors directories and organizes files in real-time using FastAPI and watchdog


---

## ✨ Features

- 📂 Real-time file detection using watchdog
- ⚡ Automatic file categorization (documents, images, videos, music)
- 🔄 Background file processing
- 🎛️ API control (start/stop/status)
- 🛡️ Safe file handling (prevents overwrite)

---

## 🧠 How It Works

1. API starts a watcher on a directory
2. System listens for new files
3. File is categorized based on extension
4. File is moved into the appropriate folder

---

## 📁 Example

### Before:


downloads/
report.pdf
song.mp3
image.png


### After:


downloads/
documents/report.pdf
music/song.mp3
images/image.png


---

## 🛠️ Tech Stack

- FastAPI
- Watchdog
- Python (os, shutil)

---


📌 Future Improvements

Custom file rules via API
File renaming logic
Recursive directory support
Logging system
Web dashboard
👨‍💻 Author

Built as a practical automation project using FastAPI.

---

## 🚀 Getting Started

### 1. Clone repo

```bash
git clone https://github.com/your-username/auto-file-organizer.git
cd auto-file-organizer

---

2. Install dependencies
pip install -r requirements.txt

---

3. Run server
uvicorn app.main:app --reload

---

4. Open Swagger UI
http://127.0.0.1:8000/docs
📡 API Endpoints
▶️ Start Organizer

POST /start

{
  "directory": "C:/Users/YourName/Downloads"
}
⏹️ Stop Organizer

POST /stop

📊 Get Status

GET /status
