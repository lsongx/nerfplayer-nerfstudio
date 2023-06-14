<!-- Adapted from https://github.com/kerrj/lerf -->

# NeRFPlayer: A Streamable Dynamic Scene Representation with Decomposed Neural Radiance Fields
This is an nerfstudio framework based implementation for [NeRFPlayer](https://lsongx.github.io/projects/nerfplayer.html).


[![NeRFPlayer Video](https://img.youtube.com/vi/flVqSLZWBMI/0.jpg)](https://www.youtube.com/watch?v=flVqSLZWBMI)


# Installation
NeRFPlayer follows the integration guidelines described [here](https://docs.nerf.studio/en/latest/developer_guides/new_methods.html) for custom methods within nerfstudio. 
### 0. Install Nerfstudio dependencies
[Follow these instructions](https://docs.nerf.studio/en/latest/quickstart/installation.html) up to and including "tinycudann" to install dependencies and create an environment

### 1. Clone this repo
```git clone https://github.com/lsongx/nerfplayer-nerfstudio.git```

### 2. Install this repo as a python package
Navigate to this folder and run `python -m pip install -e .`

### 3. Run `ns-install-cli`

### Checking the install
Run `ns-train -h`: you should see a list of "subcommands" with `nerfplayer-nerfacto` and `nerfplayer-ngp` included among them.

# Using NeRFPlayer
Now that NeRFPlayer is installed you can play with it.

## Preparing data
- Currently only [DyCheck](https://hangg7.com/dycheck/) dataset is supported.
- Download [DyCheck data](https://drive.google.com/drive/folders/1cBw3CUKu2sWQfc_1LbFZGbpdQyTFzDEX).
- You can capture your own scenes by following [DyCheck's guide](https://github.com/KAIR-BAIR/dycheck/blob/main/docs/RECORD3D_CAPTURE.md).

## Run
- Launch training with `ns-train nerfplayer-ngp --data <data_folder>`. This specifies a data folder to use.
    - example: `ns-train nerfplayer-ngp --data dycheck/mochi-high-five/`
- Connect to the viewer by forwarding the viewer port, and click the link to `viewer.nerf.studio` provided in the output of the train script

# Misc
### Issues
Please open Github issues (under this repo, not under nerfstudio) for any installation/usage problems you run into.
#### Known TODOs
- [ ] Multi-camera datasets: DyNeRF, ImmersiveVideo
- [ ] Decomposition in NeRFPlayer. Under nerfstudio's framework, we got NaN soon if a decomposition module is used.
