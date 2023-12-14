# RaspiAsUSBStickWithCloudSync

A [Raspberry Pi Zero W](https://rpilocator.com/) is used as a USB Stick with integrated cloud syncronization. All files written to the USB drive are either copied to a Dropbox account or another linux server. Power is supplied by the USB port. 

![Overview pic](doc/img/overview.png)

This project can be used in conjunction with a camera system which has the possibility to store the video files locally on a USB stick, but not in the cloud.

Each new video file is automatically uploaded to a free Dropbox account and can subsequently be viewed and replayed with the Dropbox app.

Some very basic linux skills are necessary. Should also work with a "Raspberry Pi Zero 2 W". 

This project is open source software licensed via [GNU General Public License v3.0](LICENSE), use at your own risk.

## Quickstart
**Basic process:**
Install a Raspberry Pi Zero W, adjust project config.json, copy project files to home directory of the Raspi and execute the setup script.

The Micro-SD card should have at least 16GB. 

1. Install Raspberry Pi **OS Lite** (32bit) from category Raspberry Pi OS (other) with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Take note whether it is a Debian Bullseye or Debian Bookworm image.
![pi imager](doc/img/piimager.png)

- Settings (After NEXT)
    > - Set Hostname: raspberrypi.local
    > - Enable SSH with Password
    > - Username: pi
    > - Password: YOUR_PASSWORD
    > - Setup your Wifi (important)

2. Be patient on first setup boot, it might take several minutes on Raspi Zero.

3. Download latest [released RaspiAsUSBStickWithCloudSync.zip
](https://github.com/Koseng/RaspiAsUSBStickWithCloudSync/releases) and extract files

4. Update settings in configuration file `config.json`:

    | Entry                | Description |
    |----------------------|---------------|
    | ActivateDropboxSync  | Activate (1) or deactivate (0) sync to dropbox  |
    | Dropbox...           | [Prepare and configure for Dropbox sync](doc/dropbox.md) |

    [Click here for all possible settings.](doc/settings.md)


5. Copy all extracted and updated files from `home_pi` to `/home/pi` on the Raspberry Pi. 
    
    For example use [WinSCP](https://winscp.net/eng/download.php):
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
    - Connect the USB cable to the USB port and not to the PWR port.
    - Make sure to have a data capable USB cable and not a cable which only support power via USB.

8. Connect to system of your choice, for example camera system with video sync to USB.

#### View videos in dropbox mobile app: 

![dropbox app](doc/img/dropboxapp.png)

## Diagnose
[Diagnose issues](doc/diagnose.md)

## More information
[Detailed documentation](doc/documentation.md)


