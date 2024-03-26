import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_graph(x_data, y_data, z_data):
    """
    Plots a 3D graph using X, Y, and Z axis data.

    Args:
    - x_data (list): List of X axis data points.
    - y_data (list): List of Y axis data points.
    - z_data (list): List of Z axis data points.

    Returns:
    - None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_data, y_data, z_data)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()


# x_data = [1, 2, 3, 4, 5]
# y_data = [2, 3, 4, 5, 6]
# z_data = [3, 4, 5, 6, 7]

# plot_3d_graph(x_data, y_data, z_data)


import matplotlib.pyplot as plt

def plot_2d_graph(x_data, y_data):
    """
    Plots a 2D graph using X and Y axis data.

    Args:
    - x_data (list): List of X axis data points.
    - y_data (list): List of Y axis data points.

    Returns:
    - None
    """
    plt.plot(x_data, y_data)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('2D Graph')
    plt.grid(True)
    plt.show()


# x_data = [1, 2, 3, 4, 5]
# y_data = [2, 3, 4, 5, 6]

# plot_2d_graph(x_data, y_data)





