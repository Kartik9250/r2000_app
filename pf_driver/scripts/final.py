#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi
from matplotlib.animation import FuncAnimation
import rospy
from sensor_msgs.msg import LaserScan
import time


class lidar_plot:
	def __init__(self, scan_topic):
		# subscribing the scan topic
		print(scan_topic)
		self.scan_info = rospy.Subscriber(
			scan_topic, LaserScan, self._scan_registration)
		self.fig = plt.figure(figsize=(10,5))
		self.ax = plt.axes()
		self.ax.set_xlim(10, -15)
		self.ax.set_ylim(8, -8)
		self.scatter = self.ax.scatter([], [], s=2, color = "red")
		self.x_arr = []
		self.y_arr = []
		plt.axis("equal")
		# self.start()
		plt.grid()
		self.annot = self.ax.annotate("", xy=(0,0), xytext=(10,10), textcoords='offset points',
					  bbox=dict(boxstyle='round', fc='w'))
		self.annot.set_visible(False)
		self.fig.canvas.mpl_connect("motion_notify_event", self.hover)
	
	def update_annot(self, ind):
		pos = self.scatter.get_offsets()[ind["ind"][0]]
		self.annot.xy = pos

		k_lst = []
		v_lst = []

		for k, v in self.num_d.items():
			k_lst.append(k)
			v_lst.append(v)
		print(k_lst, v_lst)
		ans_lst = []
		for line in v_lst:
			ans_lst.append(line[int(ind['ind'])])
		
		text = f"{k_lst[0]}:{ans_lst[0]}"
														
		self.annot.set_text(text)

	def hover(self, event):
		# bool
		vis = self.annot.get_visible()
		# if on the point, update the annot and show on the canvas
		if self.event.inaxes == self.ax:
			cont, ind = self.scatter.contains(event)
			if cont:
				self.update_annot(ind)
				self.annot.set_visible(True)
				self.fig.canvas.draw_idle()
			else:
				# not on the point, so will not show any annot
				if vis:
					self.annot.set_visible(False)
					self.fig.canvas.draw_idle()

	def _scan_registration(self, scan_topic):

		self.angle_min = scan_topic.angle_min  # in radians
		self.angle_max = scan_topic.angle_max  # in radians
		self.angle_increment = scan_topic.angle_increment
		self.range_min = scan_topic.range_min
		self.range_min = scan_topic.range_max
		self.range_arr = scan_topic.ranges  # array of range values
		self.plotting_scan()
		# passing the range info to plotting scan

	def plotting_scan(self):
		self.num_d = {'Distance':self.range_arr}
		x_arr = []
		y_arr = []
		angle_min = self.angle_min
		t = time.time()
		for i in self.range_arr:
			angle_min = angle_min + self.angle_increment
			x = i * np.cos(angle_min)
			y = i * np.sin(angle_min)
			x_arr.append(x)
			y_arr.append(y)

		self.x_arr = x_arr
		self.y_arr = y_arr

		# print(x_arr)
		# return x_arr, y_arr

	def _update(self, i):
		points = np.transpose(np.array([self.y_arr, self.x_arr]))
		self.scatter.set_offsets(points)
		return self.scatter,

	def start(self):
		self.anim = FuncAnimation(
			self.fig, self._update, interval=20, blit=True)


if __name__ == "__main__":
	rospy.init_node("scan_node", anonymous=False)
	scan_topic = "/laser/scan"
	read = lidar_plot(scan_topic)
	read.start()
	# plt.axes("equal")
	plt.show()

	rospy.spin()