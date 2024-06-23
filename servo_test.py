# servo_control/src/test_servo_publisher.py
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16MultiArray
import time

def test_servo_publisher():
    pub = rospy.Publisher('servo_angle', Int16MultiArray, queue_size=10)
    rospy.init_node('test_servo_publisher', anonymous=True)

    num_loops = 3
    servo_pins = range(12)  # Pins 0 to 11

    def publish_angles(angles):
        msg = Int16MultiArray()
        msg.data = []
        for pin in servo_pins:
            msg.data.append(pin)
            msg.data.append(angles)
        pub.publish(msg)

    for _ in range(num_loops):
        # Move from 0 to 180 degrees
        for angle in range(0, 181, 10):  # Adjust the step for smoother motion
            publish_angles(angle)
            time.sleep(0.1)  # Adjust the delay for smoother motion

        # Move from 180 to 0 degrees
        for angle in range(180, -1, -10):
            publish_angles(angle)
            time.sleep(0.1)

    rospy.signal_shutdown("Finished moving servos")

if __name__ == '__main__':
    try:
        test_servo_publisher()
    except rospy.ROSInterruptException:
        pass
