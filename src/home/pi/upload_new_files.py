#!/usr/bin/env python

import os, subprocess, shutil, time
import logging, logging.handlers
import dropbox
from dropbox.files import WriteMode

# To Dropbox
APP_KEY = "xxxxxxxxxxxxx"
APP_SECRET = "yyyyyyyyyyyyyy"
REFRESH_TOKEN = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
DROPBOX_PATH = "/"

# To Linux Server via SCP
SCP_PATH = 'myUser@11.22.33.44:/home/myUser/transfer'

SOURCE_BASE_DIR = '/home/pi/transfer'
COPYING_ACTIVE_FILE = os.path.join(SOURCE_BASE_DIR, 'copyingActive')

def setup_logging(log_file_full_path):
    base_path = os.path.split(log_file_full_path)[0]
    if base_path: os.makedirs(base_path, exist_ok=True)
    log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    file_handler = logging.handlers.RotatingFileHandler(log_file_full_path, maxBytes=500000, backupCount=7)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)


def wait_until_no_copying_active(copy_active_file):
    max_time = 0
    while (os.path.isfile(copy_active_file)):
        time.sleep(1)
        max_time += 1
        if (max_time > 30): break
        

def transfer_via_scp(source_dir, destination):
    source_dir_content = os.path.join(source_dir, '*')
    result = subprocess.run(['expect', '-f', 'scp-copy.exp', source_dir_content, destination], capture_output=True, text=True)
    logging.info(f'{result.returncode}' f'{result.stdout}')


def get_all_files(folder):
    all_files = []
    for item in os.scandir(folder):
        if item.is_file(): all_files.append(item.path)
        elif item.is_dir(): all_files.extend(get_all_files(item.path))
    return all_files


def transfer_to_dropbox(source_dir):
    with dropbox.Dropbox(oauth2_refresh_token=REFRESH_TOKEN, app_key=APP_KEY, app_secret=APP_SECRET) as dbx:  
        all_files = get_all_files(source_dir)
        for file in all_files:
            with open(file, mode='rb') as f:
                destination_path = os.path.join(DROPBOX_PATH) + os.path.relpath(file, source_dir)
                logging.info(f"START UPLOAD Path: {destination_path}")
                file_metadata = dbx.files_upload(f.read(), destination_path, mode=WriteMode('overwrite'))
                logging.info(f"FINISH UPLOAD Metadata Path: {file_metadata.path_display}")


# todo on start initialize move everything to an archive and beging fresh

# MAIN
setup_logging("/home/pi/logs/uploadLogging.log") 
try:
    logging.info(f"----STARTED upload_new_files.py----")
    os.makedirs(SOURCE_BASE_DIR, exist_ok=True)
    while (True):
        folders_to_transfer = [d for d in os.scandir(SOURCE_BASE_DIR) if d.is_dir()]
        if folders_to_transfer:
            wait_until_no_copying_active(COPYING_ACTIVE_FILE)
            for folder in folders_to_transfer:
                # transfer_via_scp(folder, destinationSCP)
                transfer_to_dropbox(folder)
                shutil.rmtree(folder) # delete
        time.sleep(4.5)
except Exception as ex:
    logging.exception(ex)