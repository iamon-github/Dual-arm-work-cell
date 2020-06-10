This folder holds planning modules and moveit configuration for the robot.

## Planning

To spawn the models in Gazebo and rviz, just run in the terminal:

```
roslaunch dual_moveit test.launch
```
Now, to test whether the controllers are working, try running the following command in another terminal (which is a basic Python code for moving the two arms to a particular coordinate):

```
rosrun scripts task1.py
```
___
After running the above two commands, the two arms in Gazebo will move something like this

<img align="down" alt="" src="https://github.com/iamon-github/Dual-arm-work-cell/blob/master/docs/images/running_simulation.gif" width="450" />
