# GSDMA_2021  
### O. KAUFMANN, 2021.  
  
Representation of galeries, shafts and coal seams of an old coal mine 

[![Documentation](https://readthedocs.org/projects/gsdma-2021/badge/?version=latest)](https://gsdma-2021.readthedocs.io/en/latest/?badge=latest
)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


## Table of Contents
1. [Description of the project](#Description-of-the-project)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [First steps](#First-steps)
5. [Contributing](#Contributing)
6. [License](#License)
7. [Contact](#Contact)

## Description of the project <a name="Description-of-the-project"></a>

The objective of this project is to create a 3D geometric model of a coal mine. The modeling takes place within the framework of the modeling and study of a geothermal system in former coal mines in Wallonia. Thus, the project aims to model the shafts, galleries and coal seams exploited. During the exploitation of coal, the rock collapsed behind the face, which leaves areas with high void rates, i.e. destressed zones.
This modeling will be done using georeferenced mine plans. These mine plans allow us to know the coordinates in two dimensions of the different parts studied. These coordinates are in the Lambert 72 reference system. In order to be able to model in three dimensions the elevations of the objects will have to be introduced. Thus, from raster images, the project can be vectorized in order to make geometric modeling possible.


## Prerequisites <a name="Prerequisites"></a>

The project is developed in a virtual environment using Pipenv. It is therefore necessary to install Pyenv and Pipenv before starting the installation of the program. It is also necessary to install Pyenv because pyenv will setup the virtual environment with the correct version of Python. Pipenv add the required dependencies automatically during installation.

* `install Pyenv <https://github.com/pyenv/pyenv-installer>`_
* `install Pipenv <https://pipenv.pypa.io/en/latest/install/>`_
  
## Installation <a name="Installation"></a>

To clone the repository and setup the environment for using this project
:

.. code-block:: bash

   $ git clone git@github.com:kaufmanno/gsdma_2021.git
   $ cd gsdma_2021/
   $ pipenv shell
   $ pipenv install

To view installed dependencies, see the
`Pipfile <https://github.com/kaufmanno/gsdma_2021/blob/master/Pipfile>`__.
Be aware that using *pipfile install* actually installs from the
Pipfile.lock file. Use the –skip-lock option if you want to use the
Pipfile instead.

Install the different (geopandas, pyvista, pyacd, numpy) libraries with "pip install"


## First steps <a name="First-steps"></a>  

Hello World :)
--------------

First, collecting data of galeries, shafts and coal seams  as geopackages.


A few steps further
-------------------

GSDMA_2021 is used to model the geometry of a coal mine in order to modelise several things with modeflow. It used basic functions such as drawing shafts, galeries and coal seams on basis of real data. The limits of the geometries are defined at first. Then the geometries are grided so that it is possible to assign different properties to each grid. For this assignement, a model of the surfaces based is created on the known points. Then there is an assignement of an order and a orientation for those surfaces. The main functions are exposed in the part function.

## Contributing <a name="Contributing"></a>

Author : O. KAUFMANN

Contributors : F. CAMUS, J. LELEUX & M. VAN TRIMPONT



## License <a name="License"></a>

The license of the project is avalaible on the [license](https://github.com/kaufmanno/gsdma_2021/blob/master/LICENSE) file.  



## Contact <a name="Contact"></a>

We are interested in your feedback. Please create issues for bug reports, suggestions, PR and questions.  
