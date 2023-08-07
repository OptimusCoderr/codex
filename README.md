# EDGE AI
Working with edge devices such as raspberrypi, jetson nano, and google coral dev board

## Table of contents
* Raspberrypi
* Jetson_Nano
* Google Development Board

## Raspberrypi
This is a step-by-step guide on setting up a raspberry pi(also with the ssh method).
We will also cover performing inferencing on the raspberrypi, with and without the coral tpu.

## Setup for raspberry pi
Steps taken to set up the raspberrypi OS.
### Installation of the pi imager and OS writing
* The pi imager should be installed on your PC.
* The pi imager can be gotten from [here](https://www.raspberrypi.com/software/).
* You can follow this installation [tutorial](https://www.youtube.com/watch?v=ntaXWS8Lk34).
* For the next step, you would need an SD card reader and SD card of at least 16GB, make sure the card reader is not in a locked state.
* Other operating system images can be downloaded from [here](https://www.raspberrypi.com/software/operating-systems/). The image used for this project was the "Raspberry Pi OS with desktop and recommended software".
  
### VNC Setup on raspberrypi
For VNC and SSH setup for raspberrypi can be done with this [link](https://thesecmaster.com/step-by-step-tutorial-to-set-up-vnc-on-raspberry-pi/).
For more on raspi configurations and documentation check this [link](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking).

For the next steps you need good knowledge of how to use a Linux terminal. This [tutorial](https://youtu.be/KQlF7IfgZ28) is recommended.

### Installing other versions of Python from Source on the pi
You can change the version as you wish but this guide is for Python Version 3.9
##### Update and Upgrade:
First, make sure your Raspberry Pi is up to date by running the following commands:
```
sudo apt update
sudo apt upgrade
```
#### Install Dependencies:
Install the dependencies required to build Python from source:
```
sudo apt install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev libreadline-dev libncurses5-dev libncursesw5-dev libgdbm-dev liblzma-dev libffi-dev uuid-dev libffi-dev liblzma-dev libsqlite3-dev libncurses5 libgdbm-compat-dev libgdbm-dev libssl-dev libreadline-gplv2-dev
```
#### Download and Compile Python:
Now, you can download and compile Python 3.9. Here's how:
```
cd ~
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
tar -xf Python-3.9.7.tgz
cd Python-3.9.7
./configure --enable-optimizations
make -j 4  # Adjust the number based on your Pi's resources
sudo make altinstall
```
#### Verify Installation:
After the installation is complete, you can verify that Python 3.9 is installed by running:
```
python3.9 --version
```
#### Cleanup:
You can remove the downloaded files to free up space:
```
cd ~
rm -rf Python-3.9.7 Python-3.9.7.tgz
```
To make use of the python version you nee to run your programs created in a virtual environment.

#### Install virtualenv (if not already installed):
Run the following command to install the virtualenv package:
```
sudo apt install python3.9-venv
```
#### Create a Virtual Environment:
Navigate to the directory where you want to create your virtual environment. For example, you might create a venv directory within your home folder:
```
cd ~
mkdir venv
```
Now, create the virtual environment by running:
```
python3.9 -m venv venv/myproject
```
Replace myproject with the name of your project. This will create a virtual environment named myproject within the venv directory

#### Activate the Virtual Environment:
To activate the virtual environment, run:
```
source venv/myproject/bin/activate
```
Now you can run your python programs with your new python version in the virtual envrionment.

## Inferencing on the Raspberrypi
Model or AI inferencing on the raspberrypi can be done from [here](https://www.tensorflow.org/lite/examples). Select the examples Tensorflow has made specially for the raspberrypi.
For steps on using the coral tpu stick with the raspberrypi, check the [github repo](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/raspberry_pi)








