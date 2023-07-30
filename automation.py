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

print make_uniqie('Users/lukearmstrong/Documents/Open University /TM112/TM112 TMA01/TM112 TMA01.docx', 'TM112_TMA01.zip')



