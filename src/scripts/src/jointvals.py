#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('jointvals', anonymous=True)
robot = moveit_commander.RobotCommander()
#scene = moveit_commander.PlanningSceneInterface()
group_name = "blue_arm"
red_group = moveit_commander.MoveGroupCommander(group_name)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	joint_vals=moveit_commander.move_group.MoveGroupCommander.get_current_pose(red_group)
	rospy.loginfo(joint_vals)
	rate.sleep()
