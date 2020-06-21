#!/usr/bin/bash

echo -n "Enter the username to start the installation: "
 read user

echo "Installation is starting"

apt update 

apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 -y
apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 -y
apt install nautilus -y

cp /home/$user/mattos-codec-base64/Install/mattos-codec-base64.desktop /home/$user/Área\ de\ trabalho/
cp /home/$user/mattos-codec-base64/mattos-codec-base64.pyc /usr/share/applications/
chmod  +x /home/$user/Área\ de\ trabalho/mattos-codec-base64.desktop
chmod +x /usr/share/applications/mattos-codec-base64.pyc

echo "Installation completed"
