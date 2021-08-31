# Mass zip archive extractor
# by Julian Laury

import os
import zipfile
import time

# Validate input and set a default path
def validate_input(path):
    # Sets the current directory if blank
    working_dir = os.getcwd()
    if path == '':
        path = working_dir

    # See if the given directory exists, otherwise make a new one
    try:
        os.chdir(path)
    except(OSError):
        try:
            os.chdir(os.getcwd() + os.sep + path)
            path = os.getcwd() + os.sep + path
        except(OSError):
            os.mkdir(os.getcwd() + os.sep + path)
            path = os.getcwd() + os.sep + path

    os.chdir(working_dir)
    return path


# Get the source directory from stdin
print('Source directory to extract zips from (press enter for current directory, or a name for a new directory): ')
src_dir = validate_input(input())

# Get the target directory for stdin
print('Target directory to extract zips to (press enter for current directory, or a name for a new directory): ')
target_dir = validate_input(input())

# Flag on whether or not to delete zip files after extracting
print('Delete zips after extracting? (y/n): ')
delete_after = True if input() == 'y' else False

start_time = time.time()
# Loop over items in directory and find zip files
for entry in os.listdir(src_dir):
    if (entry.endswith('.zip')):
        # Exctract zip files to stdout
        print('Extracting ' + entry + '...')
        file_path = src_dir + os.sep + entry
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)

        if (delete_after):
            os.remove(file_path)

# Print results and execution time
end_time = time.time()
print('Done (' + str(round(end_time - start_time, 3)) + ' sec)')