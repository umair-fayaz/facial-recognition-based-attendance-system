import time
import cv2
import tester
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

directory = r'../../../../'

class Watcher:
    DIRECTORY_TO_WATCH = "image_cache/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.

            # imgPath = event.src_path+'.JPEG'
            # print(imgPath)
            print("----- STARTING DETECTION -----")
            tester.mainFunction(event.src_path)
            os.chdir(directory)
            print("----- ALIGNING FACES -----")
            subprocess.call(['./face_allignment.sh'])
            print("----- ALIGNING FACES FINISHED-----")
            print("----- MATCHING FACES-----")
            subprocess.call(['./match_faces.sh'])
            print("##################################################")

        # elif event.event_type == 'modified':
        #     # Taken any action here when a file is modified.
        #     print(event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()
