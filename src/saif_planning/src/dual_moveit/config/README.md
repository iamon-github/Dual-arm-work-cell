## Files that are being used

The key config files that configure the different controllers of the arm models in the simulation are (in no particular order):

```test_joint_state_controller.yaml```, ```t_controllers.yaml```, ```t_list.yaml```, ```gazebo_ros_control_params.yaml```, ```joint_limits.yaml```, ```kinematics.yaml```

And the semantic description of the two UR10 models used in the simulation is manifested in ```test_dual.srdf``` which corresponds to the visual description in ```t_dual.urdf``` (in **dual_arm_description/urdf/**)

Note that the white cylinders "attached" to the two arms in urdf/srdf files account for the cables that are wrapped around in the real arms and work to closely resemble the actual spatial region that motion planning processes should use.

These attached cylinders have the collision disabled with the arms to which it is attached in ```test_dual.srdf```
