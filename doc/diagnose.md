# Diagnose

### Cannot connect to Raspberry Pi Zero W
- Did you wait several minutes on initial setup boot before trying to connect?
- Did you set hostname to raspberrypi.local in Raspberry Pi Imager settings?
- Did you enable SSH with password in Raspberry Pi Imager settings?
- Did you enter correct WiFi id and password in Raspberry Pi Imager settings?

If any of the settings is incorrect, correct settings and write image again.

### Automatic dropbox upload not working
- Did you enter all settings correctly in config.json?
- Check **log files**:
    - `cat /home/pi/logs/uploadLogging.log`
    - `cat /home/pi/logs/copyLogging.log`
- Check for errors on boot:
    - `sudo dmesg`

### Manually execute python scripts to investigate

Stop copy and upload system services:
- `sudo systemctl status usb-copy.service`
- `sudo systemctl stop usb-copy.service`
- `sudo systemctl status usb-copy.service`
- `sudo systemctl status usb-upload.service`
- `sudo systemctl stop usb-upload.service`
- `sudo systemctl status usb-upload.service`

Execute scripts manually:
- `python3 /home/pi/copy_new_usb_files.py`
- `python3 /home/pi/upload_new_files.py`

### Useful commands for testing

Activate / Deactivate USB mass storage mode:
- `sudo modprobe -r g_mass_storage`
- `sudo modprobe g_mass_storage file=/piusb.bin stall=0 removable=y ro=0 iSerialNumber=1122334455`

Check for rogue process:
- `sudo top`



