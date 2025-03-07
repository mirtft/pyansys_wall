
def run_explode():
    from explode_assembly import explode
    explode('narrow_am_inex_wall_v2.assembly.json')

def launch_pyansys():
    # this function will start PyANSYS
    from ansys.mapdl.core import launch_mapdl

    mapdl = launch_mapdl()

#def import_electrical():
    # this will import the eletrical chaseway geometry as a beam in ANSYS
    

# run_explode()
launch_pyansys
