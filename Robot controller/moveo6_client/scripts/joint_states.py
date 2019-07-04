#!/usr/bin/env python

import sys
import rospy
from joint_state_listener.py import *

def jointValues():
    rospy.wait_for_service('joint_state_listener')
    try:
        joint_states = rospy.ServiceProxy('joint_state_listener')
        print joint_states
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    jointValues()
