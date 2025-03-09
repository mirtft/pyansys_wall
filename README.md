# pyansys_wall

# make a virtual enviroment
python -m venv /.venv

# change to the virtual enviromment directory and activate it
cd .venv
source bin/activate

# Install pip
python -m pip install -U pip

# Upgrade pip
python -m pip install --upgrade pip

# install pyansys
python -m pip install pyansys

# explode json into a folder
python explode_assembly.py narrow_am_inex_wall_v2.assembly.json ./

# open pyansys_wall.py
# 