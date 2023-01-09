#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import pandas as pd
path = '/home/noemoji041/int_catkin/src/pf_lidar_ros_driver/ok.csv'
df = pd.DataFrame()



def callback(data):
    print(data)
    list1 = list(data.ranges)
    list2 = list(data.intensities)
    df['ranges'] = list1
    df['intensities'] = list2
    list3 = []
    for i in range(len(data.ranges)):
        ray_angle = (data.angle_min + (i * data.angle_increment))
        list3.append(ray_angle)
    df['ray_angle'] = list3
    df.to_csv(path, index= False)

    
        



def start():

    rospy.init_node('LDdata')
    rate = rospy.Rate(0.000001)

    rospy.Subscriber("/scan", LaserScan, callback)

    rate.sleep()
   




    rospy.spin()





start()