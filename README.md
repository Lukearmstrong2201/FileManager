
# File Management Application

This Python script is a simple file management application that monitors a specified directory for changes and organizes files into different directories based on their types.

## Features

- Automatically organizes files into the following categories:
  - Audio files
  - Video files
  - Image files
  - Document files

- Provides support for various file extensions within each category.

## Requirements

- Python 3.x
- Required Python packages (install using `pip install watchdog`):
  - watchdog

## Usage

1. Clone or download the repository to your local machine.

2. Install the required dependencies:

   ```bash
   pip install watchdog
Open a terminal or command prompt and navigate to the directory containing the script:
    


cd /path/to/your/script
Run the script:
    
python file_manager.py

or...

python3 file_manager.py

## Configuration

Update the following variables in the script to match your setup:

source_dir: The directory to be monitored for changes.
dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_documents: Destination directories for organizing files.

Update the following variables in the script to match your setup:

source_dir: The directory to be monitored for changes.
dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_documents: Destination directories for organizing files.
