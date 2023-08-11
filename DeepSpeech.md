# JETSON NANO
This is a step-by-step guide on setting up a jetson nano(also with the ssh method).
We will also cover performing inferencing on the jetson nano.

## Setup for Jetson Nano
Steps taken to set up the Jetson Nano.If you are not familiar with the it's important you follow the [link](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)

### Jetson Nano OS setup
* The Jetson Nano OS can be setup following the [Jetson Orin Nano Developer Kit Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#prepare).
* You can follow the youtube [tutorial](https://youtube.com/playlist?list=PLGs0VKk2DiYxP-ElZ7-QXIERFFPkOuP4_) by Paul McWhorter for hands on experience with Jetson.

### Conda installation on Jetson Nano 
Since Archiconda3 is tailored for ARM64 computer (Raspberry Pi, Jetson Devices), the setup process is different from the one with the normal Anaconda. To start off, please follow the setup instructions below:
The [git_repo](https://github.com/yqlbu/archiconda3/tree/master)
#### Setup
Download the installation script and run it.
```
wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh
sudo sh Archiconda3-0.2.3-Linux-aarch64.sh
```
Then

```
cd ~
sudo chown -R $USER archiconda3/
export "PATH=/bin:/usr/bin:$PATH" >> ~/.bashrc 
source ~/.bashrc
conda config --add channels conda-forge
conda -V
```
The conda version should be displayed at the end of the setup.

### How to create and delete a conda environment
```
conda create --name venv (replace venv in your preference)
```

To create an environment with a specific version of Python
```
$ conda create -n venv python=3.6 (replace venv in your preference)
```

To delete an environment
```
$ conda remove -n envname --all (replace envname in your preference)
```
To remove an environment
```
To remove an environment
```
Grant the current user permission
```
$ sudo chown -R username <PATH\TO>/archiconda
```

### Activate/Deactivate the environment
To activate the environment
```
$ conda activate envname (replace envname in your preference)
```

To deactivate the environment
```
$ conda deactivate
```

To prevent conda from activating the base environment by default when terminal opens
```
conda config --set auto_activate_base false
```

For running Jupyter lab/notebook from your client machine , edge device and package installation with conda check the [git_repo](https://github.com/yqlbu/archiconda3/tree/master)

