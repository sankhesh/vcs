#!/usr/bin/env bash
ls
pwd
export PATH=${HOME}/miniconda/bin:${PATH}
conda install -c uvcdat/label/nightly -c conda-forge -c uvcdat "vtk-cdat<7.1.0.2.10.2017.07.07" cdutil genutil dv3d "mesalib=17.1.4=3" nose image-compare flake8 matplotlib
export UVCDAT_ANONYMOUS_LOG=False
python setup.py install --old-and-unmanageable
