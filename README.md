# Setting Up Anaconda Environment with Pandas and Pytest

This guide will walk you through the process of setting up an Anaconda environment, creating a new environment, installing Pandas, Pytest, and ipykernel, and then using it to connect to a Jupyter Notebook.

## Step 1: Install Anaconda

If you don't have Anaconda installed, download and install it from the official website: [Anaconda Downloads](https://www.anaconda.com/products/individual)

## Step 2: Create a new environment

Open a terminal and run the following command to create a new environment named `my_environment`, install Pandas, Pytest, and ipykernel, and activate the environment:

```bash
conda create --name my_environment python=3.11 pandas pytest ipykernel -y && conda activate my_environment
```

## Step 3: Activate the New Environment

In the terminal, activate your newly created environment:

```bash
conda activate my_environment
```

## Step 4: Install Pandas, Pytest, and ipykernel

Install Pandas, Pytest, and ipykernel using the following commands:

```bash
conda install pandas
conda install pytest
conda install ipykernel
```

## Step 5: Install and launch Jupyter notebook

```bash
conda install jupyterlab -y
jupyter lab
```