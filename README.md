# pyansys_wall

# In VS Code, go to View - Appearance - Panel
# In the panel at the bottom go to Terminal
# Copy paste the non-hashed lines into terminal and hit enter to execute the line

## First Time through
# make a virtual enviroment
cd ..
cd ..

# macos
cd ./virtualenvs
python -m venv ./.PYANSYS_WALL
# windows
cd .\virtualenvs
python -m venv .\.PYANSYS_WALL

# change to the virtual enviromment directory and activate it
cd .PYANSYS_WALL
# mac os
source bin/activate
# windows, note this sets PowerShell to run as administrator for this command, and sets all scripts as unrestricted
Start-Process powershell -Verb runAs -ArgumentList "-command", "Set-ExecutionPolicy"
# in the powershell terminal that pops up, use the following commands
Unrestricted
Y
# In the original VS Code terminal use the following command
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


## Subsequent times through start here
## Skip if first time through
cd .venv
.\Scripts\Activate.ps1
cd ..

## open pyansys_wall.py
# 