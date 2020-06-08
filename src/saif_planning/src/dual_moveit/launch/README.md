## Naming of the files

The files that launch the empty world in Gazebo and spawns the models (after being given the description of those in the other files) and launches the **config** files to configure the controllers were initially named without the prefix **test**.

Copies of the key files were made to trace the development in the working simulations and **test_** was added in their names. This work was initially not done on GitHub, so, this was one way to keep track of the versions in the local workstation.

After cloning, the names can obviously be changed to make them convenient to use in different files but the names should also be changed in the files where they are referenced (for example, **test_gazebo.launch** is called in **test.launch**). Otherwise, the simulation will not run and may display an error saying that the file could not be found.

## Files that are being used

The key launch files that call the different config files and are used in the development of the simulation of dual-arm workcell are:

```test.launch```, ```test_gazebo.launch```, ```test_ros_controllers.launch```, ```test_controller_utils.launch```, ```test_trajectory_execution.launch.xml```, ```test_move_group.launch```, ```planning_context.launch```, ```moveit_rviz.launch```, ```moveit.rviz```
