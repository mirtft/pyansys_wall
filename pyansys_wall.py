# Description: This script will import the geometry of the wall and the electrical chase way into ANSYS

# # import parallels desktop api so we can call Parllels Windows 10 VM
# import prlsdkapi
# def start_parallels_vm(vm_name):
#     prlsdkapi.Initialize()
#     vm = prlsdkapi.VirtualMachine.Open(vm_name)
#     vm.Start()
# start_parallels_vm("Win10")  # Replace "VM_Name" with the actual name of your VM


# this function will start PyANSYS
from ansys.tools.path import find_mechanical
from ansys.mechanical.core import launch_mechanical
from ansys.mapdl.core import launch_mapdl
from ansys.tools.path import save_mechanical_path

import os
wbpath = os.path.join("/Volumes", "[C] Win10", "Program Files", "ANSYS Inc", "ANSYS Student", "v251", "aisol", "bin", "winx64")
wbexec_file = os.path.join(wbpath, "AnsysWBU.exe")

MAPDLpath = os.path.join("/Volumes", "[C] Win10", "Program Files", "ANSYS Inc", "ANSYS Student", "v251", "ansys", "bin", "winx64")
MAPDLexec_file = os.path.join(MAPDLpath, "MAPDL.exe")

#save_mechanical_path(wbpath)

mechanical = launch_mechanical(wbexec_file)
mapdl = launch_mapdl(MAPDLexec_file)
