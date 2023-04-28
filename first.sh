#!/bin/bash

apt update -y && apt upgrade -y && apt install nginx python3-pip transmission-cli transmission-daemon -y
systemctl enable transmission-daemon && systemctl start transmission-daemon
pip3 install python-telegram-bot==13.7

