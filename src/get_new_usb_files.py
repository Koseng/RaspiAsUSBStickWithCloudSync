import os, subprocess, shutil, time

def get_files_since_point_in_time(rootdir, pointInTime):
    allFiles = []
    for item in os.scandir(rootdir):
        if item.is_file() and (item.stat().st_mtime > pointInTime):          
            allFiles.append(item.path)          
        elif item.is_dir():             
            if (item.stat().st_atime > pointInTime): # continue in folder if it was accessed
                get_files_since_point_in_time(item, pointInTime)
    return allFiles

# WORK IN PROGRESS
fileToCheck = "c:/temp/test.txt"
sourceDir = '/mnt/usb_share'
destinationDir = '~/transfer'
lastModifyTime = os.stat(fileToCheck).st_mtime

while (True):
    currentModifyTime = os.stat(fileToCheck).st_mtime
    if (currentModifyTime > lastModifyTime):        
        subprocess.call(['sudo', 'modprobe', '-r', 'g_mass_storage'])        
        subprocess.call(['sudo', 'mount', '-a'])
        time.sleep(1)        
        newFiles = get_files_since_point_in_time(sourceDir, lastModifyTime)
        paths = [shutil.copy2(file, destinationDir) for file in newFiles]        
        subprocess.call(['sudo', 'umount', '-f', sourceDir]) # -f force
        subprocess.call(['sudo', 'modprobe', 'g_mass_storage', 'file=/piusb.bin', 'stall=0', 'removable=y', 'iSerialNumber=1234567890'])      
        lastModifyTime = currentModifyTime
    else:
        time.sleep(5)