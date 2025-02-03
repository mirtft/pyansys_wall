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
