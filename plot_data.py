import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi
from matplotlib.animation import FuncAnimation
from itertools import count


plt.style.use('fivethirtyeight')



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

# ang, dist = file_read("ok.csv")
# ox = np.sin(ang) * dist
# oy = np.cos(ang) * dist
# plt.figure(figsize=(10,5))
# plt.scatter([ox], [oy], color="red", s= 2) # lines from 0,0 to the
# plt.axis("equal")
# bottom, top = plt.ylim()  # return the current ylim
# plt.ylim((top, bottom)) # rescale y axis, to match the grid orientation
# plt.grid(True)

index = count()


def animate(i):
    ang, dist = file_read("ok.csv")
    ox = np.sin(ang) * dist
    oy = np.cos(ang) * dist    
    plt.cla()
    plt.scatter([ox], [oy], color="red", s= 2) # lines from 0,0 to the
    # plt.axis("equal")
    # bottom, top = plt.ylim()  
    # return the current ylim
    plt.ylim((6, -6))
    
    # rescale y axis, to match the grid orientation

    # plt.gcf().autofmt_xdate()
    # plt.tight_layout()

ani = FuncAnimation(plt.figure(), animate, 10)


# plt.tight_layout()
plt.show()
