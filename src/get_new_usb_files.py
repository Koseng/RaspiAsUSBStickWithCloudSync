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
    print(f"Copy {sourceFile} to {dstPath}")
    os.makedirs(dstPath, exist_ok=True)
    shutil.copy2(sourceFile, dstPath)


fileToCheck = '/piusb.bin'
sourceDir = '/mnt/usb_share'
destinationBaseDir = '/home/pi/transfer'
copyingActiveFile = os.path.join(destinationBaseDir, 'copyingActive')
lastModifyTime = os.stat(fileToCheck).st_mtime

while (True):
    currentModifyTime = os.stat(fileToCheck).st_mtime
    destinationDir = os.path.join(destinationBaseDir, str(int(currentModifyTime)))
    if (currentModifyTime > lastModifyTime):        
        subprocess.call(['sudo', 'mount', sourceDir])
        time.sleep(0.5)
        newFiles = get_files_since_point_in_time(sourceDir, lastModifyTime, newestDirCount=2)
        Path(copyingActiveFile).touch()
        for file in newFiles:
            copy_file_with_directory_structure(sourceDir, file, destinationDir)
        if os.path.isfile(copyingActiveFile):
            os.remove(copyingActiveFile)
        subprocess.call(['sudo', 'umount', '-f', sourceDir]) # -f force    
        time.sleep(0.5)     
        lastModifyTime = os.stat(fileToCheck).st_mtime
    else:
        time.sleep(3)

