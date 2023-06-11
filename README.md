# Hands-on tutorial on data analysis and numerical modeling

## Objective
The present lecture is intended for you to accomplish the following objectives:
- Learn how to set up a conda environment
- Get a little experience of scripting using PyCharm IDE
- Understand a selected subset of the basic principles of Python language and apply them for data analysis using pandas library
- Have a quick look at a simple model for behavioral tracking data

### Terminology
**python** computer programming language

**interpreter**
program to read and execute code

**PyCharm**
integrated development environment (IDE): software application that helps programmers develop software code

**module**
a python file: ending with .py

**package**
collection of modules: useful code that has already been written by others

**pip**
package manager

**environment**
allow to isolate Python development projects from your system installed Python and other Python environments. Gives full control of your project and makes it easily reproducible.

**Anaconda**
helps you create an environment for many different versions of Python and package versions

## Prerequisites
1. Install PyCharm and Anaconda following https://medium.com/@GalarnykMichael/setting-up-pycharm-with-anaconda-plus-installing-packages-windows-mac-db2b158bd8c
2. Download this repository as a zip file

### Create your python environment
**1. Open your terminal**

WINDOWS: press Windows key + R

macOS: press CMD + space, type in “Terminal”

Linux: press Ctrl + Alt + T


**2. Create a new environment named pyVTK and install python 3.9**

```conda create --name pyVTK python=3.10```

press ```y``` if prompted


**3. Activate the new environment to use it**

WINDOWS:
```activate py35```

LINUX, macOS:
```source activate py35```


**4. Install packages required for today**

```conda install --yes pytables matplotlib numpy pandas imageio```


**5. To update a package (e.g. matplotlib) type**

```conda update matplotlib ```

