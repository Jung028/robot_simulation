import time
from robot import Robot
from plot import plot_robot, setup_plot
import matplotlib.pyplot as plt

def simulate_robot():
    robot = Robot()
    fig, ax = setup_plot()

    for _ in range(100):
        ax.clear()
        setup_plot()
        plot_robot(robot, ax)
        plt.draw()
        plt.pause(0.1)
        
        # Example movement: move forward with v=1 and rotate with omega=0.1
        robot.move(1, 0.1, 0.1)
        
        # Optional: time.sleep(0.1) to slow down the loop

    plt.show()

if __name__ == "__main__":
    simulate_robot()
