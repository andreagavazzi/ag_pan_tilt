#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelStateList

rospy.init_node('head_controller')
rospy.loginfo('Tracker node started.')

# crea oggetto bridge e il publisher per le coordinate
head_pub = rospy.Publisher('joint_trajectory', JointTrajectory, queue_size=1)


# funzione callback
def callback(data):

    jp = JointTrajectoryPoint()
    jp.positions = [0, 0] # in ordine definito dal names
    jp.velocities = []
    jp.accelerations = []
    jp.effort = []

    print jp

    joints = JointTrajectory()
    joints.header.stamp = rospy.Time.now()
    joints.header.frame_id = '/base_link'
    joints.joint_names = ['pan', 'tilt']
    joints.points.append(jp)

    head_pub.publish(joints)
    

def main():
    # Sottoscrive lo stato dei dyna e pubblica il movimento
    camera_sub = rospy.Subscriber("/dynamixel_state", DynamixelStateList, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        # TODO: migliorare uscita dal programma
        print 'Process shutting down'


# Main routine
if __name__ == '__main__':
    main()
