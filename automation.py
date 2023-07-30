from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ? folder to track e.g. Windows: "C:\\Users\\UserName\\Downloads"
source_dir = "/Users/lukearmstrong/Downloads"
dest_dir_sfx = "/Users/lukearmstrong/Documents/sounds"

dest_dir_documents = "/Users/lukearmstrong/Documents"
dest_dir_music = "/Users/lukearmstrong/Documents/music "
dest_dir_video = "/Users/lukearmstrong/Documents/videos"
dest_dir_image = "/Users/lukearmstrong/Documents/images"


# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

class MoverHandler(FileSystemEventHandler):
    # THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):
        for extension in audio_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):
        for extension in video_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = dest_dir_video
                move_file(dest, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):
        for extension in image_extensions:
            if name.endswith(extension) or name.endswith(extension.uppr()):
                dest = dest_dir_image
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")


        
        


