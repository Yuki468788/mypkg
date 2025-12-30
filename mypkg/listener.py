#!/usr/bin/python
# SPDX-FileCopyrightText: 2025 Yuki Akutsu
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub_state = self.create_subscription(String,'timer_state',self.state_callback,10)

        self.sub_time = self.create_subscription(Int16,'remaining_seconds',self.time_callback,10)
        self.current_state = "UNKNOWN"

    def state_callback(self, msg):
        self.current_state = msg.data

    def time_callback(self, msg):
        seconds = msg.data
        mins = seconds // 60
        secs = seconds % 60
        self.get_logger().info(f"[{self.current_state}] | Remaining:{mins:02d}:{secs:02d}")
def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()
