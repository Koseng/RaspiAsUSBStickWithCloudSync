import os, subprocess, shutil, time

password = 'myPassword'
sourceBaseDir = '/home/pi/transfer'
sourceDir = os.path.join(sourceBaseDir, 'totransfer')
destination = 'myUser@11.22.33.44:/home/myUser/transfer'
copyingActiveFile = os.path.join(sourceBaseDir, 'copyingActive')

def wait_until_no_copying_active(copyActiveFile):
    maxTime = 0
    while (os.path.isfile(copyActiveFile)):        
        time.sleep(1)
        maxTime += 1
        if (maxTime > 30): break

def transfer_via_scp(password, sourceDir, destination):
    subprocess.call(['sshpass', '-p', f'{password}', 'scp', '-r', sourceDir, destination])     

while (True):
    foldersToTransfer = [d for d in os.scandir(sourceDir) if d.is_dir()]        
    if foldersToTransfer:
        wait_until_no_copying_active(copyingActiveFile)
        for folder in foldersToTransfer:
            transfer_via_scp(password, folder, destination) 
            shutil.rmtree(folder) # delete  
    time.sleep(4.5)