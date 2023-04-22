import os
import shutil

# Source and destination folder paths
# !!! If you're not running the script from the "script" folder this path will not work !!!
src_folder = '../data/original_images'
dest_folder = '../data/renamed_images'

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Iterate through all the files in the source folder
i = 1
for filename in os.listdir(src_folder):
    new_filename = str(i) + '.jpg'
    shutil.copy(os.path.join(src_folder, filename), os.path.join(dest_folder, new_filename))
    i += 1