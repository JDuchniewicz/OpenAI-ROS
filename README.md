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
cd openai_ros
git checkout version2
cd ../../
catkin build # or whatever tool you use for building
source devel/setup.bash # or zsh/fish if you have
```
Install the OpenAI [Gym](https://github.com/openai/gym) with
`pip install gym`

## Setting up the project
#### Once the necessary prerequisites are installed you may clone this project:
```
cd src/
git clone https://github.com/JDuchniewicz/OpenAI-ROS.git
```

#### Then, assuming you want to give a custom task to the Turtlebot3 you need to do following changes to files:
Create a new directory called `turtlebot3_custom` in the `src/openai_ros/openai_ros/src/openai_ros/task_envs` folder:

`mkdir src/openai_ros/openai_ros/src/openai_ros/task_envs/turtlebot3_custom`

Copy all contents of the `task_env` folder there:

`cp -Rv task_env/ ../openai_ros/openai_ros/src/openai_ros/task_envs/turtlebot3_custom`

Patch the `task_envs_list.py` file:

`patch ../openai_ros/openai_ros/src/openai_ros/task_envs/task_envs_list.py < task_envs_list.patch`

Substitute the `openai_turtlebot3` string with `OpenAI-ROS` or whatever you chose as the name of this project.

#### Tweaking

**GUI ON/OFF** - change the parameter `gui` to either `true` or `false`
**Adding actions** - modify the `task_env/turtlebot3_custom.py` adding new actions to `_set_action` method
**Changing the map** - modify the launch files, especially `start_world.launch`
**Changing the robot** - not covered here, check [here](https://wiki.ros.org/openai_ros/TurtleBot2%20with%20openai_ros)
**Adding own training algorithm** - add own algorithm and integrate it with/create a new training script


#### Running
After building the project and sourcing new env variables changes with `source devel/setup.bash` run:
`roslaunch <name_of_this_project> <training_script>`
where `training_script` is either `start_training_v2.launch` or `start_sarsa_training.launch`.

#### Plotting results
In the `utils` directory there is a plotting script, run it and observe the results. The files with results are saved as JSON strings in the `training_results` directory
`python results.py -f <name_of_json_with_episodes>

