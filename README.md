# RaspiAsUSBStickWithCloudSync

## Raspberry Pi Zero W as USB stick

For using Linux USB "On-The-Go" (OTG)  with the Raspberry Pi Zero W, a different USB driver is necessary. The standard heavily patched and performance oriented driver does not support OTG mode. Instead the dwc2 driver needs to be used.

For OTG mode there are different [gadget drivers](http://www.linux-usb.org/gadget/). A Raspberry Pi Zero W can behave like an USB stick with the [g_mass_storage](https://www.kernel.org/doc/Documentation/usb/mass-storage.txt) driver. A more complex alternative is using libcomposite with configfs.

### Load the driver

> In `/boot/config.txt` comment out `otg_mode` and add `dtoverlay=dwc2`

```
sudo sed -i '/^otg_mode=1/s/^/#/' /boot/config.txt
sudo sh -c "echo 'dtoverlay=dwc2' >> /boot/config.txt"
```

> In `/etc/modules` add `dwc2`:

```
sudo sh -c "echo 'dwc2' >> /etc/modules"
```

### Create the 2GB USB share

> First install packages for exfat file system. Then create and format usb image file piusb.bin. Finally prepare mounting.

 ```
sudo apt-get install exfat-fuse
sudo apt-get install exfat-utils
sudo dd bs=1M if=/dev/zero of=/piusb.bin count=2048 # create file
sudo mkfs.exfat /piusb.bin # format
sudo mkdir /mnt/usb_share
```
> In `/etc/fstab` add `/piusb.bin /mnt/usb_share exfat noauto,nofail,users,umask=000 0 2`
```
sudo sh -c "echo '/piusb.bin /mnt/usb_share exfat noauto,nofail,users,umask=000 0 2' >> /etc/fstab"
```

### Activate USB mass storage
Create system service to activate USB mass storage at the very end of the boot process. Therefore setting the type to idle is important. 

Copy `usb-storage.service` to `/etc/systemd/system/` then
```
sudo chmod 644 /etc/systemd/system/usb-storage.service
sudo systemctl enable usb-storage.service
```


 


