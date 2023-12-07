# RaspiAsUSBStickWithCloudSync

A [Raspberry Pi Zero W](https://rpilocator.com/) is used as a USB Stick with integrated cloud syncronization. All files written to the USB drive are either copied to a Dropbox account or another linux server. Power is supplied by the USB port. 

![Overview pic](doc/img/overview.png)

This can be used in conjunction with a camera system which has the possibility to store the video files locally on a USB stick, but not in the cloud.

Each new video file is automatically uploaded to a free Dropbox account and can subsequently be viewed and replayed with the Dropbox app.

Some very basic linux skills are necessary. Should also work with "Raspberry Pi Zero 2 W". 

## Quickstart
The Micro-SD card should be at least 16GB. 

1. Install Raspberry Pi **OS Lite** (32bit) from category Raspberry Pi OS (other) with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Take note whether it is a Debian Bullseye or Debian Bookworm image.
![pi imager](doc/img/piimager.png)

- Settings (After NEXT)
    > - Set Hostname: raspberrypi.local
    > - Enable SSH with Password
    > - Username: pi
    > - Password: YOUR_PASSWORD
    > - Setup your Wifi (important)

2. Be patient on first setup boot, it might take several minutes on Pi Zero.

3. Download latest release from RaspiAsUSBStickWithCloudSync and extract files

4. Enter configuration data for Dropbox sync or linux server sync
    - [Prepare and configure Dropbox](doc/dropbox.md)
    - Configure linux server sync

5. Copy all files to `/home/pi` on the Raspberry Pi. For example use [WinSCP](https://winscp.net/eng/download.php):
    > - File protocol: SFTP
    > - Host name: raspberrypi.local
    > - User name: pi
    > - Password: YOUR_PASSWORD

6. Login to Raspberry Pi with SSH. For example use [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) with `Host name: raspberrypi.local` and `user: pi`
    - For Debian Bullseye image type and execute command: `bash /home/pi/execute_setup_bullseye.sh`
    - For Debian Brookworm image type execute command: `bash /home/pi/execute_setup_bookworm.sh`

    > [!NOTE]
    > The setup script downloads and installs necessary software components, configures driver modules as well as services and creates the USB drive image.

7. Restart and you are all set. For a first test connect the pi with it's USB port to your PC and see whether the USB drive is accessible. Create a folder with some files and check whether it is auto uploaded to configured Dropbox or linux server.

8. Connect to system of your choice, for example camera system with video sync to USB.

#### View videos in dropbox mobile app: 

![dropbox app](doc/img/dropboxapp.png)

## Diagnose
[Diagnose issues](doc/diagnose.md)

## More information
[Detailed documentation](doc/documentation.md)

### License
[GNU General Public License v3.0](LICENSE)

