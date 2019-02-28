#!/usr/bin/env python

#Project ALVIN (Autonomous Logic Virtual Intelligence n' Navigation)

import rospy
import roslib
from gps_common.msg import GPSFix
from geometry_msgs.msg import Twist
listener_nodo='gpsfake'

gpsData = GPSFix()
dataChanged = 0

def callback(data):
    global gpsData
    global dataChanged
    gpsData.latitude = (round(data.linear.x/100))+((data.linear.x/100)-(round (data.linear.x/100)))*100/60
    gpsData.longitude = -((round(data.linear.y/100))+((data.linear.y/100)-(round (data.linear.y/100)))*100/60)
    gpsData.track = data.linear.z
    dataChanged = 1


def GpsMapper():

    global gpsData
    global dataChanged

    pub = rospy.Publisher('GPS', GPSFix, queue_size=10)
    rospy.init_node('GPSMapviz', anonymous=True)
    rospy.Subscriber(listener_nodo,Twist,callback)

    while not rospy.is_shutdown():
        if dataChanged:
            #rospy.loginfo(gpsData)
            pub.publish(gpsData)
            dataChanged = 0


if __name__ == '__main__':
    try:
        GpsMapper()

    except rospy.ROSInterruptException:
        pass
