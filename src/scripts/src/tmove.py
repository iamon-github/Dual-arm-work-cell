#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
from moveit_msgs.msg import RobotState, Constraints, OrientationConstraint
import geometry_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('tmove', anonymous=True)
robot = moveit_commander.RobotCommander()
#scene = moveit_commander.PlanningSceneInterface()
group_name = "blue_arm"
group = moveit_commander.MoveGroupCommander(group_name)

#constraints = Constraints()
#constraints.name = "Ko"
#end_effector_link = group.get_end_effector_link()
#start_pose = group.get_current_pose(end_effector_link)
#orientation_constraint = OrientationConstraint()
#orientation_constraint.header = start_pose.header
#orientation_constraint.link_name = group.get_end_effector_link()
#orientation_constraint.orientation.w = 1.0
#orientation_constraint.absolute_x_axis_tolerance = 0.1
#orientation_constraint.absolute_y_axis_tolerance = 0.1
#orientation_constraint.absolute_z_axis_tolerance = 0.14
#constraints.orientation_constraints.append(orientation_constraint)
#group.set_path_constraints(constraints)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

joint_vals=moveit_commander.move_group.MoveGroupCommander.get_current_joint_values(group)

#rospy.set_param('/move_group/trajectory_execution/allowed_start_tolerance', 0.0)
joint_vals[0]=-1.0
joint_vals[4]=-0.0004
group.set_joint_value_target(joint_vals)
plan=group.go(wait=True)
rospy.sleep(3.0)