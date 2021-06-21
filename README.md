# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Karina Barcelos

---
### Project topic: tidynamics

Functions:

1. Serve as a reference implementation for common algorithms that are useful for molecular and stochastic simulations.

2. Performs the computation of mean-square displacements and correlation functions using the Fast Correlation Algorithm.

---
### Conda Software Setup

Prior the tidynamics setup, it is necessary to install conda from Miniforge installer, which can be found to download [here](https://github.com/conda-forge/miniforge). After copy the appropriate link regarding your OS and architeture, run as below:

```
wget [past the link here replacing within and the brackets]
bash Miniforge3-Linux-x86_64.sh
```

Check if conda has been properly installed with `--version`:

```
conda --version
```
----
### Tidynamics Software and Dependencies Setup

Then create conda environment with the chosen software name and activate:   

```
conda create -n tidynamics
conda activate tidynamics
```

Install Python, NumPy, Matplotlib, Pytest, and Pandas (dependencies) to use tidynamics:

```
conda install python numpy matplotlib pytest pandas pytrends
```

Install tidynamics:

```
conda install -c conda-forge tidynamics
```
---
### Tidynamics Testing

In order to test if everything has been installed properly, first clone the tidynamics, and run the pytest in tests/:

```
git clone https://github.com/pdebuyl-lab/tidynamics
cd tidynamics/tests/
python3 -m pytest
```
---
