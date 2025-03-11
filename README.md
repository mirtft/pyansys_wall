# pyansys_wall

# In VS Code, go to View - Appearance - Panel
# In the panel at the bottom go to Terminal
# Copy paste the non-hashed lines into terminal and hit enter to execute the line

# make a virtual enviroment
# macos
python -m venv ./.venv
# windows
python -m venv .\.venv

# change to the virtual enviromment directory and activate it
cd .venv
# mac os
source bin/activate
# windows, note this sets PowerShell to run as administrator for this command, and sets all scripts as unrestricted
Start-Process powershell -Verb runAs -ArgumentList "-command", "Set-ExecutionPolicy"
Unrestricted
Y
.\Scripts\Activate.ps1

# Upgrade pip
python -m pip install -U pip

# install pyansys
python -m pip install pyansys

# explode json into a folder
cd ..
# mac os
python explode_assembly.py narrow_am_inex_wall_v2.assembly.json ./
# Windows
python explode_assembly.py narrow_am_inex_wall_v2.assembly.json .\

# open pyansys_wall.py
# 