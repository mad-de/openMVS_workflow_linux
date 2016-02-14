# openMVS_workflow for Linux
A simple python workflow for [openMVS](https://github.com/cdcseacave/openMVS) and [openMVG](https://github.com/openMVG/openMVG)

#Usage example
```
~ cd PATH/TO/YOUR/WORKFLOW_OPENMVS
~ home=~ && python workflow_openMVS.py input_file="$home/openMVG_build/software/SfM/ImageDataset_SceauxCastle/images_out/reconstruction_global/sfm_data.json" output_dir="$home/openMVG_build/software/SfM/ImageDataset_SceauxCastle/images_out/SVM_out/" 

(Set use_densify and use_refine to "OFF" or leave them out if you prefer to skip these steps)

```
