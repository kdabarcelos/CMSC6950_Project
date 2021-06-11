# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Karina Barcelos


### Software topic: tidynamics

Funtions:

1.

2. 

3.


### Software Setup

Prior the following steps, it is necessary to install conda with Miniforge, which can be found [here](https://github.com/conda-forge/miniforge).


Create conda environment with the software name and acitivate:   

```
conda create -n tidynamics
conda activate tidynamics
```

Install Python, NumPy, Matplotlib, and Pytest to use tidynamics:

```
conda install python numpy matplotlib pytest
```

Install tidynamics

```
conda install -c conda-forge tidynamics
```

In order to test if everything has been installed properly, first clone the tidynamics, and run the pytest in tests/:


```
git clone https://github.com/pdebuyl-lab/tidynamics
cd tidynamics/tests
python3 -m pytest
```
