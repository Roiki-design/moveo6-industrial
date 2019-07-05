#! /usr/bin/env python

import rospy
from actionlib import*
from moveo6_client import*

f = SimpleActionServer(simple_action_server, execute_cb=None, auto_start=True)

goal = f.accept_new_goal()
goal_available = f.is_new_goal_available()
print(goal)
print(goal_available)
