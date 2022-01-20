import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # for 3D plotting

if __name__ == "__main__":
    # create figure and set figure size and dpi (dots per inch)
    fig = plt.figure(figsize=(10, 6), dpi=80)
    ax = Axes3D(fig)

    # inputs
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)

    X, Y = np.meshgrid(X, Y)

    # 3D surface
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    # Métodos para graficar en un espacio tridimensional
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.magma)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.magma)

    # set z axis limit
    ax.set_zlim(-3, 3)

    plt.show()