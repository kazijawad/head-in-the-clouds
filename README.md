# CycleGAN

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

```
Python 3.8.x
```

### Installing

A step by step guide that tell you how to get a development environment running.

1. Clone the repository:

```bash
git clone https://github.com/kazijawad/cycle-gan.git
```

2. Install necessary packages, an [Anaconda](https://www.anaconda.com) environment is recommended:

```bash
# Python Packages
conda create -n p-cycle-gan python=3.8
conda activate p-cycle-gan
pip install tensorflow tensorflow-datasets notebook matplotlib ipywidgets
```

3. Install custom dataset:

```bash
cd datasets/clouds
tfds build
cd ../people
tfds build
```

3. Run the application:

```bash
jupyter notebook
```
