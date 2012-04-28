from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# This example demonstrates mplot3d's offset text display.
# As one rotates the 3D figure, the offsets should remain oriented
# same way as the axis label, and should also be located "away"
# from the center of the plot.
#
# This demo triggers the display of the offset text for the x and
# y axis by adding 1e5 to X and Y. Anything less would not
# automatically trigger it.

fig = plt.figure()
#fig.patch.set_facecolor('white')
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
X, Y = np.mgrid[0.2:2:0.02, 0.2:2:0.02]
#Z = np.sqrt(np.abs(np.cos(X) + np.cos(Y)))
def MyZ(X, Y):
    #Z = X[::]
    Z = (Y > X) * (Y / X) + (X >= Y) * (X / Y)
    #Z[(Z == np.nan)] = 0
    #Z[(Z == np.inf)] = 0
    return Z

Z = MyZ(X, Y)
#surf = ax.plot_surface(X, Y, Z, cstride=1, rstride=1)
surf = ax.plot_surface(X, Y, Z, linewidth=0, cstride=1, rstride=1, cmap=cm.jet)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("abs_ratio")
ax.set_zlim(0, 10)

plt.show()
