#!/bin/bash

gnome-terminal -- bash -c "source venv/bin/activate; python EthackingApp/main.py; exec bash"
