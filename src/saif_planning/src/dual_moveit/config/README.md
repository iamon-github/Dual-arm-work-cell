## Files that are being used

The key config files that configure the different controllers of the arm models in the simulation are (in no particular order):

```test_joint_state_controller.yaml```, ```t_controllers.yaml```, ```t_list.yaml```, ```gazebo_ros_control_params.yaml```, ```joint_limits.yaml```, ```kinematics.yaml```

And the semantic description of the two UR10 models used in the simulation is manifested in ```test_dual.srdf``` which corresponds to the visual description in ```t_dual.urdf``` (in **dual_arm_description/urdf/**)

Note that the white cylinders "attached" to the two arms in urdf/srdf files account for the cables that are wrapped around in the real arms and work to closely resemble the actual spatial region that motion planning processes should use.

These cylinders have the collision disabled with the arms to which it is attached in ```test_dual.srdf```

There is a fine difference between ```t_list.yaml``` and ```t_controllers.yaml``` :  
```t_controllers.yaml``` is for the simulated robot/Gazebo plugin side
```t_list.yaml``` is for the MoveIt! side (moveit controller manager) and this can work after the controllers are up in the simulator (Gazebo in our case)
So, it is essential to have both the YAML files (with the correct reference to the namespaces which is **dual** in our case) in order for the controllers to actuate the joint in the simulation.

---
## Function of the key YAML files

```gazebo_ros_control_params.yaml```
- Specifies the pid values of different joints

```t_list.yaml```
- Controller manager that defines which controller controls which joint/group of joints

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Here, in our simulation, each controller controls a single joint.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note also that every controller has **dual** defined as its namespace becuase our model has two arms (which we refer to as blue  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and red arm) which are a part of dual arm (workcell).

```t_controllers.yaml```
- This YAML file defines that the controllers are in the **dual** namespace and also defines other characteristics such as the joints that they control, pid values and the constraints on goal time.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note that all the controllers are defined as effort_controllers (except the controllers that move the gripper joints)
