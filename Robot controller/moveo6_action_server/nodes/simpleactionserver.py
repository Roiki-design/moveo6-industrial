#! /usr/bin/env python

import roslib
roslib.load_manifest('moveo6_action_server')
import rospy
import actionlib
from moveo6_action_server.msg import*

class moveo6Server:
  def __init__(self):
    print("test1")
    self.server = actionlib.SimpleActionServer('', moveo6_action_server.msg.JointTrajectoryAction, self.execute, False)
    self.server.start()

  def execute(self, goal):
    print(goal)
    print("test2")

    f=self.is_new_goal_available()
    print(f)	
    print("test")
    
# Do lots of awesome groundbreaking robot stuff here
    self.server.set_succeeded()


if __name__ == '__main__':
  print("test3")
  rospy.init_node('moveo6_action_server')
  print("test3")
  server = moveo6Server()
  rospy.spin()
