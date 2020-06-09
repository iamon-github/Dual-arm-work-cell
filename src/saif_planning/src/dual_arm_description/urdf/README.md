# URDF files

URDF files provide the visual description of the robot to the simulator

In our case, we use ```t_dual.urdf``` to provide the visual description which closely resembles the dual-arm workcell and the measurements of the table, ceiling (distance between the two arms) and the two UR10 arms in the urdf are proportionate to the sizes of the actual workcell.

Though this file is not flawless and needs some work, it can be safely used for the motion planning purposes in the simulation.

If you are using a new URDF file, it is suggested to call it (instead of the current one which is ```t_dual.urdf```) in the appropriate files.
