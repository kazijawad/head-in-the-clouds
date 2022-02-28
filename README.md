# Head in the Clouds

“Head in the Clouds” is a concept inspired by the child-like pastime of finding images of faces in objects like food, cars, and buildings. The thought of generating unique images that could be represented as clouds was a concept we all agreed to when thought of, as searching for objects in clouds felt like something we all did growing up. As a final result, we wanted to take a sketch, generate it into a face, and turn the generated face into something that resembled a cloud.

![Output](https://github.com/kazijawad/head-in-the-clouds/blob/main/preview.png)

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
conda create -n p-head-in-the-clouds python=3.8
conda activate p-head-in-the-clouds
pip install tensorflow tensorflow-datasets notebook matplotlib ipywidgets
```

3. Install each custom dataset inside the `datasets` folder:

```bash
tfds build
```

3. Run the application:

```bash
jupyter notebook
```

## Built With

- [TensorFlow](https://tensorflow.org)
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
- [Houdini](https://www.sidefx.com/products/houdini)
- [Cinema 4D](https://www.maxon.net/en/cinema-4d)
- [Octane Renderer](https://home.otoy.com/render/octane-render)

## Authors

- [Kazi Jawad](https://kazijawad.com)
- [Richard Zhou](https://www.richardczhou.com)
- [Michael Kim](https://maikool.com)
