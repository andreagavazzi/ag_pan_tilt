#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory

rospy.init_node('head_controller')
rospy.loginfo('Tracker node started.')

# crea oggetto bridge e il publisher per le coordinate
head_pub = rospy.Publisher('joints', JointTrajectory, queue_size=1)

# funzione callback
def callback(data):
    try:
    
    blablabla
    
    joints = JointTrajectory()
    
    blablabla
    
    joints.name = ['pan', 'tilt']
    joints.positions = [1, 0.5]
    
    head_pub.publish(joints)    
    
    except CvBridgeError, e:
    print e


def main():
    # Sottoscrive lo stato dei dyna e pubblica il movimento
    camera_sub = rospy.Subscriber("/dynamixel_State", dyna_state, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        # TODO: migliorare uscita dal programma
        print 'Process shutting down'
        cv2.destroyAllWindows()


# Main routine
if __name__ == '__main__':
    main()
