#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from std_msgs.msg import String
import math

def talker():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(24) 


	
    while not rospy.is_shutdown():
		position = JointState()
		position.header = Header()
		position.header.stamp = rospy.Time.now()
		position.name = ['base_to_head', 'head_to_right_hand', 'head_to_left_hand','r_joint_to_head','l_joint_to_head','l_joint_to_left_leg','r_joint_to_right_leg']

		position.velocity = []
		position.effort = []

		animVal = rospy.get_time() % 6.28
		animVal -= 3.14
		rospy.loginfo(animVal)
		position.position = [abs(animVal/15),abs(animVal/5),abs(animVal/5),abs(animVal/2),abs(animVal/20),abs(animVal/10),abs(animVal/10)]
		pub.publish(position)
		rate.sleep()
	

	
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass