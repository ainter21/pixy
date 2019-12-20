import os
import sys
import glob
from pathlib import Path
import subprocess
import shutil

def write_on_file(content: str, destination: str):
    with open(destination, 'w') as f:
        f.write(content)

def copy_folder_content_to(source_dir: str, destination_dir: str):
    files = glob.glob(source_dir + '/*')
    print(files)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for f in files:
        shutil.copy2(f, destination_dir)

def execute_pixy(php_file_path: str, output_folder: str):
    print("Processing", php_file_path)
    result = subprocess.run(['bash', 'run.sh', php_file_path], stdout=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8')
    base_filename = os.path.basename(php_file_path)
    php_filename = os.path.splitext(base_filename)[0]
    print(php_filename)
    write_on_file(stdout, './graphs/' + php_filename + '_stdout.log')
    copy_folder_content_to('./graphs', output_folder)

# get input_folder parameter
input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not input_folder.endswith('/'):
    input_folder += '/'

if not os.path.exists(input_folder):
    print("Path", input_folder, "does not exist")

# for each php file
for filename in Path(input_folder).glob('**/*.php'):
    execute_pixy(filename, output_folder)