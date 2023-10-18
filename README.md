# RaspiAsUSBStickWithCloudSync

![Overview pic](doc/overview.png)

A Raspberry Pi Zero W is used as a USB Stick with integrated cloud sync. All files written to the USB drive are either copied to a Dropbox account or another linux server. Power is supplied by USB port. 

For example, this can  be used with camera systems where videos are synced to a local USB stick. Each new video file is automatically uploaded to a free Dropbox account and can be viewed and replayed with the Dropbox app.

Some very basic linux skills are necessary.

## Quickstart WIP
Scripts and manual are prepared for Debian Bookworm based Raspberry image. Micro-SD card should be at least 16GB. 
1. [Get](https://rpilocator.com/) and install a Raspberry Pi Zero W with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). 
    - CHOOSE OS: Raspberry Pi OS (other) -> Raspberry Pi OS Lite (32bit)
    - CHOOSE STORAGE
    - Settings (Gear Symbol)
        - Set Hostname: raspberrypi.local
        - Enable SSH with Password
        - Username: pi
        - Password: YOUR_PASSWORD
        - Setup your Wifi (important)
    - WRITE
2. Download latest release from RaspiAsUSBStickWithCloudSync and extract files
3. Adapt files for Dropbox sync or linux server sync
    - Create and configure Dropbox
    - Configure linux server sync
4. Power up your Raspberry Pi Zero W. First startup might take some time.
5. Copy all files to `/home/pi` on the Raspberry Pi. For example use [WinSCP](https://winscp.net/eng/download.php):
    - File protocol: SFTP
    - Host name: raspberrypi.local
    - User name: pi
    - Password: YOUR_PASSWORD
6. Login to Raspberry Pi with SSH and execute command `bash /home/pi/execute_setup.sh`.
For example use [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) with Host name: raspberrypi.local and user: pi
> The setup script downloads and installs necessary software components, configures driver modules as well as services and creates the USB drive image.
7. Restart and you are all set. For a first test connect the pi with it's USB port to your PC and see whether the USB drive is accessible. Create a folder with some files and check whether it is auto uploaded to configured Dropbox or linux server.
8. Connect to system of your choice, for example camera system with sync to USB.



## Diagnose
- Wifi
- Log Files
- Mount test

## More information
xx

### License

