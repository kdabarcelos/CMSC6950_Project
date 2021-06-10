# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Karina Barcelos

##Pymagicc Software Ssetup

First, you will need to have a conda installation such as Miniforge installed.

Then proceed with the following commands:

```
conda create -n pymagicc
conda activate pymagicc
conda install pymagicc
```

Clone the third-party software repo:

```
git clone https://github.com/openscm/pymagicc.git

cd pymagicc
make venv
./venv/bin/pip install --editable .
./venv/bin/jupyter-notebook notebooks/Example.ipynb
```
