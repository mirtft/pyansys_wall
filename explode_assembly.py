# """ //mirtft: @workspace /explain 
# Workspace: The provided code is a segment from a Python script named explode_assembly.py. This script appears to handle the extraction and processing of data from a JSON file representing an assembly, potentially for a CAD (Computer-Aided Design) application. The script writes specific parts of the JSON data to files in a specified output directory.
# The first part of the code writes the `shape_step` data from the next_doc dictionary to a file. This is followed by a conditional block that checks if the `shape_stl` data is present and base64-encoded. If so, it decodes this data and writes it to a file named `geometry.stl` in the specified directory. This is useful for handling binary STL (Stereolithography) files, which are commonly used for 3D printing and CAD applications.
# The script then iterates over any child documents within the next_doc dictionary, adding them to a fringe list for further processing. This suggests a recursive or iterative approach to handle nested structures within the assembly JSON.
# A print statement at the end of the loop indicates the completion of the explosion process for the given assembly file, providing feedback to the user.
# The __HELP__ variable contains a usage message for the script, explaining how to run it from the command line. This message is displayed if the script is executed incorrectly or if an exception occurs.
# The if __name__ == "__main__": block ensures that the script runs only when executed directly, not when imported as a module. It imports the sys module to handle command-line arguments and attempts to call the explode function with the provided arguments. If an exception occurs, it prints the usage message and re raises the exception for debugging purposes. Finally, the script exits with a status code of 0, indicating successful execution. """

import json
import os
import re
import base64


def safe_name(name: str):
    return re.sub(r"[^A-Za-z0-9-_]", "_", name)


def explode(filename: str, output_dir: str = None):

    if output_dir is None:
        output_dir = "./assembly"

    print(f"Exploding {filename} assembly into directory {output_dir}...")

    os.makedirs(output_dir, exist_ok=True)

    with open(filename, "r") as f:
        assembly_doc = json.load(f)

    #
    # Assemblies are a nested JSON structure, here we just search down and dump
    # out meta/geom data at every level into a nested directory.
    #

    fringe = [(assembly_doc, output_dir)]

    while fringe:

        next_doc, parent_dir = fringe.pop(0)
        next_dir = os.path.join(parent_dir, safe_name(next_doc["name"]))
        os.makedirs(next_dir, exist_ok=True)

        meta_file = os.path.join(next_dir, "meta.json")
        with open(meta_file, "w") as f:
            json.dump(next_doc.get("metadata", {}), f, indent=2)

        if next_doc.get("obj", {}).get("shape_step"):
            step_file = os.path.join(next_dir, "geometry.step")
            with open(step_file, "w") as f:
                f.write(next_doc["obj"]["shape_step"])

        if (next_doc.get("obj", {}).get("shape_stl", {}) or {}).get("b64"):
            # STL binary data is base64-encoded in JSON
            stl_file = os.path.join(next_dir, "geometry.stl")
            with open(stl_file, "wb") as f:
                f.write(base64.b64decode(next_doc["obj"]["shape_stl"]["b64"]))

        for child_doc in next_doc.get("children", []):
            fringe.append((child_doc, next_dir))

    print(f"DONE exploding {filename} assembly into directory {output_dir}.")


__HELP__ = f"""
USAGE: {__file__} my.assembly.json [./output-dir]
""".strip()

if __name__ == "__main__":

    import sys

    try:
        explode(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    except Exception as ex:
        print("\n\n" + __HELP__ + "\n\n")
        raise ex

    sys.exit(0)
