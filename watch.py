import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys

class RestartHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(self.command)

    def on_modified(self, event):
        # Pantau semua perubahan file
        print(f"Detected change in {event.src_path}, restarting...")
        self.start_process()

if __name__ == "__main__":
    path = "."
    command = [sys.executable, "main.py"]

    event_handler = RestartHandler(command)
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
