from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from app.organizer import move_file


class FileHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)  # wait for file to fully save
            print(f"[DETECTED] {event.src_path}")
            move_file(event.src_path, self.directory)


class Watcher:
    def __init__(self):
        self.observer = None

    def start(self, directory):
        if self.observer:
            print("Watcher already running")
            return

        event_handler = FileHandler(directory)
        self.observer = Observer()
        self.observer.schedule(event_handler, directory, recursive=False)
        self.observer.start()

        print(f"[STARTED] Watching: {directory}")

    def stop(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None
            print("[STOPPED] Watcher stopped")