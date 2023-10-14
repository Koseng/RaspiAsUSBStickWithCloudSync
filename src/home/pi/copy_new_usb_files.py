#!/usr/bin/env python

import os, subprocess, shutil, time
import logging, logging.handlers
from pathlib import Path

USB_IMAGE_FILE = '/piusb.bin'
SOURCE_DIR = '/mnt/usb_share'
DESTINATION_BASE_DIR = '/home/pi/transfer'
COPYING_ACTIVE_FILE = os.path.join(DESTINATION_BASE_DIR, 'copyingActive')

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


def get_files_since_point_in_time(start_dir, point_in_time, newest_dir_count):
    all_files = []
    directories = []
    for item in os.scandir(start_dir):
        if item.is_file() and (max(item.stat().st_mtime, item.stat().st_ctime) > point_in_time):
            all_files.append(item.path)
        elif item.is_dir():
            directories.append(item)
    # Continue for the newest_dir_count newest folders in current directory
    directories.sort(key=lambda d: d.stat().st_mtime, reverse=True)
    for i in range(newest_dir_count):
        if len(directories) > i:
            all_files.extend(get_files_since_point_in_time(directories[i], point_in_time, newest_dir_count))
    return all_files


def copy_file_with_directory_structure(source_base_path, source_file_path, dest_base_path):
    relative_path = os.path.relpath(source_file_path, source_base_path)
    destination_path =  os.path.join(dest_base_path, os.path.dirname(relative_path))
    logging.info(f"Copy {source_file_path} to {destination_path}")
    os.makedirs(destination_path, exist_ok=True)
    shutil.copy2(source_file_path, destination_path)

# MAIN
setup_logging("/home/pi/logs/copyLogging.log") 
try:
    logging.info(f"----STARTED copy_new_usb_files.py----")
    last_modify_time = os.stat(USB_IMAGE_FILE).st_mtime
    while (True):
        current_modify_time = os.stat(USB_IMAGE_FILE).st_mtime
        destinationDir = os.path.join(DESTINATION_BASE_DIR, str(int(current_modify_time)))
        if (current_modify_time > last_modify_time):
            subprocess.call(['sudo', 'mount', SOURCE_DIR])
            time.sleep(0.5)
            new_files = get_files_since_point_in_time(SOURCE_DIR, last_modify_time, newest_dir_count=2)
            Path(COPYING_ACTIVE_FILE).touch()
            for file in new_files:
                copy_file_with_directory_structure(SOURCE_DIR, file, destinationDir)
            if os.path.isfile(COPYING_ACTIVE_FILE):
                os.remove(COPYING_ACTIVE_FILE)
            subprocess.call(['sudo', 'umount', '-f', SOURCE_DIR]) # -f force
            time.sleep(0.5)
            last_modify_time = os.stat(USB_IMAGE_FILE).st_mtime
        else:
            time.sleep(3)
except Exception as ex:
    logging.exception(ex)

