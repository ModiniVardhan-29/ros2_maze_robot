#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Subscriber to laser scan
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        # Publisher for velocity
        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.twist = Twist()

    def scan_callback(self, msg):

    ranges = list(msg.ranges)
    n = len(ranges)

    center = n // 2

    # Front is around center
    front_indices = list(range(center-10, center+10))

    # Left ~ 90 degrees
    left_start = center + 60
    left_end   = center + 120

    # Right ~ -90 degrees
    right_start = center - 120
    right_end   = center - 60

    self.front = self.safe_min([ranges[i] for i in front_indices])
    self.left  = self.safe_min(ranges[left_start:left_end])
    self.right = self.safe_min(ranges[right_start:right_end])


def main(args=None):

    rclpy.init(args=args)

    node = ObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
