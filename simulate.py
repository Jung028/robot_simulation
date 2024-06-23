import time
from robot import Robot
from plot import plot_robot, setup_plot
import matplotlib.pyplot as plt

def simulate_robot():
    robot = Robot()
    fig, ax = setup_plot()  # Initialize the plot outside the loop

    for _ in range(100):
        ax.clear()  # Clear the previous plot
        plot_robot(robot, ax)  # Plot the updated robot position
        plt.draw()  # Redraw the plot
        plt.pause(0.1)  # Pause to display the plot
        
        # Example movement: move forward with v=1 and rotate with omega=0.1
        robot.move(1, 0.1, 0.1)

    plt.show()  # Show the final plot after all iterations

if __name__ == "__main__":
    simulate_robot()
