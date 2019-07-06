#! /usr/bin/env python

import rospy

import actionlib

from action_server.msg import*

class ServerAction(object):
    # create messages that are used to publish feedback/result
    _feedback = action_server.msg.JointTrajectoryFeedback()
    _result = action_server.msg.JointTrajectoryResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self.action_name, action_server.msg.JointTrajectoryAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        
        
        # start executing the action
        for i in range(1, goal.order):
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
          
        if success:
            self._result.sequence = self._feedback.sequence
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('moveo6_action_server')
    server = JointTrajectoryAction(rospy.get_name())
    rospy.spin()
