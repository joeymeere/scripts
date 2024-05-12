import os
import shutil

# Define the source and destination directories
source_dir = os.path.expanduser('~/Desktop')
dest_dir = os.path.join(source_dir, 'media')

file_types = ['.png', '.jpg', '.webp', '.mp3', '.wav', '.mp4', '.mkv', '.mov']

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Move all specified files from the Desktop to the 'images' folder
for filename in os.listdir(source_dir):
    if any(filename.lower().endswith(ext) for ext in file_types):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(dest_dir, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All files have been moved to the 'media' folder.")