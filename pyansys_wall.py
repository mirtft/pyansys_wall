# Description: This script will import the geometry of the wall and the electrical chase way into ANSYS

# this function will start PyANSYS
from ansys.tools.path import find_mechanical
from ansys.mechanical.core import launch_mechanical
from ansys.mapdl.core import launch_mapdl
from ansys.tools.path import save_mechanical_path
save_mechanical_path('192.168.18.33)
#save_mechanical_path('/Users/s/Applications\ \(Parallels\)/\{1fe107cd-77f8-4a53-ad5d-e40531ed3584\}\ Applications.localized/') #Workbench\ 2025\ R1.app/')
find_mechanical()
mechanical = launch_mechanical()
mapdl = launch_mapdl()
