# openMVS_workflow for Linux
A simple python workflow for [openMVS](https://github.com/cdcseacave/openMVS) 

#Usage example
## Getting the required sfm_data.json file to import
Make sure [openMVS](https://github.com/cdcseacave/openMVS) and [openMVG](https://github.com/openMVG/openMVG) are built and linked according to [the build instrcutions](https://github.com/cdcseacave/openMVS/blob/master/BUILD.md#linux-compilation)
Get the [OpenMVG tutorial files](https://github.com/openMVG/ImageDataset_SceauxCastle) and copy them into your software/SfM/ folder in your openMVG Build.
Run the tutorial_demo.py file in software/sfm/ (~ python tutorial_demo.py)
We will use the resulting sfm_data.json in the folder /ImageDataset_SceauxCastle/images_out/reconstruction_global/

## Running the script
```
~ git clone https://github.com/mad-de/openMVS_workflow_linux.git
~ cd openMVS_workflow_linux
~ home=~ && python workflow_openMVS.py input_file="$home/openMVG_build/software/SfM/ImageDataset_SceauxCastle/images_out/reconstruction_global/sfm_data.json" output_dir="$home/openMVG_build/software/SfM/ImageDataset_SceauxCastle/images_out/SVM_out/" 
```

## Costumize
Set use_densify and use_refine to "OFF" or leave them out if you prefer to skip these steps. 
Change input_file and output_dir to link to your desired locations
