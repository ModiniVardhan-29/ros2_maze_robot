#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

    def get_distance(self, msg, angle_deg):
        """
        Return distance at a given angle
        """

        angle_rad = math.radians(angle_deg)

        index = int((angle_rad - msg.angle_min) / msg.angle_increment)

        if index < 0 or index >= len(msg.ranges):
            return 8.0

        distance = msg.ranges[index]

        if math.isinf(distance) or distance < 0.2:
            return 8.0

        return distance

    def scan_callback(self, msg):

        front = self.get_distance(msg, 0)
        left = self.get_distance(msg, 90)
        right = self.get_distance(msg, -90)

        cmd = Twist()

        threshold = 0.8

        # Debug print (optional)
        print(f"Front: {front:.2f}  Left: {left:.2f}  Right: {right:.2f}")

        # If path ahead is clear → move forward
        if front > threshold:
            cmd.linear.x = 0.35
            cmd.angular.z = 0.0

        # Obstacle ahead
        else:

            cmd.linear.x = 0.0

            if left > right:
                cmd.angular.z = 0.7
            else:
                cmd.angular.z = -0.7

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = ObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
