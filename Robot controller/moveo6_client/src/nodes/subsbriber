#!/usr/bin/env python
import rospy
import std_msgs.msgs
import joint_state_listener


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('program_listener', anonymous=True)

    states = rospy.Subscriber("joint_states", float64, callback)
    path_command = rospy.Subscriber("join_path_command",float64 , callback)
    print(states)
    print(path_command)
    sleep(2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
