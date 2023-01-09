import math
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi
import lidar_to_grid as lg

def file_read(f):
    """
    Reading LIDAR laser beams (angles and corresponding distance data)
    """
    measures = [line.split(",") for line in open(f)]
    angles = []
    distances = []
    for measure in measures:
        try:
            angles.append(float(measure[2][0:-1]))
            distances.append(float(measure[0]))
        except:
            pass
    angles = np.array(angles)
    distances = np.array(distances)
    return angles, distances
#print(file_read("ok.csv"))

ang, dist = file_read("ok.csv")
ox = np.sin(ang) * dist
oy = np.cos(ang) * dist
plt.figure(figsize=(10,5))
plt.scatter([ox], [oy], color="red", s= 2) # lines from 0,0 to the
plt.axis("equal")
bottom, top = plt.ylim()  # return the current ylim
plt.ylim((top, bottom)) # rescale y axis, to match the grid orientation
plt.grid(True)
plt.show()

xyreso = 0.02  # x-y grid resolution
yawreso = math.radians(3.1)  # yaw angle resolution [rad]
ang, dist = file_read("ok.csv")
ox = np.sin(ang) * dist
oy = np.cos(ang) * dist
pmap, minx, maxx, miny, maxy, xyreso = lg.generate_ray_casting_grid_map(ox, oy, xyreso, False)
xyres = np.array(pmap).shape
plt.figure(figsize=(20,8))
#plt.subplot(122)
plt.imshow(pmap, cmap = "PiYG_r")
plt.clim(-0.4, 1.4)
plt.gca().set_xticks(np.arange(-.5, xyres[1], 1), minor = True)
plt.gca().set_yticks(np.arange(-.5, xyres[0], 1), minor = True)
plt.grid(True, which="minor", color="w", linewidth = .6, alpha = 0.5)
plt.colorbar()
plt.show()
