#!/usr/bin/python
#! -*- encoding: utf-8 -*-

# A basic workflow for OpenMVS

import commands
import os
import subprocess
import sys
import re

# Define global vars

def get_parent_dir(directory):
    import os
    return os.path.dirname(directory)

# Initialize vars
user_vars = { };
dict_field = "";

# Fill dictionary with index and field
for num in sys.argv[1:]:
 dict_name = re.findall(r'\w+\ ?(?=\=)',num);
 dict_field = num.replace(dict_name[0] + "=", "")
 user_vars.update({dict_name[0] : dict_field});

# Check if necessary vars are set
if not "use_densify" in user_vars:
 user_vars["use_densify"] = "OFF";

if not "use_refine" in user_vars:
 user_vars["use_refine"] = "OFF";

# Indicate the openMVS binary directory
OPENMVS_BIN = os.path.join(os.path.expanduser('~'), "openMVS_build/bin")

if not os.path.exists(user_vars["output_dir"]):
 os.mkdir(user_vars["output_dir"])

# 1. Import
pMVSImport = subprocess.Popen( [os.path.join(OPENMVS_BIN, "InterfaceOpenMVG"),  "-i", user_vars["input_file"], "-o", os.path.join(user_vars["output_dir"], "scene.mvs")] )
pMVSImport.wait()

if os.path.exists(os.path.join(user_vars["output_dir"], "scene.mvs")):
 still_working = 1;
else:
 print "Import went wrong :/";
 still_working = 0;

 # 2. Densify Point Cloud (optional)
if still_working == 1 and user_vars["use_densify"] == "ON":
 pMVSDensify = subprocess.Popen( [os.path.join(OPENMVS_BIN, "DensifyPointCloud"),  "-i", os.path.join(user_vars["output_dir"], "scene.mvs"), "-o", os.path.join(user_vars["output_dir"], "scene_dense.mvs")] )
 pMVSDensify.wait()

 if not os.path.exists(os.path.join(user_vars["output_dir"], "scene_dense.mvs")):
  print "Densify went wrong :/";
  still_working = 0;

# 3. Reconstruct Meshes
if user_vars["use_densify"] == "ON":
 this_input_file = "scene_dense.mvs";
else:
 this_input_file = "scene.mvs";

if still_working == 1:
 pMVSReconstruct = subprocess.Popen( [os.path.join(OPENMVS_BIN, "ReconstructMesh"),  "-i", os.path.join(user_vars["output_dir"], this_input_file), "-o", os.path.join(user_vars["output_dir"], "scene_mesh.mvs")] )
 pMVSReconstruct.wait()

 if not os.path.exists(os.path.join(user_vars["output_dir"], "scene_mesh.mvs")):
  print "Reconstruct went wrong :/";
  still_working = 0;

# 4. Refine Meshes (optional)
if still_working == 1 and user_vars["use_refine"] == "ON":
 pMVSRefine = subprocess.Popen( [os.path.join(OPENMVS_BIN, "RefineMesh"),  "-i", os.path.join(user_vars["output_dir"], "scene_mesh.mvs"), "-o", os.path.join(user_vars["output_dir"], "scene_dense_mesh.mvs")] )
 pMVSRefine.wait()

 if not os.path.exists(os.path.join(user_vars["output_dir"], "scene_dense_mesh.mvs")):
  print "Refine went wrong :/";
  still_working = 0;

# 5. Texture Meshes
if user_vars["use_refine"] == "ON":
 this_input_file = "scene_dense_mesh.mvs";
else:
 this_input_file = "scene_mesh.mvs";

if still_working == 1:
 pMVSRefine = subprocess.Popen( [os.path.join(OPENMVS_BIN, "TextureMesh"),  "-i", os.path.join(user_vars["output_dir"], this_input_file), "-o", os.path.join(user_vars["output_dir"], "scene_dense_mesh_texture.mvs")] )
 pMVSRefine.wait()

 if os.path.exists(os.path.join(user_vars["output_dir"], "scene_dense_mesh_texture.mvs")):
  print "Finished :)";
 else:
  print "Texturing went wrong :/";
