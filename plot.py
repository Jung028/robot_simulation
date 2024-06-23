import matplotlib.pyplot as plt
from matplotlib.patches import Arrow

# draw the robot 
def plot_robot(robot, ax):
    x, y, theta = robot.get_position()
    arrow = Arrow(x, y, 0.5 * np.cos(theta), 0.5 * np.sin(theta), width=0.3)
    ax.add_patch(arrow)

def setup_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    return fig, ax
