# OpenAI-ROS example project

This repository the necessary code for an exemplary project utilizing `openai-ros` package with Turtlebot3

## Installation

You should have the `ros-<version>-destop-full` package installed (in case of this project version is melodic). You can do this with your respective system packet manager.
You also need the `ros-melodic-turtlebot3` package for Turtlebot3 support.

### Ubuntu
`sudo apt install ros-melodic-desktop-full ros-melodic-turtlebot3`
### Arch Linux
`yay -S ros-melodic-desktop-full ros-melodic-turtlebot3`

Then add the `openai-ros` package and build the workspace:
```
cd catkin_ws_location/src
git clone https://bitbucket.org/theconstructcore/openai_ros.git
cd ../
catkin build # or whatever tool you use for building
source devel/setup.bash # or zsh/fish if you have
```
Install the OpenAI [Gym](https://github.com/openai/gym) with
`pip install gym`

## Setting up the project
Once the necessary prerequisites are installed you may clone this project:
```
cd src/
git clone https://github.com/JDuchniewicz/OpenAI-ROS.git
```

Then, assuming you want to give a custom task to the Turtlebot3 you need to do following changes to files
