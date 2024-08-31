#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exec sudo bash "$0" "$@"
  exit
fi

gnome-terminal -- bash -c "source venv/bin/activate; python EthackingApp/main.py; exec bash"
