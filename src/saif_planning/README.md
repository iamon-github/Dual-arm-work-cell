This folder holds planning modules and moveit configuration for the robot.

## Planning

To spawn the models in Gazebo and rviz, just run in the terminal:

```
roslaunch dual_moveit test.launch
```
Now, to test whether the controllers are working, try running the following command (which is a basic Python code for moving the two arms to a particular coordinate):

```
rosrun scripts task1.py
```
