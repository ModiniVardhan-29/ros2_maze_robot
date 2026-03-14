#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class CBLMNode(Node):
    def __init__(self):
        super().__init__('cblm_node')
        print("✅ Python file executed")
        self.get_logger().info("✅ CBLM ROS2 Node Started")

def main(args=None):
    print("🚀 main() function entered")
    rclpy.init(args=args)
    node = CBLMNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

