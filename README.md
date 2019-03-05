# nano-extravasation
Program that runs a diffusive simulation in vasculature data from tumors. More generally however, it can be used to simulate the diffusion on a substance in some complicated geometrical environment using an Euler method. Where the code lacks in efficiency, it makes up for in simplicity and quick customization.

## Theory

See Supplementary of main paper.

## Requirements

This module runs on Python 2.7.15. Please check requirements.txt for the proper dependencies. If you have pip, you can install all dependencies using the command

`pip install -r /path/to/requirements.txt`

## Structure

This project has the following architecture:

`/home`
  * `/model`
  * `/figures`
  * `/data`
    * `/gaps_100x`
    * `/thresh_vessels`
    * `/tissure_boundary`
  * `/sim`

This repository does not contain any of the data that is necessary to run these simulation, you will have to create a '/data' directory as above and download the necessary files from [here](https://figshare.com/articles/Annotated_TEM_images_of_blood_vessels_in_tumours/7485770). You can do so manually (follow link, download extravasationfinalsimgs.zip and unzip the contents into the data folder as above) or if you are running a Linux based system simply run the `download_data.sh` script in terminal and it will take care of the download.

For Windows users who want to use scripts, see below [^1].

I will not go into the details of how the code runs here, but will briefly explain how it works: models of diffusion are described in `/models`, each of them with the name `[something]_model.py`. These models are classes, in which the geometry of the problem is defined (boundaries, sources, sinks, etc.). For now, the physical dynamics that are described in these classes are diffusion, sinks, sources and different boundary conditions (Neumann, Dirichlet). The simulation is run in `/models/main.py` and certain time points of the simulations are saved in `/sim`.

## Initialization and Running

Simulations as written now should take 1 hour to run and are not too intensive.

### Linux/macOS

A lot of this code can be run using the scripts provided in the `/home` directory.

If you're savvy enough, you can run the commands you find inside the scripts, notably (from inside the `/models` directory):

`python2 main.py -m parent_model`

### Windows

Windows does not have built in support for .sh files, however you have Cygwin installed, you will be able to run all the same commands in such a terminal.

Unless you have the proper support to run the scripts, you will have to run the commands in your favourite IDE for Python to simulate the nanoparticle extravasation. To run simulations, go to the `/model` directory and run

`python2 main.py -m parent_model`

## Customization

You do not need a full understanding of the code to customize certain parameters in the simulations in `/model/parameters.py`. Notably, to run any of the 12 different simulations that are in `/data`, you can change the tumor image (158,159,160) and the stack (1,2,3,4):

~~~python
#IMAGE LOADING
TUMOR_IMAGE = 160 # 158, 159 or 160
STACK = 2 # 1, 2, 3 or 4
NUM_HOLES = 5000 # anything you'd like really
~~~
You'll notice there's also a line where you can define the number of holes in the simulation.

Additionally there are other parameters one could play around with, such as diffusion coefficient, spacing, runtime and many more!

For the very brave, there is a `hopping_model.py` that can be used instead of `parent_model.py` to actually make the holes move around. This describes the dynamics in which the holes are openning in one location only for a short period of time, closing only for other holes to appear somewhere else.

Much more can be done with this skeleton of code.

## Visualization

For now, all you need to do is run

`python2 figure1.py`

from the directory `/figures`. You need to specify which simulation you want to visualize in `/figures/figure1.py` in the line 50

~~~python
main('parent_model_tumor160_stack2', time='2D1800.0')
~~~

and can change which slice you want to visualizehigher up in the code.



## Future work
* Jupyter notebook for visualization AND analyzing data.
* Jupyter notebook for running simulation???
* Add more features? customization, templates for different simulations/generalizations?
* Extending this to current work

[^1]: Windows does not have built in support for .sh files, however if you have Cygwin installed, you will be able to run all the same commands in such a terminal. You can also get the proper support from using Git bash in Windows, I'm not sure how Cygwin or Git bash have access to Python interpretters, but it seems doable.
