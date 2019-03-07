#!/bin/bash
sudo apt update
sudo apt install openssh-server x11vnc* wmctrl python3-pip -y
pip3 install stormssh cerberus configparser pexpect sshconf -y
