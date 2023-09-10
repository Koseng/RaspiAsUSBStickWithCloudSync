# RaspiUsbCloudSync

## Raspberry Pi Zero W as USB stick

For using Linux USB "On-The-Go" (OTG)  with the Raspberry Pi Zero W, a different USB driver is necessary. The standard heavily patched and performance oriented driver does not support OTG mode. Instead the dwc2 driver needs to be used.

For OTG mode there are different [gadget drivers](http://www.linux-usb.org/gadget/). A Raspberry Pi Zero W can behave like an USB stick with the [g_mass_storage](https://www.kernel.org/doc/Documentation/usb/mass-storage.txt) driver. A more complex alternative is using libcomposite with configfs.

### Loading the driver

#### config.txt
In /boot/config.txt comment out otg_mode and add dtoverlay=dwc2

```
# Comment out
# otg_mode=1
dtoverlay=dwc2
```

#### cmdline.txt
After rootwait in /boot/cmdline.txt add as one line:

```modules-load=dwc2,g_mass_storage g_mass_storage.file=/piusb.bin g_mass_storage.stall=0 g_mass_storage.removable=y g_mass_storage.ro=0 g_mass_storage.iSerialNumber=1234567890```

### Creating a 2GB USB share

The content of the USB share is stored in a file called piusb.bin.

 ```
sudo apt-get install exfat-fuse
sudo apt-get install exfat-utils
sudo dd bs=1M if=/dev/zero of=/piusb.bin count=2048 # create file
sudo mkfs.exfat /piusb.bin # format

sudo mkdir /mnt/usb_share
sudo nano /etc/fstab → /piusb.bin /mnt/usb_share exfat noauto,nofail,users,umask=000 0 2
 ```


