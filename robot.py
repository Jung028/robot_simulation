import numpy as np 

class Robot:
    def __init__(self, x=0, y=0, theta = 0):
        self.x = x
        self.y = y
        self.theta = theta 
        
    #Move the robot with a given linear velocity v and angular velocity omega for time dt.
    def move(self, v, omega, dt):
        self.x += v * np.cos(self.theta) * dt
        self.y += v * np.sin(self.theta) * dt
        self.theta += omega * dt
    
    def get_position(self):
        return self.x, self.y, self.theta
