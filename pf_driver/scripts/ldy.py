#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import pandas as pd
path = '/home/noemoji041/int_catkin/src/pf_lidar_ros_driver/pf_driver/data/ok.csv'
df = pd.DataFrame()



def callback(data):
    list1 = list(data.ranges)
    list2 = list(data.intensities)
    df['ranges'] = list1
    df['intensities'] = list2
    list3 = []
    for i in range(len(data.ranges)):
        ray_angle = (data.angle_min + (i * data.angle_increment))*57.2957795131
        list3.append(ray_angle)
    df['ray_angle'] = list3
    df.to_csv(path, index= False)

    
        



def start():
    rospy.init_node('LDdata')
    rospy.Subscriber("/scan", LaserScan, callback)
   




    rospy.spin()





start()