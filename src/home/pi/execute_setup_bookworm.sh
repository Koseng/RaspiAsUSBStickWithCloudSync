#! /bin/sh
echo "-----------------------------------------------------------------"
echo "Create configuration for loading otg usb drivers on boot"
echo "-----------------------------------------------------------------"
sudo grep -qxF '#otg_mode=1' /boot/firmware/config.txt || sudo sed -i '/^otg_mode=1/s/^/#/' /boot/firmware/config.txt
sudo sh -c "grep -qxF 'dtoverlay=dwc2' /boot/firmware/config.txt || echo 'dtoverlay=dwc2' >> /boot/firmware/config.txt"
sudo sh -c "grep -qxF 'dwc2' /etc/modules || echo 'dwc2' >> /etc/modules"
echo "Done"

echo "-----------------------------------------------------------------"
echo "Create the 3GB USB share"
echo "-----------------------------------------------------------------"
echo "Create the 3GB USB image file - BE PATIENT FOR SEVERAL MINUTES"
sudo dd bs=1M if=/dev/zero of=/piusb.bin count=3072 # create file
echo 'type=07' | sudo sfdisk /piusb.bin # create exfat primary partition
loopd=$(sudo losetup --partscan --show --find /piusb.bin) # create loop device
sudo mkfs.exfat -L Raspi "${loopd}p1" # format with exfat
sudo mkdir -p /mnt/usb_share

echo "-----------------------------------------------------------------"
echo "Prepare python copy and upload services"
echo "-----------------------------------------------------------------"
sudo apt-get update
sudo apt-get -y install expect
sudo apt-get -y install python3-dropbox

echo "-----------------------------------------------------------------"
echo "Add system services"
echo "-----------------------------------------------------------------"
# [ -f ...] checks whether file exists, only then mv is executed
[ -f "/home/pi/usb-storage.service" ] && sudo mv /home/pi/usb-storage.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/usb-storage.service
sudo systemctl enable usb-storage.service
[ -f "/home/pi/usb-copy.service" ] && sudo mv /home/pi/usb-copy.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/usb-copy.service
sudo systemctl enable usb-copy.service
[ -f "/home/pi/usb-upload.service" ] &&  sudo mv /home/pi/usb-upload.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/usb-upload.service
sudo systemctl enable usb-upload.service
