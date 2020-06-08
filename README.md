# Safe AI for surgical assistance

<img align="right" alt="" src="https://github.com/ipab-rad/saifer-surgery/blob/master/docs/images/front.png" width="400" />  As AI based decision-making methods make their way from internet applications to more safety-critical physical systems, questions about the robustness of the models and policies become increasingly more important. This project is developing methods to address this through novel methods for learning specifications from human experts and synthesising policies that are correct by construction. These developments are grounded in the domain of surgical assistance with autonomous robots in the operating room.

## Requirements:

Ubuntu 16.04, ROS Kinetic
## Installation:

- Install the [required packages](https://github.com/ipab-rad/saifer-surgery/wiki/Required-packages), clone this repository, and
```
cd saifer-surgery
git submodule update --init --recursive
catkin_make
source devel/setup.bash
```
___
## Current functionality 
### (Warning: this is semi-functional research code under active development):

___
### Motion planning and control

<img align="right" alt="" src="https://github.com/ipab-rad/saifer-surgery/blob/master/docs/images/arms.gif" width="150" /> [Launch arms](https://github.com/ipab-rad/saifer-surgery/tree/master/src/saif_ui/saifer_launch), plan and execute using MoveIt!
```
roslaunch saifer_launch dual.launch
```

___

### 3D mouse control with spacenav

<img align="right" alt="" src="http://wiki.ros.org/spacenav_node?action=AttachFile&do=get&target=spacenav.png" width="120" /> Inverse dynamics on the red arm, with gripper opening and closing. See the [spacenav_teleop](./src/saif_control/spacenav_teleop) node for more detail.
```
roslaunch saifer_launch dual.launch
roslaunch spacenav_teleop teleop.launch
```

___
### User defined contour following

<img align="right" alt="" src="https://github.com/ipab-rad/saifer-surgery/blob/master/src/saif_ui/contour_launch/ims/surface.gif" width="150" /> Select a pointcloud region in Rviz and follow this surface using MoveIt! Cartesian waypoint following and position control. This requires calibrated offsets depending on the tool used for contour following. See the [contour launch](./src/saif_ui/contour_launch) node for more detail.
```
roslaunch contour_launch contour.launch
```


___
### Kinesthetic demonstration

<img align="right" alt="" src="https://github.com/ipab-rad/saifer-surgery/blob/master/src/saif_control/ft_compliance/ims/demo.gif" width="150" />Physically move red arm (only red has this functionality at present, to avoid risk of crushing blue camera. Make sure to zero the ft sensor before using. See the [ft_compliance](./src/saif_control/ft_compliance) node for more detail.
```
rosservice call /red/robotiq_ft_sensor_acc "command_id: 0 command: 'SET ZRO'"
roslaunch ft_compliance compliance.launch
```

___
### Autonomous ultrasound scanning

<img align="right" alt="" src="https://github.com/ipab-rad/saifer-surgery/blob/master/docs/images/scan.gif" width="150"/>This app uses Bayesian optimisation to move an ultrasound scanner over an ultrasound imaging phantom in search of a tumour like object. The app relies on a reward model learned from demonstration ultrasound image sequences using the [visual IRL](https://github.com/ipab-rad/saifer-surgery/tree/irl/src/saif_learning/visual_irl) package. 

Launch robot and ultrasound image streamer
```
roslaunch saifer_launch dual.launch
roslaunch ultrasound_epiphan us.launch
rosrun ultrasound_imager pairwise_ultrasound_scanner.py
```


