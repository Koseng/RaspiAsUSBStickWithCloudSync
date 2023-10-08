import os, subprocess, shutil, time
from pathlib import Path

def get_files_since_point_in_time(rootdir, pointInTime, newestDirCount):
    allFiles = []
    directories = []
    for item in os.scandir(rootdir):
        if item.is_file() and (item.stat().st_mtime > pointInTime):          
            allFiles.append(item.path)
        elif item.is_dir():
            directories.append(item)                    
    # Continue for the newestDirCount newest folders in current directory
    directories.sort(key=lambda d: d.stat().st_mtime, reverse=True)
    for i in range(newestDirCount):
        if len(directories) > i:
            allFiles.extend(get_files_since_point_in_time(directories[i], pointInTime, newestDirCount))
    return allFiles


def copy_file_with_directory_structure(sourceBasePath, sourceFile, destBasePath):
    relativePath = os.path.relpath(sourceFile, sourceBasePath)   
    dstPath =  os.path.join(destBasePath, os.path.dirname(relativePath))
    os.makedirs(dstPath, exist_ok=True)
    shutil.copy2(sourceFile, dstPath)

def aquire_lock(lockFile):
    if os.path.isfile(lockFile):
        time.sleep(0.2)
    else:
        Path(lockFile).touch()

def release_lock(lockFile):
    if os.path.isfile(lockFile):
        os.remove(lockFile) 

# WORK IN PROGRESS
fileToCheck = "c:/temp/test.txt"  # /piusb.bin
sourceDir = 'c:/temp/'
destinationDir = 'c:/dest/'
# sourceDir = '/mnt/usb_share'
# destinationDir = '~/transfer'
lastModifyTime = os.stat(fileToCheck).st_mtime
lockFile = os.path.join(destinationDir, 'lock')

while (True):
    currentModifyTime = os.stat(fileToCheck).st_mtime
    if (currentModifyTime > lastModifyTime):        
        aquire_lock(lockFile)
        # subprocess.call(['sudo', 'modprobe', '-r', 'g_mass_storage'])        
        # subprocess.call(['sudo', 'mount', sourceDir])
        time.sleep(1)        
        newFiles = get_files_since_point_in_time(sourceDir, lastModifyTime, newestDirCount=2)       
        for file in newFiles:
            copy_file_with_directory_structure(sourceDir, file, destinationDir)      
        # subprocess.call(['sudo', 'umount', '-f', sourceDir]) # -f force
        # subprocess.call(['sudo', 'modprobe', 'g_mass_storage', 'file=/piusb.bin', 'stall=0', 'removable=y', 'iSerialNumber=1234567890'])      
        release_lock(lockFile)
        lastModifyTime = currentModifyTime
    else:
        time.sleep(5)